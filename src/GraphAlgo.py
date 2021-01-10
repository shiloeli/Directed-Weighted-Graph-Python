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

    def __init__(self, graph: GraphInterface = None):
        self.__graph = graph

    def get_graph(self) -> GraphInterface:
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
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
        try:
            with open(file_name, "w") as file:
                file.write(str(self.__graph))
                return True
        except IOError:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
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
        plot = PlotGraph(self.__graph)
        plot.have_pos()
        if plot.have_pos() is False:
            plot.random_pos()
        plot.paint()

    def Dijkstra(self, node_id: int):
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
