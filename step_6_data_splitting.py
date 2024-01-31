import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Step 6 : Data Division
# This script will focus on splitting the transformed data into training and testing sets.

# Charger les données transformées
df_encoded = pd.read_csv("real_estate_data_transformed.csv")

# Prendre le logarithme de la variable 'price'
df_encoded['price'] = np.log(df_encoded['price'])

# Séparer les données en features (X) et target (y)
X = df_encoded.drop('price', axis=1)
y = df_encoded['price']

# Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sauvegarder ces ensembles dans des fichiers séparés pour une utilisation ultérieure
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

# Afficher quelques informations sur les ensembles de données
print(f"Dimensions de X_train: {X_train.shape}")
print(f"Dimensions de X_test: {X_test.shape}")
print(f"Dimensions de y_train: {y_train.shape}")
print(f"Dimensions de y_test: {y_test.shape}")
