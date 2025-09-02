import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('gas_dataset.csv')
X = df[['mq135', 'mics5524']]  # fruit name excluded for model input
y = df['label']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

with open('models/gas_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Random Forest model saved.")