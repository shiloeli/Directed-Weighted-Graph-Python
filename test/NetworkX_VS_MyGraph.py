import json

import networkx as nx
from networkx.readwrite import json_graph
from unittest import TestCase

from src.GraphAlgo import GraphAlgo


def graph_creator(v, e) -> nx.DiGraph:
    g = nx.DiGraph()
    g.has_edge()
    g._
    for n in range(v):
        g.add_node(n)

    for i in range(0, v):
        for j in range(1, v):
            if g.number_of_edges() < e:
                g.add_edge(i, j)

        if g.number_of_edges() >= e:
            break

    return g


def save_json_in_networkX(G, file_name):
    str_graph = "{\"Edges\":["
    for s, d, w in G.edges(data=True):
        str_graph += "{" + f"\"src\":{s},\"w\":{w['weight']},\"dest\":{d}" + "}" + ","

    if str_graph[-1] == ',':
        str_graph = str_graph[:-1]

    str_graph += "],\"Nodes\":["

    for node, data in G.nodes(data=True):
        str_graph += "{" + f"\"pos\":\"{data['pos'][0]},{data['pos'][1]},{data['pos'][2]}\",\"id\":{node}" + "}" + ","

    if str_graph[-1] == ',':
        str_graph = str_graph[:-1]
    str_graph += "]}"

    try:
        with open(file_name, "w") as file:
            file.write(str_graph)
            return True
    except IOError:
        return False


def load_json_in_networkX(file_name) -> nx.DiGraph:
    g = nx.DiGraph()
    try:
        with open(file_name, "r") as file:
            my_dict = json.load(file)
            for item in my_dict['Nodes']:
                pos = []
                if "pos" in item:
                    for p in item['pos'].split(','):
                        pos.append(float(p))
                else:
                    pos = [0, 0, 0]

                g.add_node(item['id'], pos=(pos[0], pos[1], pos[2]))

            for item in my_dict['Edges']:
                g.add_edge(item['src'], item['dest'])
                g[item['src']][item['dest']]['weight'] = item['w']

            return g
    except IOError:
        return False


class NetworkX_VS_MyGraph(TestCase):

    def test_save_and_load_and_equal(self):
        g = load_json_in_networkX("../data/A0")
        save_json_in_networkX(g, "../data/newA0.json")
        ga = GraphAlgo()
        ga.load_from_json("../data/newA0.json")
        self.assertTrue(ga.get_graph().__eq__(g))

        g = load_json_in_networkX("../data/A1")
        save_json_in_networkX(g, "../data/newA1.json")
        ga = GraphAlgo()
        ga.load_from_json("../data/A1")
        self.assertTrue(ga.get_graph().__eq__(g))

        g = load_json_in_networkX("../data/A2")
        save_json_in_networkX(g, "../data/newA2.json")
        ga = GraphAlgo()
        ga.load_from_json("../data/A2")
        self.assertTrue(ga.get_graph().__eq__(g))

        g = load_json_in_networkX("../data/A3")
        save_json_in_networkX(g, "../data/newA3.json")
        ga = GraphAlgo()
        ga.load_from_json("../data/A3")
        self.assertTrue(ga.get_graph().__eq__(g))

        g = load_json_in_networkX("../data/A4")
        save_json_in_networkX(g, "../data/newA4.json")
        ga = GraphAlgo()
        ga.load_from_json("../data/A4")
        self.assertTrue(ga.get_graph().__eq__(g))

        g = load_json_in_networkX("../data/A5")
        save_json_in_networkX(g, "../data/newA4.json")
        ga = GraphAlgo()
        ga.load_from_json("../data/A5")
        self.assertTrue(ga.get_graph().__eq__(g))

        g = load_json_in_networkX("../data/T0.json")
        save_json_in_networkX(g, "../data/newT0.json")
        ga = GraphAlgo()
        ga.load_from_json("../data/T0.json")
        self.assertTrue(ga.get_graph().__eq__(g))

    def test_shortest_path(self):
        g = graph_creator(5, 0)
        g.add_edge(0, 1)
        g[0][1]['weight'] = 1
        g.add_edge(1, 2)
        g[1][2]['weight'] = 1
        g.add_edge(2, 3)
        g[2][3]['weight'] = 1
        g.add_edge(3, 4)
        g[3][4]['weight'] = 1
        g.add_edge(0, 4)
        g[0][4]['weight'] = 10
        expected = [0, 1, 2, 3, 4]
        actual = nx.dijkstra_path(g, 0, 4)
        self.assertEqual(expected, actual)

        g.add_edge(0, 3)
        g[0][3]['weight'] = 1

        expected = [0, 3, 4]
        actual = nx.dijkstra_path(g, 0, 4)
        self.assertEqual(actual, expected)

        expected = [0]
        actual = nx.dijkstra_path(g, 0, 0)
        self.assertEqual(actual, expected)

        expected = [0, 3]
        actual = nx.dijkstra_path(g, 0, 3)
        self.assertEqual(actual, expected)

    def calculate_shortest_path(self, g):
        limit = 0
        for node, data in g.nodes(data=True):
            limit += 1
            if limit < 1000:
                try:
                    # for node1, data1 in g.nodes(data=True):
                    # print(nx.dijkstra_path(g, node, node1))
                    nx.dijkstra_path(g, 0, node)
                except nx.NetworkXNoPath:
                    pass
            else:
                return

    def test_shortest_path_of_graph(self):
        g = load_json_in_networkX("../data/G_10_80_0.json")
        self.calculate_shortest_path(g)
        print("G_10_80_0 Done!")

        g = load_json_in_networkX("../data/G_100_800_0.json")
        self.calculate_shortest_path(g)
        print("G_100_800_0 Done!")

        g = load_json_in_networkX("../data/G_1000_8000_0.json")
        self.calculate_shortest_path(g)
        print("G_1000_8000_0 Done!")

        g = load_json_in_networkX("../data/G_10000_80000_1.json")
        self.calculate_shortest_path(g)
        print("G_10000_80000_1 Done!")

        g = load_json_in_networkX("../data/G_20000_160000_0.json")
        self.calculate_shortest_path(g)
        print("G_20000_160000_0 Done!")

        g = load_json_in_networkX("../data/G_30000_240000_0.json")
        self.calculate_shortest_path(g)
        print("G_30000_240000_0 Done!")

        # g = load_json_in_networkX("../data/A0")
        # self.calculate_shortest_path(g)
        # print("A0 Done!")
        #
        # g = load_json_in_networkX("../data/A1")
        # self.calculate_shortest_path(g)
        # print("A1 Done!")
        #
        # g = load_json_in_networkX("../data/A2")
        # self.calculate_shortest_path(g)
        # print("A2 Done!")
        #
        # g = load_json_in_networkX("../data/A3")
        # self.calculate_shortest_path(g)
        # print("A3 Done!")
        #
        # g = load_json_in_networkX("../data/A4")
        # self.calculate_shortest_path(g)
        # print("A4 Done!")
        #
        # g = load_json_in_networkX("../data/A5")
        # self.calculate_shortest_path(g)
        # print("A5 Done!")

    def test_100_vertices(self):
        g = graph_creator(100, 100)
        self.assertEqual(g.number_of_nodes(), 100)

    def test_10000_vertices(self):
        g = graph_creator(10000, 10000)
        self.assertEqual(g.number_of_nodes(), 10000)

    def test_1000000_vertices(self):
        g = graph_creator(1000000, 1000000)
        self.assertEqual(g.number_of_nodes(), 1000000)
