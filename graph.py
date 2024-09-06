class Graph:

    def __init__(self):
        self.numberOfNodes = 0
        self.adjacencyList={}

    def insert_node(self,node):
        if node not in self.adjacencyList:
            self.adjacencyList[node] = []
            self.numberOfNodes += 1
            return

    def insert_edge(self,vertex1, vertex2):
        if vertex2 not in self.adjacencyList[vertex1]:
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
            return
        else:
            return "edge already exists"

    def show_graph(self):
        for node in self.adjacencyList:
            print(f'{node} --> {" ".join(map(str, self.adjacencyList[node]))}')


myGraph = Graph()
myGraph.insert_node(1)
myGraph.insert_node(2)
myGraph.insert_node(3)
myGraph.insert_node(4)
myGraph.insert_edge(1,2)
myGraph.insert_edge(2,3)
myGraph.insert_edge(2,4)
myGraph.show_graph()
