n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

adjacencyList = {}
for i in range(len(edges)):
    adjacencyList[edges[i][0]] = []

for edge in edges:
    adjacencyList[edge[0]].append(edge[1])
    adjacencyList[edge[1]].append(edge[0])


if destination in adjacencyList[source] or source in adjacencyList[destination]:
    print(True)
else:
    print(False)

print(adjacencyList)