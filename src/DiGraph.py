from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.vertices: {int, NodeData} = dict()
        self.neighborsOut: {int, {int, float}} = dict()
        self.neighborsIn: {int, {int, float}} = dict()
        self.MC = 0
        self.edgeSize = 0

    def v_size(self) -> int:
        return len(self.vertices)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.neighborsIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.neighborsOut.get(id1)

    def get_mc(self) -> int:
        return self.MC

    def getEdge(self, src: int, dest: int):
        if self.neighborsOut.get(src) is None:
            return None
        return self.neighborsOut.get(src).get(dest)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
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
        self.edgeSize = self.edgeSize + 1
        self.MC += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.vertices.get(node_id) is not None:
            return False
        self.vertices[node_id] = NodeData(key=node_id, location=pos)
        self.neighborsOut[node_id] = {}
        self.neighborsIn[node_id] = {}
        self.MC = self.MC + 1
        return True

    def getNode(self, node_id: int):
        if self.vertices.get(node_id) is not None:
            return self.vertices.get(node_id)
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.vertices:
            lenOut = len(self.neighborsOut.get(node_id))
            lenIn = len(self.neighborsIn.get(node_id))
            self.edgeSize -= lenOut + lenIn
            self.neighborsOut.pop(node_id)
            self.neighborsIn.pop(node_id)
            self.vertices.pop(node_id)
            self.MC += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.vertices and node_id2 in self.vertices:
            if self.neighborsOut.get(node_id1) is None or self.neighborsOut.get(node_id1).get(
                    node_id2) is None:
                return False
            self.edgeSize = self.edgeSize - 1
            self.MC += 1
            self.neighborsOut.get(node_id1).pop(node_id2)
            self.neighborsIn.get(node_id2).pop(node_id1)
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, DiGraph):
            return False

        return True

    def __repr__(self):
        str_graph = "{\"Edges\":["
        for k in self.neighborsOut.keys():
            for k2, w in self.neighborsOut[k].items():
                str_graph += "{" + f"\"src\":{k},\"w\":{w},\"dest\":{k2}" + "}" + ","

        if str_graph[-1] == ',':
            str_graph = str_graph[:-1]

        str_graph += "],\"Nodes\":["
        # for k in self.vertices.keys():
        #     pos = self.vertices.get(k).getLocation()
        #     if pos is None:
        #         pos = (0, 0, 0)
        #     print(pos)
        #     str_graph += "{" + f"\"pos\":\"{pos[0]},{pos[1]},{pos[2]}\",\"id\":{k}" + "}" + ","

        for k, v in self.vertices.items():
            str_graph += str(v) + ","

        if str_graph[-1] == ',':
            str_graph = str_graph[:-1]
        str_graph += "]}"

        return str_graph

