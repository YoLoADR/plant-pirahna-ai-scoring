import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  # Assurez-vous d'importer pandas au début de votre script

# Charger les données
df = pd.read_csv("real_estate_data_cleaned.csv")

# Scatter plot avec des couleurs pour le type de propriété
sns.scatterplot(data=df, x='price', y='property_size', hue='property_type')
plt.title('Scatter Plot de Prix et Taille de la Propriété par Type')
plt.show()

# Boxplot pour voir la distribution des prix par localisation
sns.boxplot(data=df, x='location', y='price')
plt.title('Distribution des Prix par Localisation')
plt.show()

# FacetGrid pour créer un scatter plot pour chaque localisation
g = sns.FacetGrid(df, col="location")
g.map(sns.scatterplot, "price", "property_size")
plt.show()
