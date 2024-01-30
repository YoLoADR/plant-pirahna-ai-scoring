import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

# Charger les données
df = pd.read_csv("real_estate_data.csv")

# Séparer les colonnes numériques
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Traitement des valeurs manquantes pour les colonnes numériques
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Élimination des outliers spécifiques dans la colonne 'price'
df = df[df['price'] >= 10000]

# Élimination des outliers pour les autres colonnes numériques
for col in numeric_cols:
    if col != 'price':  # Ne pas réappliquer le filtre sur la colonne 'price'
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# Sélection des features, en excluant 'id'
X = df[numeric_cols].drop(['price', 'id'], axis=1)  # Exclure la colonne 'id' ainsi que la variable cible 'price'
y = df['price']  # Variable cible (prix)

# Vérifier le nombre de features et ajuster k en conséquence
k = min(3, X.shape[1])
best_features = SelectKBest(score_func=f_regression, k=k)  # Sélectionne les meilleures features jusqu'à k
fit = best_features.fit(X, y)
X_new = fit.transform(X)

# Afficher les noms des features sélectionnées
selected_feature_names = X.columns[fit.get_support(indices=True)]
print("Features sélectionnées:", selected_feature_names)
df.to_csv("real_estate_data_cleaned.csv", index=False)
