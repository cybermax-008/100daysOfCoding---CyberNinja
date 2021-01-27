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
    else:
        graph[v1].append(v2)
print(graph)

