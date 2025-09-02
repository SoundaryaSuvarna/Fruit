import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore

img_size = (128, 128)
train_dir = "../dataset"

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train = datagen.flow_from_directory(train_dir, target_size=img_size, subset='training', class_mode='binary')
val = datagen.flow_from_directory(train_dir, target_size=img_size, subset='validation', class_mode='binary')

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train, validation_data=val, epochs=5)

# Save as .tflite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open('models/cnn_model.tflite', 'wb') as f:
    f.write(tflite_model)

print("✅ CNN model saved as TFLite.")
