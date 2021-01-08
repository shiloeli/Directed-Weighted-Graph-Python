from src.NodeData import NodeData


class PriorityQueue(NodeData):

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, nd):
        self.queue.append(nd)

    def delete(self):
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
