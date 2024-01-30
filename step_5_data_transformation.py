import pandas as pd
from sklearn.preprocessing import StandardScaler

# Charger les données nettoyées
df = pd.read_csv("real_estate_data_cleaned.csv")

# Séparer les variables catégorielles et numériques
categorical_vars = ['location', 'property_type']  # Liste des variables catégorielles
numeric_vars = [col for col in df.columns if col not in categorical_vars + ['price', 'id']]  # Exclure 'price' et 'id'

# One-Hot Encoding pour les variables catégorielles
df_encoded = pd.get_dummies(df, columns=categorical_vars)

# Normalisation des variables numériques
scaler = StandardScaler()
df_encoded[numeric_vars] = scaler.fit_transform(df_encoded[numeric_vars])

# Retirer la colonne 'id' (après la normalisation et le One-Hot Encoding)
df_encoded = df_encoded.drop('id', axis=1)

# Sauvegarder les données transformées
df_encoded.to_csv("real_estate_data_transformed.csv", index=False)
