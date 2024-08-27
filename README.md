# Reinforcement Learning for Autonomous Racing

## Project Overview

This project aims to develop and optimize a reinforcement learning-based reward function for training an autonomous racing agent. The goal is to ensure the agent stays on the track, avoids zig-zag behaviors, and maintains an optimal speed and steering angle. By refining these reward functions, the agent will be able to navigate complex tracks efficiently and safely.

## Project Files

### 1. `modelCenterLine.py`
**General Aim:**  
This script implements a basic reward function that encourages the agent to stay on track by rewarding it for staying close to the center line and penalizing it for moving too slowly. The function also adds a minor bonus for maintaining a low steering angle, which helps in reducing excessive steering.

**Specific Features:**
- Rewards staying near the center line.
- Penalizes low speed.
- Encourages minimal steering angle.

### 2. `modelPreventZigZag.py`
**General Aim:**  
This version of the reward function is designed to prevent zig-zag behavior by penalizing excessive steering. It also incorporates a system of markers that provide different reward levels based on the agent's distance from the center line. This function additionally penalizes the agent for going off track.

**Specific Features:**
- Penalizes excessive steering to avoid zig-zagging.
- Provides rewards based on the distance from the center line.
- Penalizes the agent if it goes off track.

### 3. `modelWithinTrack.py`
**General Aim:**  
This function builds on the previous versions by rewarding the agent for maintaining all wheels on the track and staying between the track borders. It also introduces a reward that scales with the square of the agent's speed, promoting faster and more efficient driving.

**Specific Features:**
- Rewards keeping all wheels on the track.
- Adds rewards for maintaining a low steering angle.
- Promotes high-speed driving through quadratic speed rewards.

## Big Goal of the Project

The overarching goal of this project is to create a highly effective and adaptable reinforcement learning reward function for autonomous racing. By iteratively refining the reward mechanisms, the project seeks to train an agent that can efficiently navigate complex tracks, maintain optimal speed, and make precise steering decisions, ultimately contributing to advancements in autonomous vehicle technology.

## How to Use

1. Clone the repository.
2. Select one of the reward functions (e.g., `modelCenterLine.py`, `modelPreventZigZag.py`, `modelWithinTrack.py`).
3. Integrate the selected reward function into your reinforcement learning training environment.
4. Train your autonomous racing agent using the chosen reward function.
5. Evaluate and compare the performance of the agent under different reward functions to determine the most effective one.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
