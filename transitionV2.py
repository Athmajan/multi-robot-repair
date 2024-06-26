import random
import numpy as np

# Given transition matrix
d_0, d_1, d_2, d_3 = 0.01, 0.02, 0.03, 0.05
damageTransition = np.array([
    [(1-d_0), d_0, 0, 0, 0],
    [0, (1-d_1), d_1, 0, 0],
    [0, 0, (1-d_2), d_2, 0],
    [0, 0, 0, (1-d_3), d_3],
    [0, 0, 0, 0, 1]
])

# Number of nodes
num_nodes = 32

# Function to initialize damage levels for each node
def initialize_damage_levels(num_nodes):
    initial_damage_levels = []
    for _ in range(num_nodes):
        # Randomly choose an initial damage level based on probabilities in the first row of damageTransition
        initial_damage_level = 0  # Starting with state 0
        rand_prob = random.random()
        cumulative_prob = 0
        for j in range(len(damageTransition[initial_damage_level])):
            cumulative_prob += damageTransition[initial_damage_level][j]
            if rand_prob < cumulative_prob:
                initial_damage_level = j
                break
        initial_damage_levels.append(initial_damage_level)
    return initial_damage_levels

# Initialize damage levels for all nodes
initial_damage_levels = initialize_damage_levels(num_nodes)

# Number of simulation steps
num_steps = 200

# Main simulation loop
current_damage_levels = initial_damage_levels.copy()
for step in range(num_steps + 1):
    print(f"Step {step}: {current_damage_levels}")
    
    # Simulate damage propagation for the next step
    new_damage_levels = []
    for i in range(num_nodes):
        current_state = current_damage_levels[i]
        # Transition to next state based on damageTransition matrix
        rand_prob = random.random()
        cumulative_prob = 0
        for j in range(len(damageTransition[current_state])):
            cumulative_prob += damageTransition[current_state][j]
            if rand_prob < cumulative_prob:
                new_damage_level = j
                break
        new_damage_levels.append(new_damage_level)
    
    # Update current damage levels
    current_damage_levels = new_damage_levels
