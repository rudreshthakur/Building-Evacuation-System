import networkx as nx
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1 + STEP 2
# CREATE BUILDING GRAPH
# -------------------------------

# Create empty graph
G = nx.Graph()

# Add connections between locations
G.add_edge("Room101", "Hallway", weight=2)

G.add_edge("Room102", "Hallway", weight=2)

G.add_edge("Hallway", "CorridorB", weight=3)

G.add_edge("CorridorB", "Room103", weight=2)

G.add_edge("Hallway", "Staircase", weight=4)

G.add_edge("Staircase", "ExitA", weight=2)

G.add_edge("Room104", "CorridorB", weight=2)

G.add_edge("Room105", "Hallway", weight=3)

# Print all nodes
print("Nodes in Building:")
print(G.nodes())

# Print all edges
print("\nConnections:")
print(G.edges(data=True))

# -------------------------------
# STEP 3
# USER INPUT
# -------------------------------

# Exit nodes
exits = ["ExitA"]

# Take current location from user
current_location = input("\nEnter your current location: ")

# Take blocked/fire location
blocked_location = input("Enter fire/blocked location: ")

# Display user input
print("\nCurrent Location:", current_location)

print("Blocked Location:", blocked_location)

# -------------------------------
# STEP 4
# REMOVE BLOCKED NODE
# -------------------------------

# Create copy of graph
safe_graph = G.copy()

# Remove blocked/fire node
if blocked_location in safe_graph:

    safe_graph.remove_node(blocked_location)

    print("\nBlocked node removed from graph!")

else:
    print("\nBlocked location not found in building!")

# -------------------------------
# STEP 5
# DIJKSTRA SHORTEST SAFE PATH
# -------------------------------

# Variables to store shortest path
shortest_path = None

shortest_distance = float('inf')

# Check path to every exit
for exit_node in exits:

    try:
        # Find shortest path
        path = nx.dijkstra_path(
            safe_graph,
            current_location,
            exit_node,
            weight='weight'
        )

        # Find total distance
        distance = nx.dijkstra_path_length(
            safe_graph,
            current_location,
            exit_node,
            weight='weight'
        )

        # Store minimum distance path
        if distance < shortest_distance:

            shortest_distance = distance

            shortest_path = path

    except:
        print(f"No safe path to {exit_node}")



        # -------------------------------
# STEP 6
# DISPLAY FINAL RESULT
# -------------------------------

print("\n--- EVACUATION RESULT ---")

print("Current Location:", current_location)

print("Blocked Location:", blocked_location)

# If path exists
if shortest_path:

    print("\nSafe Route:")

    print(" -> ".join(shortest_path))

    print("\nTotal Distance:", shortest_distance, "units")

else:

    print("\nNo safe evacuation route found!")



    # -------------------------------
# STEP 7
# GRAPH VISUALIZATION
# -------------------------------

# Generate graph layout
pos = nx.spring_layout(G)

# Store colors for nodes
node_colors = []

# Decide color of each node
for node in G.nodes():

    # Fire node = Red
    if node == blocked_location:

        node_colors.append("red")

    # Exit node = Green
    elif node in exits:

        node_colors.append("green")

    # Safe path = Blue
    elif shortest_path and node in shortest_path:

        node_colors.append("blue")

    # Normal nodes = Light gray
    else:

        node_colors.append("lightgray")

# Create graph window
plt.figure(figsize=(10, 7))

# Draw graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2500,
    font_size=10
)

# Show edge weights
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels
)

# Title
plt.title("Building Evacuation System")

# Display graph
plt.show()