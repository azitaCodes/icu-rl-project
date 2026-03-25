import pandas as pd
import numpy as np

np.random.seed(42)

n_patients = 300
timesteps = 6

data = []

for pid in range(n_patients):
    for t in range(timesteps):
        
        apache = np.random.randint(10, 40)
        lactate = np.random.uniform(1, 6)
        bp = np.random.uniform(60, 120)

        # realistic survival
        if apache > 30 or lactate > 4:
            survival = np.random.choice([0,1], p=[0.7, 0.3])
        else:
            survival = np.random.choice([0,1], p=[0.2, 0.8])

        # doctor-like decision
        if lactate > 4 or bp < 70:
            action = 1
        else:
            action = np.random.choice([0,1], p=[0.7, 0.3])

        data.append({
            "patient_id": pid,
            "time": t,
            "apache": apache,
            "lactate": lactate,
            "bp": bp,
            "action": action,
            "outcome": survival
        })

df = pd.DataFrame(data)

df.to_csv("data/icu_simulated.csv", index=False)

print("✅ Simulated dataset created!")