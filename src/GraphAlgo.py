import json
from builtins import list
from typing import List
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.PlotGraph import PlotGraph
from src.PriorityQueue import PriorityQueue
import math


class GraphAlgo(GraphAlgoInterface):
    """This class represents a Directed (positive) Weighted Graph Theory Algorithms including:
    0. __init__()
    1. get_graph(self)
    2. load_from_json(self, file_name: str)
    3. save_to_json(self, file_name: str)
    4. shortest_path(self, id1: int, id2: int)
    5. connected_component(self, id1: int)
    6. connected_components(self)
    7. plot_graph(self)
    graph-Is an abstract representation of a set of nodes and edge,
    each edge has a weight,
    it is possible to have a route from node to another node."""

    def __init__(self, graph: GraphInterface = None):
        """
        Graph builder
        :param graph: graph
        """
        self.__graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on
        """

        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        """
        This method load a graph to this graph.
        if the file was successfully loaded - the underlying graph
        of this class will be changed (to the loaded one), in case the
        graph was not loaded the original graph should remain "as is".
        :param file_name: file
        :return: true or false
        """

        self.__graph = DiGraph()
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

                    self.__graph.add_node(item['id'], (pos[0], pos[1], pos[2]))

                for item in my_dict['Edges']:
                    self.__graph.add_edge(item['src'], item['dest'], item['w'])

                return True
        except IOError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves this weighted (directed) graph to the given
        file name - in JSON format
        :param file_name: file
        :return: true or false
        """
        try:
            with open(file_name, "w") as file:
                file.write(str(self.__graph))
                return True
        except IOError:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm - as an ordered List of nodes:
        src--> n1-->n2-->...dest.
        By pass the shortest path from the end to the beginning.
        if no such path exists return math.inf, [ ](Maximum route length and empty list).
        The method adds the destination vertex (id2) to the list and accesses the parent vertex by the info value of the
        vertex until it arrives node that its info value is -1 which we set as the end of the trajectory.
        We will then create a list that will contain the weight of the destination node (id2) and the list of vertices
        of the shortest route created
        :param id1: src
        :param id2: dest
        :return: list of shortest path
        """

        if id1 not in self.__graph.vertices or id2 not in self.__graph.vertices:
            pathInf = (math.inf, [])
            return pathInf

        self.Dijkstra(id1)
        distance = self.__graph.vertices.get(id2).getWeight()

        if distance == math.inf:
            pathInf = (distance, [])
            return pathInf

        path_list = []
        if id1 == id2:
            path_list.insert(0, id2)
            distance = 0
            listSp = (distance, path_list)
            return listSp
        else:
            path_list.insert(0, id2)
            parent = self.__graph.getNode(id2)

            while parent.getInfo() != -1:
                path_list.insert(0, parent.getInfo())
                parent = self.__graph.getNode(parent.getInfo())
        listSp = distance, path_list

        return listSp

    def connected_component(self, id1: int) -> list:
        """
        This method gets a vertex Finds the Strongly Connected Component (SCC) that node id1 is a part of.
        If the node does not exist in the graph another blank list will be returned
        A list will be returned that will contain the nodes keys that are part of the bindings component.
        This method creates 3 lists: neiOut- contains the vertices that can be reached from the source node and
        neiIn- which contains the vertices in the graph that can be reached from the source node.
        Another allNode list in which all vertices are transferred and sent to the Valentine list from the previous 2.
        We will first insert the source vertex into allNode and neiOut
        We will reset the tag values of all the vertices of the graph-1 and for the source vertex
        we have a value of tag 0 then we will add all the vertices that can be reached from the source node to
        neiOut by going over the neighbors of each vertex entering allNode and defining each vertex entering
        a tag 0 so we do not repeat the operation From one time. We will perform these operations as long as
        the allNode list is not empty
        We will perform the same operation in the opposite direction, we will add to allNode all the codecs that
        can be reached from the source node by going over the neighbors' neighbors and thus we will fill
        in the neiIn list.
        Once these 2 lists are complete we will create a list that will contain the vertices that belong
        to neiIn and also neiOut which will return to us the Strongly Connected Component.

        :param id1: src
        :return: list of Strongly Connected Component
        """

        if self.__graph.vertices.get(id1) is None:
            list_none = []
            return list_none
        neiIn = []
        neiOut = []
        allNode = [self.__graph.getNode(id1)]
        neiOut.append(self.__graph.getNode(id1))

        for n in self.__graph.get_all_v().keys():
            temp = self.__graph.vertices.get(n)
            temp.setTag(-1)

        while len(allNode) > 0:
            prev = allNode.pop()
            prev.setTag(0)

            for nOut in self.__graph.neighborsOut.get(prev.getKey()).keys():
                temp1 = self.__graph.vertices.get(nOut)
                if temp1.getTag() != 0:
                    allNode.append(temp1)
                    neiOut.append(temp1)
                    temp1.setTag(0)

        for n in self.__graph.get_all_v().keys():
            temp = self.__graph.vertices.get(n)
            temp.setTag(-1)
        allNode.append(self.__graph.getNode(id1))
        neiIn.append(self.__graph.getNode(id1))

        while len(allNode) > 0:
            prev = allNode.pop()
            prev.setTag(0)
            for nIn in self.__graph.neighborsIn.get(prev.getKey()).keys():
                temp2 = self.__graph.vertices.get(nIn)
                if temp2.getTag() != 0:
                    allNode.append(temp2)
                    neiIn.append(temp2)
                    temp2.setTag(0)

        for node in neiOut:
            for node2 in neiIn:
                if node.getKey() == node2.getKey():
                    allNode.append(node.getKey())
                    break
        return allNode

    def connected_components(self) -> List[list]:
        """
          Finds all the Strongly Connected Component(SCC) in the graph.
        If there are no binding elements in the graph, [[]]] will return a list of empty lists.
        In the method we put all the keys in the graph in the allV list.
        We then sent a random vertex to the connected_component method ()
        The list of the linking component we received will be added to the allComponents list
        And the vertices component bindings we got from the method we will remove from the allV list.
        We will do this as long as our list of vertices is not empty.
        And finally we return the allComponents list that contains all the existing binding elements in the graph.
        :return: list of list of Strongly Connected Components
        """

        if self.__graph.v_size() < 1:
            return [[]]

        allComponents = []
        allV = []

        for k in self.__graph.get_all_v().keys():
            allV.append(k)

        while len(allV) > 0:
            temp = allV[0]
            oneComponent = self.connected_component(temp)
            allComponents.append(oneComponent)

            for v in oneComponent:
                allV.remove(v)
        return allComponents

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        The method draws the graph using the PlotGraph class
        (An explanation of the methods can be found in the imitation)
        Which has methods that create the graph using the "matplotlib" directory
        """

        plot = PlotGraph(self.__graph)
        plot.have_pos()
        if plot.have_pos() is False:
            plot.random_pos()
        plot.paint()

    def Dijkstra(self, node_id: int):
        """
        Algorithm for finding the shortest route with the help of a priority queue
        We will first go through all the nodes in the graph and define their math.inf weight
        Value info -1
        We will insert the given vertex into the queue and as long as the queue is not empty
         we will perform the following steps:
        We will delete the vertex at the top of the queue and pass over all the neighbors of the
        same vertex and define a weight for them using the weight of the parent node and the connecting
        side between them so that we pass over all the vertices in the graph
        (if it is a different link only to some of them)
        And we will mark their weight a method which will help us find the shortest route.
        :param node_id: src
        """

        queue = PriorityQueue()
        for node in self.__graph.vertices.values():
            node.setWeight(math.inf)
            node.setInfo(-1)
        src = self.__graph.vertices.get(node_id)
        src.setWeight(0)
        queue.insert(src)
        while not queue.isEmpty():
            prev = queue.delete()
            for k, w in self.__graph.all_out_edges_of_node(prev.getKey()).items():
                dest = self.__graph.vertices.get(k)
                if dest.getWeight() > prev.getWeight() + w:
                    dest.setWeight(prev.getWeight() + w)
                    queue.insert(dest)
                    dest.setInfo(prev.getKey())
