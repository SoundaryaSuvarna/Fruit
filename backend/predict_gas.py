import pickle
import numpy as np

with open('models/gas_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_gas(mq135: float, mics5524: float, fruit: str):
    input_data = np.array([[mq135, mics5524]])
    prediction = model.predict(input_data)[0]
    return {
        "fruit": fruit,
        "mq135": mq135,
        "mics5524": mics5524,
        "status": "Spoiled" if prediction == 1 else "Fresh"
    }
