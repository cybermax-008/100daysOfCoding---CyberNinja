# Generating Undirected Graph using Adjacency List Representation
numOfNodes = int(input())
numOfEdges = int(input())
# create an empty dictionary (adjacency list)
graph = {}

for edge in range(numOfEdges):
    path = [int(i) for i in input().split()]
    v1,v2 = path[0],path[1]
    if v1 not in graph:
        graph[v1]=[v2]
    elif v2 not in graph[v1]:
        graph[v1].append(v2)
    if v2 not in graph:
        graph[v2]=[v1]
    elif v1 not in graph[v2]:
        graph[v2].append(v1)
print(graph)