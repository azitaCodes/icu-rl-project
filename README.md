# ICU Reinforcement Learning Project

## Overview
This project applies Reinforcement Learning (Q-learning and Deep Q-Network) to optimize treatment decisions in ICU settings using simulated patient data.

## Key Features
- Simulated ICU dataset with realistic clinical patterns
- State modeling using patient vitals (APACHE, lactate, BP)
- Q-learning implementation
- Deep Q-Network (DQN)
- Comparison against rule-based clinical policy

## Results
The RL model outperformed a baseline clinical decision rule:

- RL Score: 400
- Doctor Baseline Score: 323

## Tech Stack
- Python
- Pandas, NumPy
- PyTorch
- Reinforcement Learning

## Project Structure
- data/ → dataset
- src/ → code
- run.py → pipeline runner

## Future Work
- Apply to real ICU dataset (MIMIC-IV)
- Improve reward function
- Add advanced RL (Double DQN, PPO)