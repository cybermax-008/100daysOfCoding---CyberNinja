from collections import defaultdict
num_nodes = int(input("no of nodes"))
num_edges = int(input("no of edges:"))

graph = {}
for i in range(num_edges):
    nodes = [i for i in input().split()]
    if nodes[0] not in graph:
        graph[nodes[0]] =[ nodes[1]]
    elif nodes[1] not in graph[nodes[0]]:
        graph[nodes[0]].append(nodes[1])
    if nodes[1] not in graph:
        graph[nodes[1]] = [nodes[0]]
    elif nodes[0] not in graph[nodes[1]]:
        graph[nodes[1]].append(nodes[0])
print(graph)
