import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd

df = pd.read_csv("data/icu_processed.csv")
df['state'] = df['state'].apply(eval)

def state_to_tensor(state):
    return torch.tensor(list(state), dtype=torch.float32)

class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 64),
            nn.ReLU(),
            nn.Linear(64, 2)
        )

    def forward(self, x):
        return self.net(x)

model = DQN()
optimizer = optim.Adam(model.parameters(), lr=0.001)

gamma = 0.9

for pid, group in df.groupby('patient_id'):
    group = group.sort_values('time')

    states = group['state'].tolist()
    actions = group['action'].tolist()
    rewards = group['outcome'].tolist()

    for t in range(len(states)-1):
        s = state_to_tensor(states[t])
        s_next = state_to_tensor(states[t+1])
        r = rewards[t]
        a = actions[t]

        q_values = model(s)
        q_next = model(s_next).max()

        target = r + gamma * q_next

        loss = (q_values[a] - target.detach())**2

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

print("✅ DQN training complete!")