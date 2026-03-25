import pandas as pd

df = pd.read_csv("data/icu_simulated.csv")

df['apache_bin'] = pd.cut(df['apache'], bins=3, labels=[0,1,2])
df['lactate_bin'] = pd.cut(df['lactate'], bins=3, labels=[0,1,2])
df['bp_bin'] = pd.cut(df['bp'], bins=3, labels=[0,1,2])

df['state'] = list(zip(df['apache_bin'], df['lactate_bin'], df['bp_bin']))

df.to_csv("data/icu_processed.csv", index=False)

print("✅ Preprocessing done!")