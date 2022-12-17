import pytest

from challenge01 import Node,Edge,Graph

def test_graph_breadth_first_traversal():
    graph1 = Graph()
    a = graph1.add_node("a")
    b = graph1.add_node("b")
    c = graph1.add_node("c")
    d = graph1.add_node("d")
    e = graph1.add_node("e")
    f = graph1.add_node("f")
    g = graph1.add_node("g")


    graph1.add_edge(a, b)
    graph1.add_edge(a, c)
    graph1.add_edge(b, c)
    graph1.add_edge(c, d)
    graph1.add_edge(c, f)
    graph1.add_edge(e, f)
    graph1.add_edge(f, g)
    
    assert graph1.breadth_first_search(g) == ['g', 'f', 'c', 'e', 'a', 'b', 'd']


def test1_graph_breadth_first_traversal():
    graph1 = Graph()
    a = graph1.add_node("a")
    b = graph1.add_node("b")
    c = graph1.add_node("c")
    d = graph1.add_node("d")
    e = graph1.add_node("e")
    f = graph1.add_node("f")
    g = graph1.add_node("g")


    graph1.add_edge(a, b)
    graph1.add_edge(a, c)
    graph1.add_edge(b, c)
    graph1.add_edge(c, d)
    graph1.add_edge(c, f)
    graph1.add_edge(e, f)
    graph1.add_edge(f, g)
    
    assert graph1.breadth_first_search(b) == ['b', 'a', 'c', 'd', 'f', 'e', 'g']



def test2_graph_breadth_first_traversal():
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
    assert graph2.breadth_first_search(c)==[3, 1, 5, 7, 2, 6, 4]


