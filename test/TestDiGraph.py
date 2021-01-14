from unittest import TestCase
from src.DiGraph import DiGraph


def graph_creator(v, e: int = 0) -> DiGraph:
    g = DiGraph()
    for n in range(v):
        g.add_node(n)

    for i in range(0, v):
        for j in range(1, v):
            if g.e_size() < e:
                g.add_edge(i, j, 10)

        if g.e_size() >= e:
            break

    return g


class TestDiGraph(TestCase):

    def test_add_node(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        print(g.getNode(5))

        g = DiGraph()
        self.assertEqual(g.v_size(), 0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(10)
        self.assertFalse(g.add_node(10))
        self.assertEqual(g.v_size(), 3)

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

        g = DiGraph()
        self.assertFalse(g.remove_node(5))
        g = graph_creator(10, 0)
        self.assertEqual(g.get_mc(), 10)
        g.add_edge(1, 2, 5)
        g.add_edge(1, 3, 5)
        g.add_edge(1, 4, 5)
        g.add_edge(1, 5, 5)
        self.assertEqual(g.get_mc(), 14)
        self.assertTrue(g.remove_node(1))
        self.assertEqual(g.get_mc(), 15)

    def test_add_edge(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        g.add_edge(1, 2, 6)
        g.add_edge(1, 3, 7)
        print(g.neighborsIn)
        print(g.neighborsOut)

        g = DiGraph()
        g.add_edge(0, 1, 1.33)
        self.assertEqual(g.e_size(), 0)
        g.add_node(0)
        g.add_node(1, (1, 2, 0))
        g.add_edge(0, 1, 12)
        g.add_edge(0, 1, 12)
        g.add_edge(1, 0, 12)
        g.add_edge(1, 20, 12)
        self.assertEqual(g.e_size(), 2)

    def test_remove_edge(self):
        g = graph_creator(5)
        self.assertEqual(g.get_mc(), 5)
        g.add_edge(1, 2, 32)
        g.add_edge(2, 3, 32)
        g.add_edge(3, 4, 32)
        self.assertEqual(g.e_size(), 3)
        self.assertEqual(g.get_mc(), 8)
        g.remove_edge(3, 4)
        g.remove_edge(3, 4)
        g.remove_edge(3, 20)
        self.assertEqual(g.e_size(), 2)
        self.assertEqual(g.get_mc(), 9)

    def test_get_all_v(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        print(g.get_all_v())

        g = graph_creator(10)
        self.assertEqual(len(g.get_all_v()), 10)

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        g.add_edge(2, 1, 6)
        g.add_edge(1, 3, 7)
        print(g.all_in_edges_of_node(1))

        g = graph_creator(10)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 1)
        g.add_edge(1, 4, 1)
        g.add_edge(1, 5, 1)
        g.add_edge(1, 5, 1)
        self.assertEqual(len(g.all_in_edges_of_node(1)), 0)

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(node_id=1)
        g.add_node(node_id=2)
        g.add_node(node_id=3)
        g.add_edge(1, 2, 6)
        g.add_edge(1, 3, 7)
        print(g.all_out_edges_of_node(1))

        g = graph_creator(10)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 1)
        g.add_edge(1, 4, 1)
        g.add_edge(1, 5, 1)
        g.add_edge(1, 5, 1)
        self.assertEqual(len(g.all_out_edges_of_node(1)), 4)

    def test_v_size(self):
        g = DiGraph()
        g.add_node(node_id=1)
        print(g.v_size())

    def test_e_size(self):
        g = DiGraph()
        g.add_node(node_id=1)
        print(g.get_mc())
        g.add_node(node_id=2)
        print(g.e_size())
        print(g.get_mc())
        g.add_edge(id1=1, id2=2, weight=4)
        print(g.e_size())
        print(g.get_mc())

    def test_100_vertices(self):
        g = graph_creator(100, 100)
        self.assertEqual(g.v_size(), 100)

    def test_10000_vertices(self):
        g = graph_creator(10000, 10000)
        self.assertEqual(g.v_size(), 10000)

    def test_1000000_vertices(self):
        g = graph_creator(1000000, 1000000)
        self.assertEqual(g.v_size(), 1000000)

    def test_10000000_vertices(self):
        g = graph_creator(1000000, 10000000)
        self.assertEqual(g.v_size(), 1000000)
