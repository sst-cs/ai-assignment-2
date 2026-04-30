import heapq

class Queue:
    """A standard FIFO queue for Breadth-First Search."""
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.pop(0)

class Stack:
    """A standard LIFO stack for Depth-First Search."""
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.pop()

class PriorityQueue:
    """A standard priority queue for A* Search."""
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, priority, item):
        # We push (priority, item) to the heap.
        # To handle cases where priority is the same, Python compares items.
        # Ensure items are comparable (e.g., strings).
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

class Graph:
    """A simple directed graph with edge weights."""
    def __init__(self):
        self.edges = {}
        self.weights = {}
    
    def neighbors(self, node):
        """Returns the neighbors of a given node in alphabetical order."""
        return sorted(self.edges.get(node, []))
    
    def cost(self, from_node, to_node):
        """Returns the cost (weight) of the edge from from_node to to_node."""
        return self.weights.get((from_node, to_node), 1)
