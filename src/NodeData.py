class NodeData:

    def __init__(self, key: int = 0, info: int = -1, tag: int = 0, location: tuple = (0, 0, 0),
                 weight: float = 0):
        self.__key = key
        self.__info = info
        self.__tag = tag
        self.__location = location
        self.__weight = weight

    def setKey(self, k: int):
        self.__key = k

    def getKey(self) -> int:
        return self.__key

    def setInfo(self, i: int):
        self.__info = i

    def getInfo(self) -> int:
        return self.__info

    def setTag(self, t: int):
        self.__tag = t

    def getTag(self) -> int:
        return self.__tag

    def setLocation(self, t: tuple = (0, 0, 0)):
        self.__location = t

    def getLocation(self) -> tuple:
        return self.__location

    def setWeight(self, w: float):
        self.__weight = w

    def getWeight(self) -> float:
        return self.__weight

    def __repr__(self):
        if self.__location is None:
            self.__location = (0, 0, 0)
        return "{" + f"\"pos\":\"{self.__location[0]},{self.__location[1]},{self.__location[2]}\",\"id\":{self.__key}" + "}"
