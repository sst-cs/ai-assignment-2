# AI Assignment 02: Uninformed and Informed Searches

In this assignment, you will implement classical search algorithms to navigate a pathfinding agent through a graph of cities.

## Your Task

Open `search.py` and implement the following three algorithms:

1. **Breadth-First Search (`bfs`)**: Implement using the `Queue` class from `utils.py`.
2. **Depth-First Search (`dfs`)**: Implement using the `Stack` class from `utils.py`.
3. **A* Search (`a_star`)**: Implement using the `PriorityQueue` class from `utils.py`.

### Rules & Guidelines
- You **must** use the data structures provided in `utils.py`.
- **Alphabetical Tie-Breaking**: When expanding a node, always explore its neighbors in alphabetical order. The `graph.neighbors(node)` function already returns them in alphabetical order, so simply iterate through the list as returned.
- A path should be returned as a list of node names, e.g., `['Arad', 'Sibiu', 'Fagaras', 'Bucharest']`.
- If no path exists, return `None`.
- For A*, the cost of a path is the sum of the edge weights, which you can get using `graph.cost(from_node, to_node)`. The heuristic value for a node can be accessed via `heuristic[node]`.

### Testing Locally
You can run `python main.py` on your machine to test your algorithms against the classic AI Romania map.

Good luck!
