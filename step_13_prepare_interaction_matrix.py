import pandas as pd
import numpy as np

# Lire les données
df = pd.read_csv("basic_user_investment_data.csv")

# Créer une matrice vide avec des utilisateurs en lignes et des projets en colonnes
users = df['user_id'].unique()
projects = df['investment_history_project_id'].unique()
interaction_matrix = pd.DataFrame(0, index=users, columns=projects, dtype=np.float64)

# Remplir la matrice avec le montant investi
for _, row in df.iterrows():
    interaction_matrix.at[row['user_id'], row['investment_history_project_id']] += row['invested_amount']

# Afficher la matrice pour vérification
print(interaction_matrix.head())

# Exporter la matrice d'interaction en CSV ou dans un autre format si nécessaire
interaction_matrix.to_csv("interaction_matrix.csv", index=False)
