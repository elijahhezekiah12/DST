class EdgeNode():
    def __init__(self, y, weight, next_edgenode):
        self.y = y
        self.weight = weight
        self.next_edgenode = next_edgenode

class Graph():
    def __init__(self, MAXV, directed):
        self.edgenodes = [None] * MAXV
        self.degree = [0] * MAXV
        self.nvertices = 0
        self.nedges = 0
        self.directed = directed

    def insert(self, x, y, directed):
        self.check_node_exist(self.edgenodes[x])
        en = EdgeNode(y, None, self.edgenodes[x])
        self.edgenodes[x] = en
        self.degree[x] += 1

        if directed is False:
            self.insert(y, x, True)
        else:
            self.nedges += 1

    def check_node_exist(self, e): 
        if e is None:
            self.nvertices += 1
        
        while e is not None:
            if self.edgenodes[e.y] is None:
                self.nvertices += 1
            e = e.next_edgenode

    def print_graph(self):
        for i in range(len(self.edgenodes)):
            print i, "|",
            en = self.edgenodes[i]
            while en is not None:
                print en.y,
                en = en.next_edgenode
            print ""

if __name__ == "__main__":
    graph = Graph(10, False)
    graph.insert(1, 6, False)
    graph.insert(1, 5, False)
    graph.insert(1, 2, False)
    graph.insert(2, 3, False)
    graph.insert(2, 5, False)
    graph.insert(3, 4, False)
    graph.insert(4, 5, False)
    graph.print_graph()
