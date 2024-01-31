import matplotlib.pyplot as plt
import pickle

model_names = ['Original', 'Deep', 'Shallow']

# Charger l'historique d'entraînement et tracer les courbes pour chaque modèle
for name in model_names:
    with open(f'model_history_{name}.pkl', 'rb') as file:
        history = pickle.load(file)

    plt.figure(figsize=(6, 4))  # Ajusté pour n'afficher que les courbes de perte
    plt.plot(history['loss'], label='Training Loss')
    plt.plot(history['val_loss'], label='Validation Loss')
    plt.title(f'Training and Validation Loss - {name} Model')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
