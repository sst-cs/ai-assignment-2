from utils import Queue, Stack, PriorityQueue

def bfs(graph, start, goal):
    """
    Breadth-First Search
    
    Args:
        graph: A Graph object
        start: The starting node (string)
        goal: The goal node (string)
        
    Returns:
        A list of strings representing the path from start to goal.
        Return None if no path is found.
    """
    # TODO: Implement BFS using the Queue class from utils.py
    pass

def dfs(graph, start, goal):
    """
    Depth-First Search
    
    Args:
        graph: A Graph object
        start: The starting node (string)
        goal: The goal node (string)
        
    Returns:
        A list of strings representing the path from start to goal.
        Return None if no path is found.
    """
    # TODO: Implement DFS using the Stack class from utils.py
    pass

def ucs(graph, start, goal):
    """
    Uniform Cost Search
    
    Args:
        graph: A Graph object
        start: The starting node (string)
        goal: The goal node (string)
        
    Returns:
        A list of strings representing the path from start to goal.
        Return None if no path is found.
    """
    # TODO: Implement UCS using the PriorityQueue class from utils.py
    pass

def a_star(graph, heuristic, start, goal):
    """
    A* Search
    
    Args:
        graph: A Graph object
        heuristic: A dictionary mapping nodes to their heuristic value {node: h(node)}
        start: The starting node (string)
        goal: The goal node (string)
        
    Returns:
        A list of strings representing the path from start to goal.
        Return None if no path is found.
    """
    # TODO: Implement A* Search using the PriorityQueue class from utils.py
    pass
