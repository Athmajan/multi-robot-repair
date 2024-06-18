import os
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import yaml
import numpy as np

class Node:
    def __init__(self, node_id, coordinates, neighbors=None, probability_distribution=None,maxDamageLevel=4):
        self.node_id = node_id
        self.coordinates = coordinates
        self.neighbors = neighbors if neighbors is not None else []
        self.damageLevels = maxDamageLevel+1
        #self.probability_distribution = probability_distribution if probability_distribution is not None else []
        self.damageDistribution = probability_distribution \
            if probability_distribution is not None \
            else np.zeros([self.damageLevels,self.damageLevels])

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"Node({self.node_id})"

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def visualize_graph(nodes):
    G = nx.Graph()

    # Add nodes with their coordinates
    pos = {node.node_id: node.coordinates for node in nodes}
    G.add_nodes_from(pos.keys())

    # Add edges based on neighbors
    for node in nodes:
        for neighbor in node.neighbors:
            G.add_edge(node.node_id, neighbor.node_id)
    
    plt.figure(figsize=(19.2, 10.8))
    
    # Draw the nodes with grey squares
    nx.draw_networkx_nodes(G, pos, node_shape='s', node_color='grey', node_size=2000)

    # Draw the edges
    nx.draw_networkx_edges(G, pos)

    # Create labels with node ID
    # Modify node_labels to use the keys from the coordinates dictionary
    node_labels = {node.node_id: str(node.node_id) for node in nodes}

    # Draw the node IDs inside the nodes
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black')

    # Remove the axis
    plt.axis('off')
    
    # Display the graph
    plt.show()


def initGraphNetwork(config):
        
    #config = load_config('config.yml')
    edges = config["node"]["edges"]
    coordinates = config["node"]["coordinates"]

    icon0 = config["icons"][0]
    icon1 = config["icons"][1]
    icon2 = config["icons"][2]
    icon3 = config["icons"][3]
    icon4 = config["icons"][4]

    nodeCount = len(coordinates)
    damageProbs = config["markov_chain"]["damages"]
    [d_0, d_1, d_2, d_3] = damageProbs

    # Construct damageTransition matrix
    damageTransition = [
        [(1 - d_0), d_0, 0, 0, 0],
        [0, (1 - d_1), d_1, 0, 0],
        [0, 0, (1 - d_2), d_2, 0],
        [0, 0, 0, (1 - d_3), d_3],
        [0, 0, 0, 0, 1]
    ]

    # Create nodes
    nodes = [Node(node_id=i+1, coordinates=coordinates[i+1], probability_distribution=damageTransition) for i in range(nodeCount)]

    # Add neighbors to nodes
    node_dict = {node.node_id: node for node in nodes}
    for edge in edges:
        node_dict[edge[0]].add_neighbor(node_dict[edge[1]])
        node_dict[edge[1]].add_neighbor(node_dict[edge[0]])

    return nodes

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

def nextDamageLevel(current_damage_levels):
    # Simulate damage propagation for the next step
    new_damage_levels = []
    for i in range(nodesN):
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
    
    return current_damage_levels


if __name__ == "__main__":
    #seed_value = 30 
    
    # Initiate Graph Network
    config  = load_config('config.yml')
    damageProbs = config["markov_chain"]["damages"]
    nodesN = len(config["node"]["coordinates"])
    steps = config["simu_n"]
    
    [d_0, d_1, d_2, d_3] = damageProbs

    # Construct damageTransition matrix
    damageTransition = [
        [(1 - d_0), d_0, 0, 0, 0],
        [0, (1 - d_1), d_1, 0, 0],
        [0, 0, (1 - d_2), d_2, 0],
        [0, 0, 0, (1 - d_3), d_3],
        [0, 0, 0, 0, 1]
    ]
    

    nodes = initGraphNetwork(config)


    #initialize random damages
    initDamageLevels = initialize_damage_levels(nodesN)

    

    current_damage_levels = initDamageLevels.copy()
    for step in range(steps):
       current_damage_levels = nextDamageLevel(current_damage_levels)
       print(f"Step {step}: {current_damage_levels}")
       
        #visualize_graph(nodes)

       



