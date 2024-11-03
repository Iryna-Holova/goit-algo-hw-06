import networkx as nx
import matplotlib.pyplot as plt

cities = {
    "Kyiv": (30.5233, 50.4500),
    "Lviv": (24.0167, 49.8333),
    "Odessa": (30.5167, 46.4833),
    "Kharkiv": (36.2500, 49.9833),
    "Dnipro": (35.0000, 48.5000),
    "Zaporizhzhia": (35.1667, 47.8333),
    "Ivano-Frankivsk": (24.7167, 48.9167),
    "Chernihiv": (31.3000, 51.5000),
    "Poltava": (34.6833, 49.5833),
    "Vinnytsia": (28.6667, 49.1667),
}

edges = [
    ("Kyiv", "Lviv"), ("Kyiv", "Vinnytsia"), ("Kyiv", "Chernihiv"),
    ("Vinnytsia", "Ivano-Frankivsk"), ("Vinnytsia", "Lviv"),
    ("Lviv", "Ivano-Frankivsk"), ("Kyiv", "Poltava"), ("Poltava", "Kharkiv"),
    ("Odessa", "Dnipro"), ("Odessa", "Vinnytsia"), ("Dnipro", "Zaporizhzhia"),
    ("Dnipro", "Poltava"), ("Zaporizhzhia", "Odessa"),
    ("Chernihiv", "Kharkiv"),
]

# Initialize graph
G = nx.Graph()

# Add nodes for each city
G.add_nodes_from(cities.keys())

# Add edges (connections between cities)
G.add_edges_from(edges)


def visualize_graph():
    plt.figure(figsize=(10, 7))
    nx.draw(
        G,
        pos=cities,
        with_labels=True,
        node_color='skyblue',
        edge_color='gray',
        node_size=2000,
        font_size=10,
    )
    plt.show()

    # Analyze basic characteristics
    print("Number of nodes (cities):", G.number_of_nodes())
    print("Number of edges (connections):", G.number_of_edges())
    print("Degree of each node (city):", dict(G.degree()))


if __name__ == "__main__":
    visualize_graph()
