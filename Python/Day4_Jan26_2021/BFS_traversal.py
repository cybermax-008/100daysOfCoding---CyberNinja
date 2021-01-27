# Generating Undirected Graph using Adjacency List Representation
numOfNodes = int(input())
numOfEdges = int(input())
# create an empty dictionary (adjacency list)
graph = {}

for edge in range(numOfEdges):
    path = [i for i in input().split()]
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

def BFS(G, s):
    # nodes that are visited 
    visited = []
    # initialize Queue to keep nodes that are to be checked
    queue = []

    # Mark the source node
    visited.append(s)
    # add the source node to queue
    queue.append(s)

    while queue:
        current_node = queue.pop(0)
        print(current_node,end=' ')
        # explore the neighbours of current node
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
BFS(graph,'A')