import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Step 7: Building and Training the TensorFlow Model
# This step consists of building and training your TensorFlow model. You will use the Sequential API to create a dense neural network.

# Charger les ensembles de données
X_train = pd.read_csv("X_train.csv").astype('float32')
X_test = pd.read_csv("X_test.csv").astype('float32')
y_train = pd.read_csv("y_train.csv")['price'].astype('float32')
y_test = pd.read_csv("y_test.csv")['price'].astype('float32')

# Construction du modèle
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dense(1)  # Couche de sortie pour la prédiction
])

# Compilation du modèle
model.compile(optimizer='adam', loss='mean_squared_error')

# Callback pour l'arrêt précoce
early_stopping = EarlyStopping(monitor='val_loss', patience=5)


# Entraînement du modèle
history = model.fit(
    X_train, y_train,
    epochs=30,  # Nombre d'époques
    batch_size=32,  # Taille du batch
    validation_split=0.2,  # Pourcentage de données utilisé pour la validation
    callbacks=[early_stopping]
)

# Évaluation du modèle
test_loss = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss}")

# Sauvegarder le modèle
model.save('real_estate_model.keras')

# Vous pouvez également choisir de sauvegarder l'historique de l'entraînement pour une analyse ultérieure
import pickle
with open('model_history.pkl', 'wb') as file:
    pickle.dump(history.history, file)



# Explanations:
# Data Loading: Training and test sets are loaded from CSV files.
# Model Building: The model is built using the Sequential API. It includes Dense layers with relu activation and a Dropout layer to reduce the risk of overfitting.
# Model Compilation: The model is compiled with the 'adam' optimizer and the 'mean_squared_error' loss function, which is appropriate for a regression task.
# Model Training: The model is trained using an EarlyStopping callback to stop training if performance on the validation set does not improve after a certain number of epochs.
# Evaluation and Saving: The model is evaluated on the test set, and the model is saved for future use.