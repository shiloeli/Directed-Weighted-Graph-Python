import random
import matplotlib.pyplot as plt
from Ex3.src.DiGraph import DiGraph


class PlotGraph:

    def __init__(self, graph: DiGraph, max_v: tuple = (0, 0, 0), min_v: tuple = (0, 0, 0)):
        self.graph = graph
        self.max_value = max_v
        self.min_value = min_v

    def have_pos(self) -> None:
        self.set_max_and_min()
        for k, v in self.graph.get_all_v().items():
            if v.getLocation() is None:
                self.random_pos(k)

    def set_max_and_min(self) -> None:
        for k, v in self.graph.get_all_v().items():
            if (0, 0, 0) != v.getLocation():
                if v.getLocation() > self.max_value:
                    self.max_value = v.getLocation()
                if v.getLocation() < self.min_value:
                    self.min_value = v.getLocation()

    def random_pos(self, key: int) -> None:
        node = self.graph.vertices.get(key)
        x = random.randint(self.min_value[0], self.max_value[0])
        y = random.randint(self.min_value[1], self.max_value[1])
        node.setLocation((x, y, 0))

        # for i in range(0, self.graph.v_size()):
        #     x = random.randint(1, 30)
        #     y = random.randint(1, 30)
        #     self.graph.get_all_v()[i].setLocation((x, y, 0))

    def paint(self):
        x_values = []
        y_values = []
        id_node = []
        for x, v in self.graph.get_all_v().items():
            x_values.append(v.getLocation()[0])
            y_values.append(v.getLocation()[1])
            id_node.append(x)

        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values)

        for i, txt in enumerate(id_node):
            ax.annotate(id_node[i], (x_values[i], y_values[i]), color='green')

        for k, v in self.graph.get_all_v().items():
            for n in self.graph.all_out_edges_of_node(k).keys():
                x = [v.getLocation()[0], self.graph.get_all_v()[n].getLocation()[0]]
                y = [v.getLocation()[1], self.graph.get_all_v()[n].getLocation()[1]]
                # plt.plot(x, y, "-", color='black')
                plt.annotate("", xy=(x[0], y[0]), xytext=(x[1], y[1]), arrowprops=dict(arrowstyle="-|>"))

        plt.plot(x_values, y_values, "o", color='red')
        plt.title("Directed Weighted Graph")

        plt.show()
