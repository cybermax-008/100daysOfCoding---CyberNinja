# Generating Undirected Graph using Adjacency List Representation
numOfNodes = int(input())
numOfEdges = int(input())
# create an empty dictionary (adjacency list)
graph = {}
# loading the paths available in the graph
for edge in range(numOfEdges):
    path = [int(i) for i in input().split()]
    v1,v2 = path[0],path[1]
    if v1 not in graph:
        graph[v1]=[v2]
    else:
        graph[v1].append(v2)

# Get the path query to be checked
print(graph)
check_path = [int(i) for i in input().split()]
if check_path[1] in graph[check_path[0]]:
    print("This path exists in the graph!")
else:
    print("This path does not exist in the graph!")
