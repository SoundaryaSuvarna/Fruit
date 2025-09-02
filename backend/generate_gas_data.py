import pandas as pd
import random
import os

# Fruits and label-based ranges
fruit_data = {
    'apple': {
        'fresh':    {'mq135': (150, 230), 'mics5524': (100, 180)},
        'at-risk':  {'mq135': (231, 390), 'mics5524': (181, 320)},
        'spoiled':  {'mq135': (391, 650), 'mics5524': (321, 500)},
    },
    'banana': {
        'fresh':    {'mq135': (160, 240), 'mics5524': (110, 190)},
        'at-risk':  {'mq135': (241, 400), 'mics5524': (191, 340)},
        'spoiled':  {'mq135': (401, 700), 'mics5524': (341, 520)},
    },
    'orange': {
        'fresh':    {'mq135': (150, 220), 'mics5524': (100, 170)},
        'at-risk':  {'mq135': (221, 380), 'mics5524': (171, 300)},
        'spoiled':  {'mq135': (381, 620), 'mics5524': (301, 470)},
    },
    'grape': {
        'fresh':    {'mq135': (140, 210), 'mics5524': (100, 160)},
        'at-risk':  {'mq135': (211, 360), 'mics5524': (161, 280)},
        'spoiled':  {'mq135': (361, 600), 'mics5524': (281, 450)},
    }
}

# Generate data
data = []
samples_per_stage = 30  # per label per fruit

for fruit, stages in fruit_data.items():
    for label, ranges in stages.items():
        for _ in range(samples_per_stage):
            mq135 = round(random.uniform(*ranges['mq135']), 2)
            mics5524 = round(random.uniform(*ranges['mics5524']), 2)
            data.append([fruit, mq135, mics5524, label])

# Save the data
df = pd.DataFrame(data, columns=["fruit", "mq135", "mics5524", "label"])

# Ensure folder exists
save_path = "gas_dataset.csv"
df.to_csv(save_path, index=False)
print(f"✅ Realistic dataset saved to {save_path} with {len(df)} rows.")
