import pandas as pd
import numpy as np

n_projects = 100  # Nombre de projets
np.random.seed(0)  # Pour la reproductibilité

# Création du dictionnaire initial
data = {
    "id": range(1, n_projects + 1),
    "location": np.random.choice(["Location1", "Location2", "Location3"], n_projects),
    "price": np.random.uniform(100000, 50000000, n_projects),
    "property_type": np.random.choice(["Residential", "Commercial"], n_projects),
    "property_size": np.random.uniform(50, 500, n_projects)  # Taille de la propriété en m²
}

# Modifier les données en fonction de la localisation
for i in range(n_projects):
    if data["location"][i] == "Location1":
        data["price"][i] *= 0.8
        data["property_size"][i] *= 0.8
    elif data["location"][i] == "Location3":
        data["property_type"][i] = np.random.choice(["Residential", "Commercial"], p=[0.2, 0.8])

# Sauvegardez les clés du dictionnaire
data_keys = list(data.keys())

# Convertissez le dictionnaire en un tableau numpy pour l'imputation
data_values = np.array(list(data.values())).T

# Introduire des valeurs manquantes
missing_mask = np.random.rand(n_projects, len(data_keys)) < 0.1
data_values = np.where(missing_mask, np.nan, data_values)

# Introduire des valeurs aberrantes uniquement dans la colonne 'price'
outliers_mask = np.random.rand(n_projects) < 0.05  # Masque pour la colonne 'price' uniquement
aberrant_prices = np.random.uniform(1, 1000, size=n_projects)  # Générer des prix aberrants entre 1$ et 1000$

# Appliquer le masque d'outliers uniquement à la colonne 'price'
data["price"] = np.where(outliers_mask, aberrant_prices, data["price"])


# Convertir en DataFrame
df = pd.DataFrame(data_values, columns=data_keys)

print(df.head())  # Affiche les premières lignes pour vérifier
print(df.columns)  # Afficher les noms des colonnes
df.to_csv("real_estate_data.csv", index=False)  # Enregistrez les données dans un fichier CSV


# Obtenir un aperçu des données de prix
df = pd.DataFrame(data)

print("Prix maximum : ", df['price'].max())
print("Prix minimum : ", df['price'].min())
print("Statistiques descriptives des prix :")
print(df['price'].describe())
