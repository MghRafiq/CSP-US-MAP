
# Import des bibliothèques nécessaires
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict

# Classe pour résoudre le problème de satisfaction de contraintes (PSC)
class CSP:
    def __init__(self, variables: List[str], domains: Dict[str, List[str]], constraints: Dict[str, List[str]]):
        """
        Initialiser un problème de satisfaction de contraintes (PSC).
        :param variables: Liste des variables (régions à colorier).
        :param domains: Dictionnaire associant chaque variable à son domaine de valeurs possibles.
        :param constraints: Dictionnaire des contraintes (adjacences des régions).
        """
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_valid_assignment(self, variable: str, value: str, assignment: Dict[str, str]) -> bool:
        """
        Vérifie si une affectation est valide selon les contraintes.
        """
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack(self, assignment: Dict[str, str] = {}) -> Dict[str, str]:
        """
        Résolution du PSC par backtracking.
        """
        if len(assignment) == len(self.variables):  # Si toutes les variables sont affectées
            return assignment

        unassigned = [var for var in self.variables if var not in assignment]
        current_var = unassigned[0]  # Choix de la première variable libre

        for value in self.domains[current_var]:
            if self.is_valid_assignment(current_var, value, assignment):
                assignment[current_var] = value
                result = self.backtrack(assignment)
                if result:  # Si une solution est trouvée
                    return result
                del assignment[current_var]  # Backtracking
        return None  # Aucune solution trouvée


# Fonction pour afficher le graphe et ses couleurs à chaque étape
def plot_graph(graph, coloring=None, title=""):
    pos = nx.spring_layout(graph)  # Positionner les nœuds
    node_colors = [coloring[node] if coloring and node in coloring else "white" for node in graph.nodes]
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=800, font_size=10)
    plt.title(title)
    plt.show()


# Définir les régions, couleurs et contraintes
variables = ['A', 'B', 'C', 'D', 'E']
domains = {var: ['red', 'green', 'blue', 'yellow'] for var in variables}
constraints = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Création d'une instance CSP
csp = CSP(variables, domains, constraints)

# Résolution du problème
solution = csp.backtrack()

# Création du graphe des régions
graph = nx.Graph()
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
graph.add_nodes_from(variables)
graph.add_edges_from(edges)

# Visualiser les étapes
plot_graph(graph, title="Graphe des régions et contraintes (Initial)")

if solution:
    # Affichage progressif des colorations
    plot_graph(graph, title="Étape 1 : Aucune région colorée")
    partial_coloring = {}

    # Ajouter et afficher chaque coloration étape par étape
    for region, color in solution.items():
        partial_coloring[region] = color
        plot_graph(graph, coloring=partial_coloring, title=f"Coloration progressive : Région {region} colorée en {color}")

    # Affichage final
    plot_graph(graph, coloring=solution, title="Résultat final : Graphe coloré")
else:
    print("Aucune solution trouvée.")
