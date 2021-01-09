from unittest import TestCase
from Ex3.src.DiGraph import DiGraph
from Ex3.src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        g = DiGraph()
        g2 = GraphAlgo()
        g.add_node(1)
        g.add_node(2)
        g.add_edge(1, 2, 3)
        g2.graph = g
        g2.save_to_json("..data/b1")

    def test_shortest_path(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 1)
        g.add_edge(3, 4, 3)
        g.add_edge(2, 4, 2)
        g2 = GraphAlgo()
        g2.graph = g
        print(g2.shortest_path(2, 3))

    def test_connected_component(self):
        g_algo = GraphAlgo()
        file = '../data/A1'
        g_algo.load_from_json(file)
        print(g_algo.connected_component(1))

        # g = DiGraph()
        # g.add_node(1)
        # g.add_node(2)
        # g.add_node(4)
        # g.add_edge(1, 2, 8)
        # g.add_edge(2, 1, 9)
        # g.add_edge(4, 1, 9)
        #
        # g2 = GraphAlgo()
        # g2.graph = g
        # print(g2.connected_component(1))

    def test_connected_components(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(1, 2, 8)
        g.add_edge(2, 1, 9)
        g.add_edge(4, 1, 9)
        g.add_edge(4, 5, 7)
        g.add_edge(5, 4, 7)
        g2 = GraphAlgo()
        g2.graph = g
        print(g2.connected_components())

    def test_save_and_load(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/A5")

        ga1 = GraphAlgo()
        ga1.graph = ga.get_graph()
        self.assertEqual(ga1.get_graph(), ga.get_graph())

        # ga1.save_to_json("../data/newA0.json")
        # ga.load_from_json("../data/newA0.json")
        # self.assertEqual(ga1.get_graph().get_mc(), ga.get_graph().get_mc())
        # self.assertEqual(ga1.get_graph().v_size(), ga.get_graph().v_size())
        # self.assertEqual(ga1.get_graph().e_size(), ga.get_graph().e_size())

    def test_general1(self):
        g_algo = GraphAlgo()
        file = '../data/A5'
        g_algo.load_from_json(file)
        print(g_algo.get_graph())
        # g_algo.save_to_json(file + "_edited")
        for k in g_algo.get_graph().get_all_v():
            for j in g_algo.get_graph().get_all_v():
                path = g_algo.shortest_path(k, j)
                print(f"shortest_path between {k} and {j}: ", path)

    def test_plot_graph(self):
        self.fail()
