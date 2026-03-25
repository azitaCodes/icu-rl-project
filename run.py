import os

os.system("python src/simulate_data.py")
os.system("python src/preprocess.py")
os.system("python src/q_learning.py")
os.system("python src/dqn.py")
os.system("python src/evaluate.py")