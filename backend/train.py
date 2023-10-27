import matplotlib.pyplot as plt
import tensorflow as tf

# Charger les données MNIST
(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = tf.keras.datasets.mnist.load_data()

# Normalisation des images
mnist_train_images = mnist_train_images / 255.0
mnist_test_images = mnist_test_images / 255.0

# Encodage one-hot des étiquettes
mnist_train_labels = tf.keras.utils.to_categorical(mnist_train_labels, 10)
mnist_test_labels = tf.keras.utils.to_categorical(mnist_test_labels, 10)

# Augmentation des données
datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.5,  # Permet des décalages allant jusqu'à 50% de la largeur de l'image
    height_shift_range=0.5  # Permet des décalages allant jusqu'à 50% de la hauteur de l'image
)
datagen.fit(mnist_train_images.reshape(-1, 28, 28, 1))

# Création du modèle
model = tf.keras.models.Sequential([
    tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dropout(0.6),
    tf.keras.layers.Dense(10, activation="softmax"),
])

# Compilation du modèle avec un taux d'apprentissage ajusté
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])

# Entraînement du modèle avec augmentation des données
history = model.fit(
    datagen.flow(mnist_train_images.reshape(-1, 28, 28, 1), mnist_train_labels, batch_size=32),
    epochs=25,
    validation_data=(mnist_test_images.reshape(-1, 28, 28, 1), mnist_test_labels)
)

# Affichage de l'historique de l'entraînement
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Précision (entraînement)")
plt.plot(history.history["val_accuracy"], label="Précision (validation)")
plt.title("Précision")
plt.xlabel("Époque")
plt.ylabel("Précision")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Perte (entraînement)")
plt.plot(history.history["val_loss"], label="Perte (validation)")
plt.title("Perte")
plt.xlabel("Époque")
plt.ylabel("Perte")
plt.legend()

plt.tight_layout()
plt.show()

# Sauvegarder le modèle
model.save("models/mnist_model.keras")
