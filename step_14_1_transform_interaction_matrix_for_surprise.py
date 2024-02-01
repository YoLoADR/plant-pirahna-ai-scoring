import pandas as pd

# Charger la matrice d'interaction
interaction_matrix_path = 'interaction_matrix.csv'
interaction_matrix_df = pd.read_csv(interaction_matrix_path)

# Transformer la matrice d'interaction en DataFrame long
interaction_long_df = interaction_matrix_df.reset_index().melt(id_vars='index', var_name='project_id', value_name='invested_amount')
interaction_long_df.rename(columns={'index': 'user_id'}, inplace=True)

# Filtrer les lignes où le montant investi est supérieur à 0 pour éliminer les interactions sans investissement
interaction_long_df = interaction_long_df[interaction_long_df['invested_amount'] > 0]

# Sauvegarder le DataFrame transformé pour l'utiliser avec Surprise
transformed_data_path = 'transformed_interaction_matrix.csv'
interaction_long_df.to_csv(transformed_data_path, index=False)

print(f"Les données ont été transformées et sauvegardées dans {transformed_data_path}")
