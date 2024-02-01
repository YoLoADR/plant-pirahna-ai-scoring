import pandas as pd

# Lire les données
df = pd.read_csv("basic_user_investment_data.csv")

# Calculer le montant total investi et le nombre de réinvestissements par utilisateur
performance_metrics = df.groupby('user_id').agg(
    total_invested=pd.NamedAgg(column='invested_amount', aggfunc='sum'),
    projects_invested=pd.NamedAgg(column='investment_history_project_id', aggfunc='count')
).reset_index()

# Identifier les utilisateurs performants (exemple basique)
# Tu peux définir "performant" selon tes critères spécifiques (e.g., montant total, nombre de projets)
threshold_investment = performance_metrics['total_invested'].quantile(0.75)  # Exemple : utilisateurs dans le top 25% des investissements
threshold_projects = performance_metrics['projects_invested'].quantile(0.75)  # Exemple : top 25% en nombre de projets

performant_users = performance_metrics[
    (performance_metrics['total_invested'] >= threshold_investment) &
    (performance_metrics['projects_invested'] >= threshold_projects)
]

# Afficher les utilisateurs performants
print(performant_users)