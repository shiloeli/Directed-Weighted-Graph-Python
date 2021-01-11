from src.NodeData import NodeData


class PriorityQueue(NodeData):
    """This class implements a priority queue by the following methods """

    def __init__(self):
        """
        constructor
        """

        self.queue = []

    def isEmpty(self):
        """
        :return: True method if the queue is empty otherwise false
        """

        return len(self.queue) == 0

    def insert(self, nd):
        """
        A method that adds value to a queue
        :param nd: node
        :return:
        """

        self.queue.append(nd)

    def delete(self):
        """
        A method that deletes an element from the queue and updates
        the position according to the weight of the values in the queue
        :return: node
        """

        try:
            mini = 0
            for i in range(len(self.queue)):
                if self.queue[i].getWeight() < self.queue[mini].getWeight() :
                    mini = i
            item = self.queue[mini]
            del self.queue[mini]
            return item
        except IndexError:
            print()
            exit()

    def peek(self):
        """
        A method that displays the member at the top of the queue and updates the position
        according to the weight of the values in the queue
        :return: node
        """

        try:
            mini = 0
            for i in range(len(self.queue)):
                if self.queue[i].getWeight() < self.queue[mini].getWeight():
                    mini = i
            item = self.queue[mini]
            return item
        except IndexError:
            print()
            exit()
