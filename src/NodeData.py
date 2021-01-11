class NodeData:
    """this class node_data represents the set of operations applicable on a node (vertex) in a (directional) weighted graph.
    The node in the graph consists of five things:
    key - Unique ID of the node in graph
    info- Contains some characteristic of the node such as color and more .. In this project it stores the parent node.
    tag-Temporal data which can be used be algorithms.
    location- location of this node.
    weight- Weight of the node."""

    def __init__(self, key: int = 0, info: int = -1, tag: int = 0, location: tuple = (0, 0, 0),
                 weight: float = 0):
        """Constructor of a node in graph"""
        self.__key = key
        self.__info = info
        self.__tag = tag
        self.__location = location
        self.__weight = weight

    def setKey(self, k: int):
        """Defines a unique ID for node"""
        self.__key = k

    def getKey(self) -> int:
        """Return a unique ID of node"""
        return self.__key

    def setInfo(self, i: int):
        """Defines an attribute for node"""
        self.__info = i

    def getInfo(self) -> int:
        """Return an attribute of node"""
        return self.__info

    def setTag(self, t: int):
        """Defines temporary data for node"""
        self.__tag = t

    def getTag(self) -> int:
        """Return temporary data of node"""
        return self.__tag

    def setLocation(self, t: tuple = (0, 0, 0)):
        """Defines the location of a node"""
        self.__location = t

    def getLocation(self) -> tuple:
        """Return the location of a node"""
        return self.__location

    def setWeight(self, w: float):
        """Defines weight for node"""
        self.__weight = w

    def getWeight(self) -> float:
        """Return weight for node"""
        return self.__weight

    def __repr__(self):
        """Returns the node data in the graph"""
        if self.__location is None:
            self.__location = (0, 0, 0)
        return "{" + f"\"pos\":\"{self.__location[0]},{self.__location[1]},{self.__location[2]}\",\"id\":{self.__key}" + "}"
