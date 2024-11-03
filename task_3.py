from task_1 import G
from algorythm.dijkstra import dijkstra

edges = [
    ("Kyiv", "Lviv", 540),
    ("Kyiv", "Vinnytsia", 270),
    ("Kyiv", "Chernihiv", 140),
    ("Vinnytsia", "Ivano-Frankivsk", 370),
    ("Vinnytsia", "Lviv", 370),
    ("Lviv", "Ivano-Frankivsk", 140),
    ("Kyiv", "Poltava", 340),
    ("Poltava", "Kharkiv", 140),
    ("Odessa", "Dnipro", 530),
    ("Odessa", "Vinnytsia", 440),
    ("Dnipro", "Zaporizhzhia", 85),
    ("Dnipro", "Poltava", 215),
    ("Zaporizhzhia", "Odessa", 530),
    ("Chernihiv", "Kharkiv", 220)
]

G.add_weighted_edges_from(edges)


def dijkstra_all_shortest_paths(graph):
    paths = {}
    for start_city in graph.nodes:
        result = dijkstra(graph, start_city)
        paths[start_city] = result
    return paths


def visualize_shortest_paths(shortest_paths):
    shortest_paths = dijkstra_all_shortest_paths(G)
    print(
        f"{"City":^16}|" +
        "|".join([f"{city[:10]:^10}" for city in shortest_paths.keys()])
    )
    print(
        "-" * 16 + "+" +
        "+".join(["-" * 10 for _ in range(len(shortest_paths))])
    )
    for city, paths in shortest_paths.items():
        print(
            f"{city:<16}|" +
            "|".join([f"{length:>10}" for _, length in paths.items()])
        )


visualize_shortest_paths(dijkstra_all_shortest_paths(G))
