class Node:
    nodeId = 0
    paths = []
    def __init__(id_, paths_):
        nodeId = id_
        paths = paths_


    def isEnd(self):
        if(len(self.paths)==0):
            return True
        return False

    def getPaths(self):
        return self.paths

    def getId(self):
        return self.nodeId
