import geopandas as gpd
import networkx as nx
import folium
import matplotlib.pyplot as plt
import imageio
import os

# # Chemins des fichiers
# input_path = r'C:\Users\rafiq\Desktop\M1_MIAGE\S7\PROGMATH\PSC_Projet\data\us-states.json'
# output_html_path = r'C:\Users\rafiq\Desktop\M1_MIAGE\S7\PROGMATH\PSC_Projet\exports\us_states_coloration.html'
# output_gif_path = r'C:\Users\rafiq\Desktop\M1_MIAGE\S7\PROGMATH\PSC_Projet\exports\coloration_animation.gif'
# images_dir = r'C:\Users\rafiq\Desktop\M1_MIAGE\S7\PROGMATH\PSC_Projet\exports\images'

# Chemins relatifs
input_path = '../data/us-states.json'
output_html_path = '../exports/us_states_coloration.html'
output_gif_path = '../exports/coloration_animation.gif'
images_dir = '../exports/images'

# Créer le répertoire pour les images si nécessaire
os.makedirs(images_dir, exist_ok=True)

# Charger les données géographiques
gdf = gpd.read_file(input_path)

# S'assurer que les géométries sont valides
gdf['geometry'] = gdf['geometry'].buffer(0)

# Construire le graphe des adjacences
G = nx.Graph()
for idx, row in gdf.iterrows():
    G.add_node(row['name'])  # 'name' est la colonne contenant les noms des États
    for neighbor in gdf[gdf.geometry.touches(row['geometry'])].itertuples():
        G.add_edge(row['name'], neighbor.name)

# Appliquer l'algorithme DSATUR
colors = ['red', 'green', 'blue', 'yellow']
color_map = {}
images = []

# Calculer le degré de saturation initial de chaque nœud
saturation = {node: 0 for node in G.nodes()}
degrees = dict(G.degree())

# Créer une carte interactive avec Folium
m = folium.Map(location=[37.8, -96], zoom_start=4)

# l'algorithme DSATUR est appliqué pour colorier le graphe, en attribuant à chaque nœud une couleur différente de celles de ses voisins.
while len(color_map) < len(G.nodes()):
    # Sélectionner le nœud avec le degré de saturation le plus élevé
    # En cas d'égalité, choisir celui avec le degré le plus élevé
    node = max((n for n in G.nodes() if n not in color_map),
               key=lambda n: (saturation[n], degrees[n]))

    # Déterminer les couleurs déjà utilisées par les voisins
    neighbor_colors = {color_map[neighbor] for neighbor in G.neighbors(node) if neighbor in color_map}
    available_colors = [color for color in colors if color not in neighbor_colors]

    if available_colors:
        chosen_color = available_colors[0]
        color_map[node] = chosen_color
        gdf.loc[gdf['name'] == node, 'color'] = chosen_color
    else:
        raise ValueError(f"Aucune couleur disponible pour le nœud {node}.")

    # Mettre à jour le degré de saturation des voisins non colorés
    for neighbor in G.neighbors(node):
        if neighbor not in color_map:
            saturation[neighbor] += 1

    # Ajouter l'état coloré à la carte Folium
    state_geo = gdf[gdf['name'] == node].__geo_interface__
    folium.GeoJson(
        state_geo,
        style_function=lambda feature, color=chosen_color: {
            'fillColor': color,
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.6,
        },
        tooltip=f"{node}: {chosen_color}"
    ).add_to(m)

    # Enregistrer une image de l'état actuel de la coloration
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    gdf.plot(ax=ax, color=gdf['color'].fillna('white'), edgecolor='black')
    plt.title(f'Étape {len(color_map)}: Coloration de {node}')
    image_path = os.path.join(images_dir, f'step_{len(color_map):03d}.png')
    plt.savefig(image_path)
    plt.close(fig)
    images.append(image_path)

# Enregistrer la carte interactive en HTML
m.save(output_html_path)
print(f"Carte interactive enregistrée sous '{output_html_path}'.")

# Créer un GIF animé à partir des images enregistrées
with imageio.get_writer(output_gif_path, mode='I', duration=0.2) as writer:
    for image_path in images:
        image = imageio.imread(image_path)
        writer.append_data(image)
print(f"Animation GIF enregistrée sous '{output_gif_path}'.")
