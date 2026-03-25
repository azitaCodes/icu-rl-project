import pandas as pd
from q_learning import Q

df = pd.read_csv("data/icu_processed.csv")
df['state'] = df['state'].apply(eval)

policy = {}

for (state, action), value in Q.items():
    if state not in policy or value > Q[(state, policy[state])]:
        policy[state] = action

def doctor_policy(row):
    if row['lactate'] > 4 or row['bp'] < 70:
        return 1
    return 0

rl_score = 0
doc_score = 0

for _, row in df.iterrows():
    state = row['state']
    outcome = row['outcome']

    if state in policy:
        if policy[state] == 1 and outcome == 1:
            rl_score += 1

        if doctor_policy(row) == 1 and outcome == 1:
            doc_score += 1

print("RL score:", rl_score)
print("Doctor score:", doc_score)