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
            if g.e_size() < e:
                g.add_edge(i, j, 10)

        if g.e_size() >= e:
            break

    return g


def test_graph_loaded(graph: str) -> None:
    g_algo = GraphAlgo()
    file = "../data/" + graph
    g_algo.load_from_json(file)
    g_algo.save_to_json(file + "_edited")
    limit = 0
    # for k in g_algo.get_graph().get_all_v():
    #     limit += 1
    #     if limit < 2:
    path = g_algo.shortest_path(0, 1)
    # print(limit)
    # else:
    #     return

    # # print(g_algo.get_graph())
    # g_algo.save_to_json(file + "_edited")
    # limit = 0
    # for k in g_algo.get_graph().get_all_v():
    #     limit += 1
    #     if limit < 1000:
    #         path = g_algo.shortest_path(0, k)
    #     else:
    #         return
    #
    # print("Graph " + graph + " done!")


class GraphAlgoTest(unittest.TestCase):

    def test_get_graph(self):
        g = DiGraph()
        ga = GraphAlgo()
        self.assertIsNone(ga.get_graph())
        ga = GraphAlgo(g)
        self.assertEqual(ga.get_graph().get_all_v(), g.get_all_v())

    def test_save_and_load(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_30000_240000_0.json")

        ga1 = GraphAlgo(ga.get_graph())
        self.assertEqual(ga1.get_graph().get_all_v(), ga.get_graph().get_all_v())

        ga1.save_to_json("../data/newG_30000_240000.json")
        ga.load_from_json("../data/newG_30000_240000.json")
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
        expected = (4, [0, 1, 2, 3, 4])
        actual = ga.shortest_path(0, 4)
        self.assertEqual(actual, expected)

        g.add_edge(0, 3, 1)
        expected = (2, [0, 3, 4])
        actual = ga.shortest_path(0, 4)
        self.assertEqual(actual, expected)

        expected = (0, [0])
        actual = ga.shortest_path(0, 0)
        self.assertEqual(actual, expected)

        expected = (math.inf, [])
        actual = ga.shortest_path(0, 20)
        self.assertEqual(actual, expected)

        expected = (math.inf, [])
        actual = ga.shortest_path(2, 0)
        self.assertEqual(actual, expected)

        expected = (1, [0, 3])
        actual = ga.shortest_path(0, 3)
        self.assertEqual(actual, expected)

    def test_all_shortest_path(self):
        test_graph_loaded("A0")
        test_graph_loaded("A1")
        test_graph_loaded("A2")
        test_graph_loaded("A3")
        test_graph_loaded("A4")
        test_graph_loaded("A5")
        test_graph_loaded("T0.json")

        test_graph_loaded("G_10_80_0.json")
        test_graph_loaded("G_100_800_0.json")
        test_graph_loaded("G_1000_8000_0.json")
        test_graph_loaded("G_10000_80000_0.json")
        test_graph_loaded("G_20000_160000_0.json")
        test_graph_loaded("G_30000_240000_0.json")
        #
        # test_graph_loaded("G_10_80_1.json")
        # test_graph_loaded("G_100_800_1.json")
        # test_graph_loaded("G_1000_8000_1.json")
        # test_graph_loaded("G_10000_80000_1.json")
        # test_graph_loaded("G_20000_160000_1.json")
        # test_graph_loaded("G_30000_240000_1.json")

    def test_connected_component_in_graph_loaded(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_10_80_0.json")
        component = ga.connected_component(0)
        self.assertEqual(len(component), ga.get_graph().v_size())

        ga.load_from_json("../data/G_100_800_0.json")
        component = ga.connected_component(0)
        self.assertEqual(len(component), ga.get_graph().v_size())

        ga.load_from_json("../data/G_1000_8000_0.json")
        component = ga.connected_component(0)
        self.assertEqual(len(component), ga.get_graph().v_size())

        ga.load_from_json("../data/G_10000_80000_0.json")
        component = ga.connected_component(0)
        self.assertEqual(9989, len(component))

        ga.load_from_json("../data/G_20000_160000_0.json")
        component = ga.connected_component(0)
        self.assertEqual(19985, len(component))

        ga.load_from_json("../data/G_30000_240000_0.json")
        component = ga.connected_component(0)
        self.assertEqual(29971, len(component))

    def test_connected_components_in_graph_loaded(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/G_10_80_0.json")
        component = ga.connected_components()
        self.assertEqual(1, len(component))

        ga.load_from_json("../data/G_100_800_0.json")
        component = ga.connected_components()
        self.assertEqual(1, len(component))
        #
        ga.load_from_json("../data/G_1000_8000_0.json")
        component = ga.connected_components()
        self.assertEqual(1, len(component))
        #
        ga.load_from_json("../data/G_10000_80000_0.json")
        component = ga.connected_components()
        self.assertEqual(12, len(component))

        ga.load_from_json("../data/G_20000_160000_0.json")
        component = ga.connected_components()
        self.assertEqual(16, len(component))
        #
        ga.load_from_json("../data/G_30000_240000_0.json")
        component = ga.connected_components()
        self.assertEqual(30, len(component))

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
        self.assertEqual(expected, actual)

        g = DiGraph()
        g.add_edge(1, 2, 2)
        ga = GraphAlgo(g)
        expected = []
        actual = ga.connected_component(2)
        self.assertEqual(expected, actual)

        g = DiGraph()
        g.add_node(1)
        g.add_edge(1, 1, 3)

        ga = GraphAlgo(g)
        expected = [1]
        actual = ga.connected_component(1)
        self.assertEqual(expected, actual)

        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_edge(1, 2, 3)
        ga = GraphAlgo(g)
        expected = [2]
        actual = ga.connected_component(2)
        self.assertEqual(expected, actual)

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
        expected = [[1, 2, 3], [4], [5]]
        actual = ga.connected_components()
        self.assertEqual(expected, actual)

        g = DiGraph()
        g.add_node(8)
        g.add_edge(8, 1, 3)
        ga = GraphAlgo(g)
        expected = [[8]]
        actual = ga.connected_components()
        self.assertEqual(expected, actual)

        g = DiGraph()
        g.add_edge(8, 1, 3)
        ga = GraphAlgo(g)
        expected = [[]]
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

        fileG_10 = "../data/G_10_80_0.json"
        # fileG_100 = "../data/G_100_800_0.json"
        # fileG_1000 = "../data/G_1000_8000_0.json"
        # fileG_10000 = "../data/G_10000_80000_0.json"
        # fileG_20000 = "../data/G_20000_160000_0.json"
        # fileG_30000 = "../data/G_30000_240000_0.json"

        fileG_10_circle = "../data/G_10_80_1.json"
        # fileG_100_circle = "../data/G_100_800_1.json"
        # fileG_1000_circle = "../data/G_1000_8000_1.json"
        # fileG_10000_circle = "../data/G_10000_80000_1.json"
        # fileG_20000_circle = "../data/G_20000_160000_1.json"
        # fileG_30000_circle = "../data/G_30000_240000_1.json"

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

        # self.assertTrue(g.load_from_json(fileG_10))
        # g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_100))
        # g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_1000))
        # g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_10000))
        # g.plot_graph()

        self.assertTrue(g.load_from_json(fileG_10_circle))
        g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_100_circle))
        # g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_1000_circle))
        # g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_10000_circle))
        # g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_20000_circle))
        # g.plot_graph()
        # self.assertTrue(g.load_from_json(fileG_30000_circle))
        # g.plot_graph()

    def test_plot_graph_of_100_vertices(self):
        g = graph_creator(100, 100)
        print(g)
        ga = GraphAlgo(g)
        ga.plot_graph()


if __name__ == '__main__':
    unittest.main()
