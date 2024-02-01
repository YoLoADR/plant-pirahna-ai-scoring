from surprise import Dataset, Reader, accuracy
from surprise.model_selection import train_test_split, cross_validate
import joblib
import pandas as pd

# Charger la matrice d'interaction transformée
transformed_data_path = 'transformed_interaction_matrix.csv'
df = pd.read_csv(transformed_data_path)

# Configurer le Reader avec le bon rating_scale
reader = Reader(rating_scale=(100000, 50000000))  # Ajuster selon tes données

# Charger les données dans Surprise
data = Dataset.load_from_df(df[['user_id', 'project_id', 'invested_amount']], reader)

# Séparer les données en ensembles d'entraînement et de test
trainset, testset = train_test_split(data, test_size=0.2)

# Charger le modèle préalablement entraîné avec joblib
# Assure-toi que le chemin vers ton fichier de modèle est correct
algo = joblib.load('invest_wise_recommender.pkl')

# Faire des prédictions sur l'ensemble de test
predictions = algo.test(testset)

# Note: L'erreur que tu as rencontrée semblait impliquer un problème avec les valeurs None.
# Cela pourrait être dû à des valeurs manquantes dans tes données ou un problème lors de la prédiction.
# Le filtrage des prédictions avec des valeurs r_ui None n'est normalement pas nécessaire si tes données sont complètes.

# Calculer l'erreur RMSE (Root Mean Squared Error) et MAE (Mean Absolute Error)
rmse = accuracy.rmse(predictions)
mae = accuracy.mae(predictions)

# Afficher les erreurs
print(f'RMSE: {rmse}')
print(f'MAE: {mae}')

# Validation croisée pour une évaluation plus robuste
results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Affichage des résultats de la validation croisée
print(results)
