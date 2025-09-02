import tensorflow as tf
import numpy as np
from PIL import Image

interpreter = tf.lite.Interpreter(model_path="models/cnn_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_image(image_path):
    img = Image.open(image_path).resize((128, 128))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])[0][0]

    return {
        "prediction": "Spoiled" if output > 0.5 else "Fresh",
        "confidence": float(output)
    }
