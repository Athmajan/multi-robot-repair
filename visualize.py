import networkx as nx
import matplotlib.pyplot as plt
import random

def visualize_graph(damage_levels, edges, coordinates):
    # Number of nodes
    num_nodes = 32

    # Create an undirected graph
    G = nx.Graph()
    G.add_nodes_from(range(1, num_nodes + 1))

    # Add the predefined edges to the graph
    G.add_edges_from(edges)

    # Create a dictionary for the node positions
    pos = {i+1: coordinates[i] for i in range(num_nodes)}

    # Draw the nodes with grey squares
    nx.draw_networkx_nodes(G, pos, node_shape='s', node_color='grey', node_size=500)

    # Draw the edges
    nx.draw_networkx_edges(G, pos)

    # Create labels with both node ID and damage level
    damage_labels = {i+1: f"{damage_levels[i]}" for i in range(num_nodes)}
    node_labels = {i+1: f"{i+1}" for i in range(num_nodes)}

    # Draw the damage levels inside the nodes
    nx.draw_networkx_labels(G, pos, labels=damage_labels, font_size=12, font_color='black')

    # Offset for node IDs to avoid overlap with damage levels
    pos_higher = {node: (x, y + 0.04) for node, (x, y) in pos.items()}
    nx.draw_networkx_labels(G, pos_higher, labels=node_labels, font_size=10, font_color='red')

    # Remove the axis
    plt.axis('off')
    
    # Display the graph
    plt.show()

# Example damage levels for the 32 nodes (randomly assigned for demonstration)
damage_levels = [random.randint(0, 4) for _ in range(32)]

# Example list of edges (adjust this list as needed)
edges = [
    (1, 2), (1, 32), (2, 3), (2, 4), (3, 4), (3, 32),
    (4, 5), (4, 6), (5, 6), (5, 8), (6, 7), (6, 32),
    (7, 17), (8, 9), (8, 12), (9, 10), (9, 12), (10, 11),
    (11, 12), (11, 13), (12, 14), (13, 15), (14, 24), (14, 15),
    (15, 16), (16, 17), (16, 19), (16, 20), (17, 19), (17, 18),
    (18, 21), (18, 22), (18, 23), (19, 21), (20, 21), (21, 22),
    (23, 25), (23, 26), (24, 25), (25, 26), (26,28),(25, 27), (27, 28),
    (27, 29), (27, 30), (28, 29), (29, 30), (30, 31), (31, 32)
]

# Coordinates for the nodes
coordinates = [
    (-3.5, 2.5), (-3, 3), (-2.8, 2.5), (-1.8, 2.6), (-0.5, 2.5),
    (-1.4, 1.8), (0, 0), (1.2, 2.5), (2.5, 2.8), (3.8, 3),
    (3.8, 2), (2.2, 2), (4, 1), (1.8, 0.5), (3.1, 0),
    (3, -1), (1.2, -1), (1.1, -2.2), (2.5, -1.6), (3.5, -2),
    (2.5, -2.5), (2, -3), (-0.4, -2.5), (0.2, -0.5), (-1.1, -1.8),
    (-1.8, -2.5), (-3, -1.6), (-3, -2.5), (-3.8, -1.8), (-3.8, -0.9), (-3.8, 0.5),
    (-3, 1.8)  # Coordinate for the 32nd node
]

# Visualize the graph with the given damage levels, predefined edges, and specific coordinates
visualize_graph(damage_levels, edges, coordinates)
