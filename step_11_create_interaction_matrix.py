import pandas as pd
import numpy as np


# Lire les données
df = pd.read_csv("basic_user_investment_data.csv")


# Préparation de la matrice d'interactions
# Ici, on assume que chaque ligne dans le CSV représente une interaction unique utilisateur-projet
# L'objectif est de créer une matrice où chaque cellule (i, j) représente le montant investi de l'utilisateur i dans le projet j

# Créer une matrice vide avec des utilisateurs en lignes et des projets en colonnes
users = df['user_id'].unique()
projects = df['investment_history_project_id'].unique()
interaction_matrix = pd.DataFrame(0, index=users, columns=projects, dtype=np.float64)

# Remplir la matrice avec le montant investi
for _, row in df.iterrows():
    interaction_matrix.at[row['user_id'], row['investment_history_project_id']] += row['invested_amount']

# Afficher la matrice pour vérification
print(interaction_matrix.head())
