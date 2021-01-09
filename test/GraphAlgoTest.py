import unittest

from Ex3.src.DiGraph import DiGraph
from Ex3.src.GraphAlgo import GraphAlgo


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

    # def test_shortest_path(self):
    #     g = graph_creator(5, 0)
    #     g.add_edge(0, 1, 1)
    #     g.add_edge(1, 2, 1)
    #     g.add_edge(2, 3, 1)
    #     g.add_edge(3, 4, 1)
    #     g.add_edge(0, 4, 10)
    #     ga = GraphAlgo(g)
    #     expected = (4, [0, 1, 2, 3, 4])
    #     actual = ga.shortest_path(0, 4)
    #     self.assertEqual(actual, expected)
    #     g.add_edge(0, 3, 1)
    #     expected = (2, [0, 3, 4])
    #     actual = ga.shortest_path(0, 4)
    #     self.assertEqual(actual, expected)
    #     actual = ga.shortest_path(0, 0)
    #     self.assertIsNone(actual)
    #     actual = ga.shortest_path(0, 20)
    #     self.assertIsNone(actual)
    #     actual = ga.shortest_path(2, 0)
    #     self.assertIsNone(actual)
    #     expected = (1, [0, 3])
    #     actual = ga.shortest_path(0, 3)
    #     self.assertEqual(actual, expected)

    #
    #     def test_connected_component(self):
    #         pass
    #
    #     def test_connected_components(self):
    #         pass

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

    def test_general1(self):
        g_algo = GraphAlgo()
        file = '../data/A5'
        g_algo.load_from_json(file)
        print(g_algo.get_graph())
        g_algo.save_to_json(file + "_edited")
        for k in g_algo.get_graph().get_all_v():
            for j in g_algo.get_graph().get_all_v():
                path = g_algo.shortest_path(k, j)
                print(f"shortest_path between {k} and {j}: ", path)

    def test_plot_graph_of_100_vertices(self):
        g = graph_creator(100, 100)
        print(g.vertices)
        ga = GraphAlgo(g)
        ga.plot_graph()


if __name__ == '__main__':
    unittest.main()
