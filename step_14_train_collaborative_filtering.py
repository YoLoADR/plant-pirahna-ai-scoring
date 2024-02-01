import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

print("Chargement et transformation de la matrice d'interaction...")
interaction_matrix_df = pd.read_csv("interaction_matrix.csv", index_col=0)
interaction_long_df = interaction_matrix_df.stack().reset_index()
interaction_long_df.columns = ['user_id', 'project_id', 'invested_amount']

# Assure-toi que 'invested_amount' > 0
interaction_long_df = interaction_long_df[interaction_long_df['invested_amount'] > 0]

print("Regroupement par utilisateur et projet...")
# Regrouper par utilisateur et projet, et sommer les montants investis
interaction_grouped = interaction_long_df.groupby(['user_id', 'project_id']).agg({'invested_amount': 'sum'}).reset_index()

print("Préparation de la matrice utilisateur-projet...")
# Pivoter le DataFrame pour obtenir une matrice utilisateur-projet
user_project_matrix = interaction_grouped.pivot(index='user_id', columns='project_id', values='invested_amount').fillna(0)

print("Calcul de la similarité cosinus entre les utilisateurs...")
# Calcul de la similarité cosinus
cosine_sim = cosine_similarity(user_project_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=user_project_matrix.index, columns=user_project_matrix.index)

def recommend_projects(user_id, cosine_sim_df, user_project_matrix, top_n=5):
    print(f"Recherche de projets à recommander pour l'utilisateur {user_id}...")
    similar_users = cosine_sim_df.loc[user_id].sort_values(ascending=False)[1:top_n+1].index
    recommended_projects = set()
    user_projects = set(user_project_matrix.loc[user_id][user_project_matrix.loc[user_id] > 0].index)
    
    for similar_user in similar_users:
        similar_user_projects = set(user_project_matrix.loc[similar_user][user_project_matrix.loc[similar_user] > 0].index) - user_projects
        recommended_projects = recommended_projects.union(similar_user_projects)
    
    return list(recommended_projects)[:top_n]

def recommend_based_on_top_users(user_project_matrix, top_n=5):
    print("Recherche de projets basés sur les meilleurs utilisateurs...")
    top_users = user_project_matrix.sum(axis=1).sort_values(ascending=False).head(top_n).index
    recommended_projects = set()
    
    for top_user in top_users:
        top_user_projects = set(user_project_matrix.loc[top_user][user_project_matrix.loc[top_user] > 0].index)
        recommended_projects = recommended_projects.union(top_user_projects)
    
    return list(recommended_projects)[:top_n]

# Exemple d'utilisation
user_id_example = 1
individual_recommendations = recommend_projects(user_id_example, cosine_sim_df, user_project_matrix)
print("Recommandations basées sur l'historique individuel :", individual_recommendations)

top_user_recommendations = recommend_based_on_top_users(user_project_matrix)
print("Recommandations basées sur les meilleurs utilisateurs :", top_user_recommendations)
