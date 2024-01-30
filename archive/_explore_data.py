import pandas as pd

# Charger les données
df = pd.read_csv("real_estate_data.csv")

# Exploration basique
print(df.describe())  # Statistiques descriptives
print(df.columns) # Afficher les noms des colonnes
print(df['location'].value_counts())  # Fréquence des localisations
