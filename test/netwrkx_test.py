import networkx as nx
from unittest import TestCase


class networkx_test(TestCase):

    def test_test1(self):
        g = nx.DiGraph()
        for i in range(0, 10000000):
            g.add_node(i)
