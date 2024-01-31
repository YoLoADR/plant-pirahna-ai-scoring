import pandas as pd
import pickle
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Charger les données
X_train = pd.read_csv("X_train.csv").astype('float32')
X_test = pd.read_csv("X_test.csv").astype('float32')
y_train = pd.read_csv("y_train.csv")['price'].astype('float32')
y_test = pd.read_csv("y_test.csv")['price'].astype('float32')

# Définir un callback pour l'arrêt précoce
early_stopping = EarlyStopping(monitor='val_loss', patience=5)

# Modèle initial
model_original = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dense(1)
])

# Modèle avec plus de couches
model_deep = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])

# Modèle avec moins de couches
model_shallow = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(1)
])

# Liste des modèles à évaluer
models = [model_original, model_deep, model_shallow]
model_names = ['Original', 'Deep', 'Shallow']

# Entraîner et évaluer chaque modèle
for i, model in enumerate(models):
    print(f"Training {model_names[i]} Model")
    model.compile(optimizer='adam', loss='mean_squared_error')
    history = model.fit(
        X_train, y_train,
        epochs=30,
        batch_size=32,
        validation_split=0.2,
        callbacks=[early_stopping]
    )

    test_loss = model.evaluate(X_test, y_test)
    print(f"Test Loss for {model_names[i]} Model: {test_loss}")

    # Sauvegarder le modèle et l'historique d'entraînement
    model.save(f'real_estate_model_{model_names[i]}.keras')
    with open(f'model_history_{model_names[i]}.pkl', 'wb') as file:
        pickle.dump(history.history, file)
