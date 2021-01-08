import json
from builtins import list
from typing import List
from Ex3.src import GraphInterface
from Ex3.src.GraphAlgoInterface import GraphAlgoInterface
from Ex3.src.DiGraph import DiGraph
from Ex3.src.PlotGraph import PlotGraph
from Ex3.src.PriorityQueue import PriorityQueue
import math


class GraphAlgo(GraphAlgoInterface):

    # def __init__(self, g: DiGraph()):
    #     self.graph = g

    def __init__(self, graph: GraphInterface = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        self.graph = DiGraph()
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

                    self.graph.add_node(item['id'], (pos[0], pos[1], pos[2]))

                for item in my_dict['Edges']:
                    self.graph.add_edge(item['src'], item['dest'], item['w'])

                return True
        except IOError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                file.write(str(self.graph))
                return True
        except IOError:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.vertices or id2 not in self.graph.vertices:
            return None
        self.Dijkstra(id1)
        distance = self.graph.vertices.get(id2).getWeight()

        if distance == math.inf:
            pathInf = (distance, [])
            return pathInf

        path_list = []
        if id1 == id2:
            path_list.insert(0, self.graph.getNode(id2))
            distance = 0
            listSp = (distance, path_list)
            return listSp
        else:
            dest = self.graph.getNode(id2)
            path_list.insert(0, self.graph.getNode(id2))
            parent = self.graph.getNode(int(dest.getInfo()))

            while parent.getInfo() != -1:
                path_list.insert(0, parent)
                parent = self.graph.getNode(parent.getInfo())
            path_list.insert(0, self.graph.getNode(id1))
        listSp = distance, path_list

        return listSp

    def connected_component(self, id1: int) -> list:
        neiIn = []
        neiOut = []
        allNode = [self.graph.getNode(id1)]
        neiOut.append(self.graph.getNode(id1))
        for n in self.graph.get_all_v().keys():
            temp = self.graph.vertices.get(n)
            temp.setTag(-1)
        while len(allNode) != 0:
            prev = allNode.pop()
            prev.setTag(0)
            for nOut in self.graph.neighborsOut.get(prev.getKey()).keys():
                temp1 = self.graph.vertices.get(nOut)
                if temp1.getTag() != 0:
                    allNode.append(temp1)
                    neiOut.append(temp1)
                    temp1.setTag(0)

        for n in self.graph.get_all_v().keys():
            temp = self.graph.vertices.get(n)
            temp.setTag(-1)
        allNode.append(self.graph.getNode(id1))
        neiIn.append(self.graph.getNode(id1))
        while len(allNode) != 0:
            prev = allNode.pop()
            prev.setTag(0)
            for nIn in self.graph.neighborsIn.get(prev.getKey()).keys():
                temp2 = self.graph.vertices.get(nIn)
                if temp2.getTag() != 0:
                    allNode.append(temp2)
                    neiIn.append(temp2)
                    temp2.setTag(0)

        for node in neiOut:
            for node2 in neiIn:
                if node.getKey() == node2.getKey():
                    allNode.append(node)
                    break
        return allNode

    def connected_components(self) -> List[list]:
        allComponents = []
        allV = []
        for k in self.graph.get_all_v().keys():
            allV.append(k)
        while len(allV) != 0:
            temp = allV[0]
            oneComponent = self.connected_component(temp)
            allComponents.append(oneComponent)

            for v in oneComponent:
                allV.remove(v.getKey())
        return allComponents

    def plot_graph(self) -> None:
        plot = PlotGraph(self.graph)
        if plot.have_pos() is False:
            plot.random_pos()
        plot.paint()

    def Dijkstra(self, node_id: int):
        queue = PriorityQueue()
        for node in self.graph.vertices.values():
            node.setWeight(math.inf)
            node.setInfo(-1)
        src = self.graph.vertices.get(node_id)
        src.setWeight(0)
        queue.insert(src)
        while not queue.isEmpty():
            prev = queue.delete()
            for k, w in self.graph.all_out_edges_of_node(prev.getKey()).items():
                dest = self.graph.vertices.get(k)
                if dest.weight > prev.getWeight() + w:
                    dest.setWeight(prev.getWeight() + w)
                    queue.insert(dest)
                    dest.setInfo(prev.getKey())