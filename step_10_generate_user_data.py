import pandas as pd
import numpy as np

# Définit le nombre d'utilisateurs et de projets pour la simulation
num_users = 100
num_projects = 50

# Génère un nombre aléatoire d'investissements pour chaque utilisateur
investments_per_user = np.random.randint(5, 15, num_users)

# Crée une liste de tous les projets possibles
all_project_ids = np.arange(1, num_projects + 1)

# Initialise les listes pour stocker les données générées
user_ids = []
ages = []
genders = []
preferred_locations = []
preferred_property_types = []
max_prices = []
min_property_sizes = []
investment_history_project_ids = []
invested_amounts = []
investment_history_locations = []
investment_history_property_types = []
investment_history_property_sizes = []

# Boucle sur chaque utilisateur pour générer des données
for user_id in range(1, num_users + 1):
    # Génère un nombre aléatoire d'investissements pour cet utilisateur
    num_investments = np.random.randint(5, 15)
    
    # Ajoute les informations de base de l'utilisateur à chaque investissement
    user_ids.extend([user_id] * num_investments)
    age = np.random.randint(18, 70)
    ages.extend([age] * num_investments)
    gender = np.random.choice(["Male", "Female"])
    genders.extend([gender] * num_investments)
    preferred_location = np.random.choice(["Location1", "Location2", "Location3"])
    preferred_locations.extend([preferred_location] * num_investments)
    preferred_property_type = np.random.choice(["Residential", "Commercial"])
    preferred_property_types.extend([preferred_property_type] * num_investments)
    max_price = np.random.randint(100000, 50000000)
    max_prices.extend([max_price] * num_investments)
    min_property_size = np.random.randint(50, 200)
    min_property_sizes.extend([min_property_size] * num_investments)
    
    # Sélectionne un ensemble aléatoire de projets dans lesquels l'utilisateur investit
    projects = np.random.choice(all_project_ids, num_investments, replace=False)
    investment_history_project_ids.extend(projects)
    
    # Génère des données d'investissement pour chaque projet sélectionné
    invested_amounts.extend(np.random.randint(50000, 400000, num_investments))
    investment_history_locations.extend(np.random.choice(["Location1", "Location2", "Location3"], num_investments))
    investment_history_property_types.extend(np.random.choice(["Residential", "Commercial"], num_investments))
    investment_history_property_sizes.extend(np.random.randint(50, 200, num_investments))

# Crée un dictionnaire avec les listes générées
data = {
    'user_id': user_ids,
    'age': ages,
    'gender': genders,
    'preferred_location': preferred_locations,
    'preferred_property_type': preferred_property_types,
    'max_price': max_prices,
    'min_property_size': min_property_sizes,
    'investment_history_project_id': investment_history_project_ids,
    'invested_amount': invested_amounts,
    'investment_history_location': investment_history_locations,
    'investment_history_property_type': investment_history_property_types,
    'investment_history_property_size': investment_history_property_sizes,
}

# Convertit le dictionnaire en un DataFrame pour une manipulation facile
user_data_df = pd.DataFrame(data)

# Exporter les données en CSV
csv_file_path = "basic_user_investment_data.csv"
user_data_df.to_csv(csv_file_path, index=False)

print(f"Les données ont été générées et sauvegardées dans {csv_file_path}")
