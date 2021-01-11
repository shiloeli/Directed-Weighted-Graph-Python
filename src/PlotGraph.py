import random
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph


class PlotGraph:
    """This class is responsible for transferring the graph data to a graphical representation with
     the help of the matplotlib library"""

    def __init__(self, graph: DiGraph):
        """
        constructor
        :param graph: graph
        """
        self.graph = graph

    def have_pos(self) -> bool:
        """
        Checks if there is a vertex that does not have a pos
        :return: true or false
        """
        for k, v in self.graph.get_all_v().items():
            if (0, 0, 0) != v.getLocation():
                return True

        return False

    def random_pos(self) -> None:
        """
        Grid numbers in a given area for the position of points in the graph
        """
        for i in range(0, self.graph.v_size()):
            x = random.randint(1, 3000000)
            y = random.randint(1, 3000000)
            self.graph.get_all_v()[i].setLocation((x, y, 0))

    def paint(self):
        """
         This method draws the graph.
        """
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

        # x_values = []
        # y_values = []
        # id_node = []
        # for x, v in self.graph.get_all_v().items():
        #     x_values.append(v.getLocation()[0])
        #     y_values.append(v.getLocation()[1])
        #     id_node.append(x)
        #
        # fig, ax = plt.subplots()
        # ax.scatter(x_values, y_values)
        #
        # for i, txt in enumerate(id_node):
        #     ax.annotate(id_node[i], (x_values[i], y_values[i]), color='green')
        #
        # for k, v in self.graph.get_all_v().items():
        #     for n in self.graph.all_out_edges_of_node(k).keys():
        #         x = [v.getLocation()[0], self.graph.get_all_v()[n].getLocation()[0]]
        #         y = [v.getLocation()[1], self.graph.get_all_v()[n].getLocation()[1]]
        #         # plt.plot(x, y, "-", color='black')
        #         plt.annotate("", xy=(x[0], y[0]), xytext=(x[1], y[1]), arrowprops=dict(arrowstyle="-|>"))
        #
        # plt.plot(x_values, y_values, "o", color='red')
        # plt.title("Directed Weighted Graph")
        #
        # plt.show()


