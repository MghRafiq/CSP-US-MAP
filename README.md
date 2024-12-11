# **Projet Académique : Problème de Satisfaction de Contraintes (CSP)**

Ce projet académique, réalisé en binôme, explore l'application des **Problèmes de Satisfaction de Contraintes (CSP)** pour résoudre le problème de la **coloration de la carte des États-Unis**, en utilisant des algorithmes avancés tels que **DSATUR**. Ce README fournit une description complète du projet, des outils utilisés, et des étapes pour reproduire le travail.

---

## Informations générales

- **Formation** : Master 1 MIAGE
- **Cours** : Programmation mathématique et optimisation
- **Professeur** : Mohammed HADDAD
- **Année académique** : 2024/2025

---

## Membres du binôme

1. **Rafiq MAHROUG** :
   - **Email** : rafiq.mahroug@etu.univ-lyon1.fr
   - **Responsabilités** : Modélisation des CSP et résolution algorithmique.

2. **Abdellatif BENBAHA** :
   - **Email** : abdellatif.benbaha@etu.univ-lyon1.fr
   - **Responsabilités** : Visualisation des résultats et gestion des fichiers géographiques.

---

## Contexte et objectifs

L'objectif principal de ce projet est de :
- **Modéliser la coloration de la carte des États-Unis** en tant que CSP (exemple pratique)
- Utiliser le théorème des quatre couleurs pour réduire le nombre de couleurs nécessaires à la résolution.
- Implémenter et comparer des algorithmes de résolution efficaces, comme **DSATUR**, afin de garantir une solution optimale en minimisant les conflits entre régions adjacentes.

### Pourquoi ce projet ?
Ce projet a une forte pertinence académique car il :
- Combine des concepts fondamentaux de l'**algorithmique**, de la **théorie des graphes**, et des **CSP**.
- Applique des solutions mathématiques et informatiques à un problème géographique concret.
- Illustre des défis pratiques liés à la complexité computationnelle et propose des solutions optimisées.

---

## Structure du projet

Le projet est organisé comme suit :

### 1. **Dossier `data`**
- Contient le fichier GeoJSON de la carte des États-Unis :
  - `us-states.json` : Fichier décrivant les géométries des États.

### 2. **Dossier `codes_python`**
- Contient les scripts Python pour :
  - Modélisation des États-Unis en tant que graphe.
  - Résolution du problème de coloration avec des algorithmes CSP.
  - Génération de sorties visuelles (GIF et carte interactive).

### 3. **Dossier `exports`**
- Contient les résultats générés :
  - `us_states_coloration.html` : Carte interactive des États-Unis avec les États colorés.
  - `coloration_animation.gif` : Animation montrant les étapes progressives de la coloration.

---

## Configuration de l'environnement

### Outils requis :
- **Python 3.8+**
- Bibliothèques Python suivantes (à installer avec `pip`) :
  - `geopandas`
  - `matplotlib`
  - `folium`
  - `networkx`
  - `imageio`

### Installation des dépendances :
Exécutez la commande suivante pour installer toutes les bibliothèques nécessaires :
```bash
pip install geopandas matplotlib folium networkx imageio
