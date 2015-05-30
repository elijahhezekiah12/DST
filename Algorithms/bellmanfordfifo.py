from dst.graph import Graph
from dst.queue import Queue

## This algorithm has yet to be fully tested

class BellmanFord():
    def __init__(self, Graph, source):
        self.graph = Graph
        # d represents the cost of each nodes, all nodes are initially set as inifinite
        self.d = [float("inf")] * Graph.size
        # each node has an parent pointer
        self.parent = [None] * Graph.size
        # source cost will always be 0
        self.d[source] = 0

        self.queue = Queue()
        self.queue.enqueue(source)

        
    # relaxtion technique, it will decrease d[y] throughout the computation
    def relax(self, x, y, weight):
            if self.d[y] > self.d[x] + weight:
                self.d[y] = self.d[x] + weight
                self.parent[y] = x

                if self.queue.exist(y) is False:
                    self.queue.enqueue(y)

    # bellman ford algorithm has two loops, the first is to apply the relaxation
    # technique to the nodes, the second node is to detect if there is any
    # negative cycles
    def bellmanford(self):
        while self.queue.isEmpty() is False:
            x = self.queue.dequeue()
            en = self.graph.edgenodes[x]
            while en is not None:
                self.relax(x, en.y, en.weight)
                en = en.next_edgenode

if __name__ == "__main__":
    graph = Graph(5, True)
    graph.insert(0, 1, 10, True)
    graph.insert(0, 2, 5, True)
    graph.insert(1, 3, 1, True)
    graph.insert(1, 2, 2, True)
    graph.insert(2, 1, 3, True)
    graph.insert(2, 4, 2, True)
    graph.insert(2, 3, 9, True)
    graph.insert(3, 4, 4, True)
    graph.insert(4, 0, 7, True)
    graph.insert(4, 3, 6, True)

    labels = {0:"s", 1:"u", 2:"x", 3:"v", 4:"y"}
    graph.set_labels(labels)
    graph.print_graph()
    b = BellmanFord(graph, 0)
    b.bellmanford()
    print "Cost: ", b.d
    print "Parent ",b.parent
