# Write here the code challenge solution

class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight



from collections import deque

class Graph:
    def __init__(self):
        # initialize the graph with an empty dictionary
        self.graph = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.graph[new_vertex] = []
        return new_vertex
    
    def add_edge(self,node1,node2,weight=0):
        
        if not node1 in self.graph.keys():
            return("this node does not exist")

        if not node2 in self.graph.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.graph[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.graph[node2].append(edge2)
    
    def breadth_first_search(self, value1):
        visited = []
        queue = [value1]
        while queue:
            current_node = queue.pop(0)
            if current_node.value not in visited:
                visited.append(current_node.value)
                for edge in self.graph[current_node]:
                    queue.append(edge.vertex)
        return visited




if __name__ == "__main__":
    graph2=Graph()
    a=graph2.add_node(1)
    b=graph2.add_node(2)
    c=graph2.add_node(3)
    d=graph2.add_node(4)
    e=graph2.add_node(5)
    f=graph2.add_node(6)
    g=graph2.add_node(7)

    
    graph2.add_edge(a,b)
    graph2.add_edge(a,c)
    graph2.add_edge(c,e)
    graph2.add_edge(b,d)
    graph2.add_edge(b,f)
    
    graph2.add_edge(e,f)
    
    graph2.add_edge(c,g)

    print(graph2.breadth_first_search(c))

    
