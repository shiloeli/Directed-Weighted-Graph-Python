from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    """This class represent directed weighted graph
    That possible different actions on the graph, node and edge
    Vertices - contains all the nodes in the graph using dictionary.
    neighborsOut - Dictionary that contains a dictionary of key (the key of the destination node) and a value that represents the weight of the edge by the key of the source node
    neighborsIn -Dictionary that contains a dictionary of key (the key of the source node) and a value that represents the weight of the edge by the key of the destination node
    MC- Represents the number of changes made to the graph (adding a vertex and more ..).
    edgeSize- Contains the number of edges in the graph"""

    def __init__(self):
        """
        A constructor that sets default values for a graph.
        """

        self.vertices: {int, NodeData} = dict()
        self.neighborsOut: {int, {int, float}} = dict()
        self.neighborsIn: {int, {int, float}} = dict()
        self.__MC = 0
        self.__edgeSize = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        :return: number of vertices in this graph
        """

        return len(self.vertices)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """

        return self.__edgeSize

    def get_all_v(self) -> dict:
        """
       return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
       :return: dictionary of all the nodes in the Graph
       """

        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        Returns a dictionary that represents all vertices and the weight
         of the side that has a side to a given vertex
        :param id1:
        :return: dictionary that represents all vertices and the weight
        """

        return self.neighborsIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        Returns a dictionary that represents all vertices and the weight
         of the side that has a side from a given vertex
        :param id1:
        :return: dictionary that represents all vertices and the weight
        """

        return self.neighborsOut.get(id1)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        :return: current version of this graph
        """

        return self.__MC

    def getEdge(self, src: int, dest: int):
        """
        Returns the edge weight that exists in the graph by the source
         and destination value of the edge
        :param src:
        :param dest:
        :return: dge weight
        """

        if self.neighborsOut.get(src) is None:
            return None
        return self.neighborsOut.get(src).get(dest)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        :param id1:  The start node of the edge
        :param id2:  The end node of the edge
        :param weight: The weight of the edge
        :return: True if the edge was added successfully, False o.w.
        """

        if weight <= 0:
            return False
        if id1 == id2:
            return False

        src = self.vertices.get(id1)
        dest = self.vertices.get(id2)

        if src is None or dest is None:
            return False

        if id2 in self.neighborsOut.get(id1):
            return False

        self.neighborsOut[id1][id2] = weight
        self.neighborsIn[id2][id1] = weight
        self.__edgeSize = self.__edgeSize + 1
        self.__MC += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
          Adds a node to the graph.
        Note: if the node id already exists the node will not be added
        :param node_id:  The node ID
        :param pos:  The position of the node
        :return: True if the node was added successfully, False o.w.
        """

        if self.vertices.get(node_id) is not None:
            return False
        self.vertices[node_id] = NodeData(key=node_id, location=pos)
        self.neighborsOut[node_id] = {}
        self.neighborsIn[node_id] = {}
        self.__MC = self.__MC + 1
        return True

    def getNode(self, node_id: int) -> NodeData:
        """
        Returns the node by a given key
        :param node_id:
        :return: node
        """

        if self.vertices.get(node_id) is not None:
            return self.vertices.get(node_id)
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        Note: if the node id does not exists the function will do nothing
        :param node_id:  The node ID
        :return:  True if the node was removed successfully, False o.w.
        """

        if node_id in self.vertices:
            lenOut = len(self.neighborsOut.get(node_id))
            lenIn = len(self.neighborsIn.get(node_id))
            self.__edgeSize -= lenOut + lenIn
            self.neighborsOut.pop(node_id)
            self.neighborsIn.pop(node_id)
            self.vertices.pop(node_id)
            self.__MC += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        Note: If such an edge does not exists the function will do nothing
        :param node_id1: The start node of the edge
        :param node_id2: The end node of the edge
        :return: True if the edge was removed successfully, False o.w.
        """

        if node_id1 in self.vertices and node_id2 in self.vertices:
            if self.neighborsOut.get(node_id1) is None or self.neighborsOut.get(node_id1).get(
                    node_id2) is None:
                return False
            self.__edgeSize = self.__edgeSize - 1
            self.__MC += 1
            self.neighborsOut.get(node_id1).pop(node_id2)
            self.neighborsIn.get(node_id2).pop(node_id1)
            return True
        return False

    def __repr__(self):
        """
        :return: Returns all the values that make up a graph
        """

        str_graph = "{\"Edges\":["
        for k in self.neighborsOut.keys():
            for k2, w in self.neighborsOut[k].items():
                str_graph += "{" + f"\"src\":{k},\"w\":{w},\"dest\":{k2}" + "}" + ","

        if str_graph[-1] == ',':
            str_graph = str_graph[:-1]

        str_graph += "],\"Nodes\":["

        for k, v in self.vertices.items():
            str_graph += str(v) + ","

        if str_graph[-1] == ',':
            str_graph = str_graph[:-1]
        str_graph += "]}"

        return str_graph

    def __eq__(self, other):
        """
        A method that compares an existing graph with a graph obtained
         from the NetworkX_VS_MyGraph class to check if the resulting graphs are exactly the same
         by going over all the vertices and sides of the graph
        :param other: graph obtained from the NetworkX_VS_MyGraph
        :return: true or false
        """

        # Different size
        if self.v_size() != other.number_of_nodes():
            return False

        # Different nodes or positions
        for n in self.vertices:
            if not other.has_node(n):
                return False
            if other.nodes[n]['pos'] != self.getNode(n).getLocation():
                return False

        # Different edges or weight
        for node in self.neighborsOut:
            for key, weight in self.neighborsOut.get(node).items():
                if not other.has_edge(node,key):
                    return False

        return True
