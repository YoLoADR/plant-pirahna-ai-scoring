import pandas as pd
import numpy as np

# Charger les données
df = pd.read_csv("real_estate_data_cleaned.csv")

# Ajouter un score basé sur le prix (par exemple, prix plus bas obtient un score plus élevé)
max_price = df['price'].max()
df['score'] = df['price'].apply(lambda x: (max_price - x) / max_price)

# Définir les préférences de l'investisseur
preferences = {
    'budget_max': 10000000,
    'location': 'Location1',
    'property_type': 'Residential',
    'property_size': 200
}

# Filtrer les projets en fonction des préférences
filtered_projects = df[
    (df['price'] <= preferences['budget_max']) &
    (df['location'] == preferences['location']) &
    (df['property_type'] == preferences['property_type'])
]

# Trier les projets par score
recommended_projects = filtered_projects.sort_values(by='score', ascending=False)

#TEST
print("Nombre de projets après le nettoyage : ", df.shape[0])
print("Nombre de projets après le filtrage : ", filtered_projects.shape[0])

print(df['location'].unique())  # Vérifiez les valeurs uniques pour la localisation
print(df['property_type'].unique())  # Vérifiez les types de propriété
print(df['price'].max(), df['price'].min())  # Vérifiez la plage de prix

print("Projets avec prix <= 400000: ", df[df['price'] >= 400000].shape[0])
print("Projets à Location1: ", df[df['location'] == 'Location1'].shape[0])
print("Projets de type Residential: ", df[df['property_type'] == 'Residential'].shape[0])


# Afficher les 5 meilleurs projets recommandés
print(recommended_projects.head(5))
