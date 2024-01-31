## Étapes pour Déboguer et Améliorer le Modèle de Régression

### 1. Vérification des Échelles de Données
Assurez-vous que les données numériques sont correctement normalisées et ne contiennent pas d'erreurs après la normalisation. Des valeurs extrêmes ou des erreurs de manipulation des données peuvent conduire à des valeurs de perte élevées.

### 2. Révision des Types de Données
Vérifiez que toutes les colonnes sont du type approprié (`float32` ou `float64`) avant de les passer au modèle.

### 3. [WINNER] Examen de la Variable Cible
Si la variable cible `price` a des valeurs extrêmement élevées, envisagez une transformation (comme la prise de logarithme) pour réduire l'échelle et la dispersion.

### 4. Fonction de Perte et Optimiseur
Assurez-vous que la fonction de perte (`mean_squared_error` pour la régression) et l'optimiseur (comme `adam`) sont adaptés à votre problème. Vous pouvez expérimenter avec d'autres fonctions de perte et optimiseurs si nécessaire.

### 5. Réévaluation de l'Architecture du Modèle
Réexaminez le nombre de couches et de neurones dans votre réseau de neurones. Une architecture plus simple peut être plus efficace, surtout pour des ensembles de données de petite taille.

### 6. Hyperparamètres
Modifiez les hyperparamètres tels que le nombre de neurones dans chaque couche, le taux d'apprentissage et la taille des lots (batch size) pour améliorer la convergence du modèle.

### 7. Initialisation des Poids
Utilisez une initialisation appropriée pour les poids de votre modèle, car cela peut affecter l'apprentissage.

### 8. Normalisation des Sorties
Si nécessaire, appliquez une normalisation distincte à la variable cible, surtout si elle présente une grande dispersion.

### 9. Analyse de l'Histoire de l'Entraînement
Examinez comment la perte a évolué pendant l'entraînement en analysant le fichier `model_history.pkl`. Cela peut indiquer si l'entraînement s'est stabilisé ou non.

### 10. Réajustement du Modèle
En fonction des analyses ci-dessus, ajustez votre modèle et réessayez l'entraînement pour améliorer les performances.
