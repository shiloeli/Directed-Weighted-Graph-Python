import math
import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def graph_creator(v, e) -> DiGraph:
    g = DiGraph()
    for n in range(v):
        g.add_node(n)

    for i in range(0, v):
        for j in range(1, v):
            # if (g.edgeSize() < e_size) {
            if g.e_size() < e:
                g.add_edge(i, j, 10)

        if g.e_size() >= e:
            break

    return g


def test_graph_loaded(graph: str) -> None:
    g_algo = GraphAlgo()
    file = "../data/" + graph
    g_algo.load_from_json(file)
    print(g_algo.get_graph())
    g_algo.save_to_json(file + "_edited")
    for k in g_algo.get_graph().get_all_v():
        for j in g_algo.get_graph().get_all_v():
            path = g_algo.shortest_path(k, j)
        # print(f"shortest_path between {k} and {j}: ", path)

    print("Graph " + graph + " done!")


class GraphAlgoTest(unittest.TestCase):

    def test_get_graph(self):
        g = DiGraph()
        ga = GraphAlgo()
        self.assertIsNone(ga.get_graph())
        ga = GraphAlgo(g)
        self.assertEqual(ga.get_graph(), g)

    def test_save_and_load(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/A0")

        ga1 = GraphAlgo(ga.get_graph())
        self.assertEqual(ga1.get_graph(), ga.get_graph())

        ga1.save_to_json("../data/newA0.json")
        ga.load_from_json("../data/newA0.json")
        self.assertEqual(ga1.get_graph().get_mc(), ga.get_graph().get_mc())
        self.assertEqual(ga1.get_graph().v_size(), ga.get_graph().v_size())
        self.assertEqual(ga1.get_graph().e_size(), ga.get_graph().e_size())

    def test_shortest_path(self):
        g = graph_creator(5, 0)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(0, 4, 10)
        ga = GraphAlgo(g)
        expected = (4, [g.getNode(0), g.getNode(1), g.getNode(2), g.getNode(3), g.getNode(4)])
        actual = ga.shortest_path(0, 4)
        self.assertEqual(actual, expected)

        g.add_edge(0, 3, 1)
        expected = (2, [g.getNode(0), g.getNode(3), g.getNode(4)])
        actual = ga.shortest_path(0, 4)
        self.assertEqual(actual, expected)

        expected = (0, [g.getNode(0)])
        actual = ga.shortest_path(0, 0)
        self.assertEqual(actual, expected)

        expected = (math.inf, [])
        actual = ga.shortest_path(0, 20)
        self.assertEqual(actual, expected)

        expected = (math.inf, [])
        actual = ga.shortest_path(2, 0)
        self.assertEqual(actual, expected)

        expected = (1, [g.getNode(0), g.getNode(3)])
        actual = ga.shortest_path(0, 3)
        self.assertEqual(actual, expected)

    def test_connected_component(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)

        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 1, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 5, 1)
        ga = GraphAlgo(g)
        expected = [4]
        actual = ga.connected_component(4)
        self.assertEqual(expected,actual)

    def test_connected_components(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)

        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 1, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 5, 1)
        ga = GraphAlgo(g)
        expected = [[1,2,3],[4],[5]]
        actual = ga.connected_components()
        self.assertEqual(expected, actual)

    def test_plot_graph(self):
        g = GraphAlgo()
        file0 = "../data/A0"
        file1 = "../data/A1"
        file2 = "../data/A2"
        file3 = "../data/A3"
        file4 = "../data/A4"
        file5 = "../data/A5"
        fileT0 = "../data/T0.json"
        self.assertTrue(g.load_from_json(file0))
        g.plot_graph()
        self.assertTrue(g.load_from_json(file1))
        g.plot_graph()
        self.assertTrue(g.load_from_json(file2))
        g.plot_graph()
        self.assertTrue(g.load_from_json(file3))
        g.plot_graph()
        self.assertTrue(g.load_from_json(file4))
        g.plot_graph()
        self.assertTrue(g.load_from_json(file5))
        g.plot_graph()
        self.assertTrue(g.load_from_json(fileT0))
        g.plot_graph()

    def test_all_shortest_path(self):
        test_graph_loaded("A0")
        test_graph_loaded("A1")
        test_graph_loaded("A2")
        test_graph_loaded("A3")
        test_graph_loaded("A4")
        test_graph_loaded("A5")
        test_graph_loaded("T0.json")

    def test_plot_graph_of_100_vertices(self):
        g = graph_creator(100, 100)
        print(g)
        ga = GraphAlgo(g)
        ga.plot_graph()


if __name__ == '__main__':
    unittest.main()
