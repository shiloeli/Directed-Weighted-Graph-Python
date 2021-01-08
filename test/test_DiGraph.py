from unittest import TestCase
from Ex3.src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def test_v_size(self):
        g = DiGraph()
        g.add_node(node_id=1)
        print(g.v_size())

    def test_e_size(self):
        g = DiGraph()
        g.add_node(node_id=1)
        print(g.MC)
        g.add_node(node_id=2)
        print(g.e_size())
        print(g.MC)
        g.add_edge(id1=1, id2=2, weight=4)
        print(g.e_size())
        print(g.MC)

    def test_get_all_v(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        print(g.get_all_v())

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        g.add_edge(2, 1, 6)
        g.add_edge(1, 3, 7)
        print(g.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        g.add_edge(1, 2, 6)
        g.add_edge(1, 3, 7)
        print(g.all_out_edges_of_node(1))

    def test_get_mc(self):
        self.fail()

    def test_get_edge(self):
        self.fail()

    def test_add_edge(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        g.add_edge(1, 2, 6)
        g.add_edge(1, 3, 7)
        print(g.neighborsIn)
        print(g.neighborsOut)

    def test_add_node(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        print(g.getNode(5))

    def test_get_node(self):
        self.fail()

    def test_remove_node(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        g.add_edge(1, 2, 7)
        g.add_edge(1, 3, 7)
        g.add_edge(3, 1, 7)
        g.add_edge(2, 1, 7)
        print(g.e_size())
        g.remove_node(1)
        print(g.e_size())
