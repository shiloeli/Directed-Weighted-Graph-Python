import json

import networkx as nx
from networkx.readwrite import json_graph
from unittest import TestCase


def graph_creator(v, e) -> nx.DiGraph:
    g = nx.DiGraph()
    for n in range(v):
        g.add_node(n)

    for i in range(0, v):
        for j in range(1, v):
            if g.number_of_edges() < e:
                g.add_edge(i, j)

        if g.number_of_edges() >= e:
            break

    return g


def save(G, file_name):
    json.dump(dict(nodes=[[n, G.node[n]] for n in G.nodes()],
                   edges=[[u, v, G.edge[u][v]] for u, v in G.edges()]),
              open(file_name, 'w'), indent=2)


def load(file_name):
    # G = nx.DiGraph()
    # d = json.load(open(file_name))
    # G.add_nodes_from(d['Nodes'])
    # G.add_edges_from(d['Edges'])
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
                g.add_edge(item['src'], item['dest'], weigth=item['w'])
            return True
    except IOError:
        return False
    # return G


class NetworkX_VS_MyGraph(TestCase):

    def test_save_and_load(self):
        g = load("../data/A0")
        print(g.nodes)

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

    def test_100_vertices(self):
        g = graph_creator(100, 100)
        self.assertEqual(g.number_of_nodes(), 100)

    def test_10000_vertices(self):
        g = graph_creator(10000, 10000)
        self.assertEqual(g.number_of_nodes(), 10000)

    def test_1000000_vertices(self):
        g = graph_creator(1000000, 1000000)
        self.assertEqual(g.number_of_nodes(), 1000000)

    def test_10000000_vertices(self):
        g = graph_creator(10000000, 10000000)
        self.assertEqual(g.number_of_nodes(), 10000000)
