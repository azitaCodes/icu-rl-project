import pandas as pd

df = pd.read_csv("data/icu_processed.csv")
df['state'] = df['state'].apply(eval)

trajectories = []

for pid, group in df.groupby('patient_id'):
    group = group.sort_values('time')

    states = group['state'].tolist()
    actions = group['action'].tolist()
    rewards = group['outcome'].tolist()

    trajectories.append((states, actions, rewards))

Q = {}

def get_Q(state, action):
    return Q.get((state, action), 0.0)

alpha = 0.1
gamma = 0.9

for states, actions, rewards in trajectories:
    for t in range(len(states)-1):
        s = states[t]
        a = actions[t]
        r = rewards[t]
        s_next = states[t+1]

        max_Q_next = max([get_Q(s_next, a2) for a2 in [0,1]])

        Q[(s,a)] = get_Q(s,a) + alpha * (r + gamma * max_Q_next - get_Q(s,a))

print("✅ Q-learning training complete!")