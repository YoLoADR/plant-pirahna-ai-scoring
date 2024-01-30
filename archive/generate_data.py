import pandas as pd
import numpy as np

n_projects = 100  # Nombre de projets
np.random.seed(0)  # Pour la reproductibilité

data = {
    "id": range(1, n_projects + 1),
    "location": np.random.choice(["Location1", "Location2", "Location3"], n_projects),
    "price": np.random.uniform(100000, 500000, n_projects),
    "property_type": np.random.choice(["Residential", "Commercial"], n_projects),
    "property_size": np.random.uniform(50, 500, n_projects)  # Taille de la propriété en m²
}

# Modifier les données en fonction de la localisation
for i in range(n_projects):
    if data["location"][i] == "Location1":
        data["price"][i] *= 0.8  # Réduire les prix pour la localisation 1
        data["property_size"][i] *= 0.8  # Réduire les tailles pour la localisation 1
    elif data["location"][i] == "Location3":
        data["property_type"][i] = np.random.choice(["Residential", "Commercial"], p=[0.2, 0.8])  # Plus de commerciaux pour la localisation 3

df = pd.DataFrame(data)
print(df.head())  # Affiche les premières lignes pour vérifier
print(df.columns) # Afficher les noms des colonnes
df.to_csv("real_estate_data.csv", index=False)  # Enregistrez les données dans un fichier CSV
