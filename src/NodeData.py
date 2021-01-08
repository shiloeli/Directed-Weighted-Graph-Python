class NodeData:

    def __init__(self, key: int = 0, info: int = -1, tag: int = 0, location: tuple = (0, 0, 0),
                 weight: float = 0):
        self.key = key
        self.info = info
        self.tag = tag
        self.location = location
        self.weight = weight

    def setKey(self, k: int):
        self.key = k

    def getKey(self) -> int:
        return self.key

    def setInfo(self, i: str):
        self.info = i

    def getInfo(self) -> str:
        return self.info

    def setTag(self, t: int):
        self.tag = t

    def getTag(self) -> int:
        return self.tag

    def setLocation(self, t: tuple):
        self.location = t

    def getLocation(self) -> tuple:
        return self.location

    def setWeight(self, w: float):
        self.weight = w

    def getWeight(self) -> float:
        return self.weight

    # def __repr__(self):
    #     if self.location is None:
    #         self.location = (0, 0, 0)
    #
    #     return f"(key: {self.key} , info: {self.info} , tag: {self.tag}, location: {self.location} , weight:  " \
    #            f"{self.weight} )"

    def __repr__(self):
        if self.location is None:
            self.location = (0, 0, 0)

        return "{" + f"\"pos\":\"{self.location[0]},{self.location[1]},{self.location[2]}\",\"id\":{self.key}" + "}"
