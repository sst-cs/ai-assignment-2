from utils import Graph
from search import bfs, dfs, ucs, a_star

def build_sample_graph():
    """
    Builds a simple graph for testing.
    This is based on the classic AI Romania map (simplified).
    """
    g = Graph()
    g.edges = {
        'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
        'Zerind': ['Arad', 'Oradea'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
        'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']
    }
    
    # Adding edge weights
    weights = {
        ('Arad', 'Zerind'): 75, ('Zerind', 'Arad'): 75,
        ('Arad', 'Sibiu'): 140, ('Sibiu', 'Arad'): 140,
        ('Arad', 'Timisoara'): 118, ('Timisoara', 'Arad'): 118,
        ('Zerind', 'Oradea'): 71, ('Oradea', 'Zerind'): 71,
        ('Oradea', 'Sibiu'): 151, ('Sibiu', 'Oradea'): 151,
        ('Timisoara', 'Lugoj'): 111, ('Lugoj', 'Timisoara'): 111,
        ('Lugoj', 'Mehadia'): 70, ('Mehadia', 'Lugoj'): 70,
        ('Mehadia', 'Drobeta'): 75, ('Drobeta', 'Mehadia'): 75,
        ('Drobeta', 'Craiova'): 120, ('Craiova', 'Drobeta'): 120,
        ('Craiova', 'Rimnicu Vilcea'): 146, ('Rimnicu Vilcea', 'Craiova'): 146,
        ('Craiova', 'Pitesti'): 138, ('Pitesti', 'Craiova'): 138,
        ('Rimnicu Vilcea', 'Sibiu'): 80, ('Sibiu', 'Rimnicu Vilcea'): 80,
        ('Rimnicu Vilcea', 'Pitesti'): 97, ('Pitesti', 'Rimnicu Vilcea'): 97,
        ('Sibiu', 'Fagaras'): 99, ('Fagaras', 'Sibiu'): 99,
        ('Fagaras', 'Bucharest'): 211, ('Bucharest', 'Fagaras'): 211,
        ('Pitesti', 'Bucharest'): 101, ('Bucharest', 'Pitesti'): 101,
        ('Bucharest', 'Giurgiu'): 90, ('Giurgiu', 'Bucharest'): 90,
        ('Bucharest', 'Urziceni'): 85, ('Urziceni', 'Bucharest'): 85,
        ('Urziceni', 'Hirsova'): 98, ('Hirsova', 'Urziceni'): 98,
        ('Hirsova', 'Eforie'): 86, ('Eforie', 'Hirsova'): 86,
        ('Urziceni', 'Vaslui'): 142, ('Vaslui', 'Urziceni'): 142,
        ('Vaslui', 'Iasi'): 92, ('Iasi', 'Vaslui'): 92,
        ('Iasi', 'Neamt'): 87, ('Neamt', 'Iasi'): 87
    }
    g.weights = weights
    
    return g

def get_heuristics():
    """Straight-line distance to Bucharest"""
    return {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
        'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
        'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
        'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

if __name__ == "__main__":
    graph = build_sample_graph()
    heuristics = get_heuristics()
    start_node = 'Arad'
    goal_node = 'Bucharest'
    
    print(f"--- Pathfinding from {start_node} to {goal_node} ---")
    
    print("\n[BFS Path]")
    bfs_path = bfs(graph, start_node, goal_node)
    print(bfs_path)
    
    print("\n[DFS Path]")
    dfs_path = dfs(graph, start_node, goal_node)
    print(dfs_path)
    
    print("\n[UCS Path]")
    ucs_path = ucs(graph, start_node, goal_node)
    print(ucs_path)
    
    print("\n[A* Path]")
    astar_path = a_star(graph, heuristics, start_node, goal_node)
    print(astar_path)
