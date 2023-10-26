import tensorflow as tf
import matplotlib.pyplot as plt

# Charger les données MNIST
(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = tf.keras.datasets.mnist.load_data()

# Vérifier la forme des données
print("Forme des images d'entraînement:", mnist_train_images.shape)
print("Forme des étiquettes d'entraînement:", mnist_train_labels.shape)
print("Forme des images de test:", mnist_test_images.shape)
print("Forme des étiquettes de test:", mnist_test_labels.shape)


# Afficher les 5 premières images du jeu de données d'entraînement
for i in range(5):
    plt.imshow(mnist_train_images[i], cmap='gray')
    plt.title(f"Étiquette: {mnist_train_labels[i]}")
    plt.show()

# Normalisation des images
mnist_train_images = mnist_train_images / 255.0
mnist_test_images = mnist_test_images / 255.0

# Encodage one-hot des étiquettes
mnist_train_labels = tf.keras.utils.to_categorical(mnist_train_labels, 10)
mnist_test_labels = tf.keras.utils.to_categorical(mnist_test_labels, 10)

# Création du modèle
model = tf.keras.models.Sequential([
    # Redimensionnement des images pour les adapter à un CNN
    tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
    
    # Première couche convolutive
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    
    # Deuxième couche convolutive
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    # Aplatir les résultats pour les adapter à une couche DNN
    tf.keras.layers.Flatten(),
    
    # Couche dense de 128 neurones
    tf.keras.layers.Dense(128, activation='relu'),
    
    # Couche de sortie avec 10 neurones (pour 10 classes) avec activation softmax
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Affichage du résumé du modèle
model.summary()

# Entraînement du modèle
history = model.fit(
    mnist_train_images,
    mnist_train_labels,
    epochs=10,  # Nombre de fois où le modèle verra l'ensemble des données d'entraînement
    validation_data=(mnist_test_images, mnist_test_labels)  # Pour évaluer les performances du modèle sur les données de test après chaque époque
)

# Affichage de l'historique de l'entraînement (précision et perte)
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Précision (entraînement)')
plt.plot(history.history['val_accuracy'], label='Précision (validation)')
plt.title('Précision')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perte (entraînement)')
plt.plot(history.history['val_loss'], label='Perte (validation)')
plt.title('Perte')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()

plt.tight_layout()
plt.show()

# Sauvegarder le modèle
model.save('mnist_model.h5')
