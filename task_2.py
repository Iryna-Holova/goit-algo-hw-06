from algorythm.dfs import dfs
from algorythm.bfs import bfs
from task_1 import G


def task_2():
    print("DFS execution:")
    dfs(G, "Kyiv")

    print("\nBFS execution:")
    bfs(G, "Kyiv")


task_2()
