import pandas as pd
import numpy as np

# Fonction pour générer des données d'utilisateur fictives
def generate_user_data(num_users):
    # Initialisation des listes pour stocker les données
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

    # Boucle pour générer des données pour chaque utilisateur
    for user_id in range(1, num_users + 1):
        user_ids.append(user_id)
        ages.append(np.random.randint(18, 70))
        genders.append(np.random.choice(["Male", "Female"]))
        preferred_locations.append(np.random.choice(["Location1", "Location2", "Location3"]))
        preferred_property_types.append(np.random.choice(["Residential", "Commercial"]))
        max_prices.append(np.random.randint(100000, 50000000))
        min_property_sizes.append(np.random.randint(50, 200))
        investment_history_project_ids.append(np.random.randint(1, 50))
        invested_amounts.append(np.random.randint(50000, 400000))
        investment_history_locations.append(np.random.choice(["Location1", "Location2", "Location3"]))
        investment_history_property_types.append(np.random.choice(["Residential", "Commercial"]))
        investment_history_property_sizes.append(np.random.randint(50, 200))

    # Création d'un DataFrame
    df = pd.DataFrame({
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
    })

    return df

# Générer des données pour 100 utilisateurs comme exemple
num_users = 100
user_data_df = generate_user_data(num_users)

# Exporter les données en CSV
csv_file_path = "basic_user_investment_data.csv"
user_data_df.to_csv(csv_file_path, index=False)

print(f"Les données ont été générées et sauvegardées dans {csv_file_path}")
