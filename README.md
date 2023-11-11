# Graph Search Algorithms

## Project Overview

This project was conducted by the HCMUS at VNU-HCM. The main objectives were to research, implement, and present graph search algorithms. The algorithms implemented in this project include Breadth-First Search (BFS), Depth-First Search (DFS), Uniform Cost Search (UCS), and Astar(A*).

## Implementation Details

### Graph Representation

The graph is represented as a set of nodes, each with a unique value, position (x, y), and color. The start and goal nodes are specified at the initialization of the graph.

### Search Algorithms

1. **Breadth-First Search (BFS):**
    - Implemented in the `BFS` function.
    - Utilizes **a queue** (`open_set`) to explore nodes level by level.
    - Draws the explored path on the screen using different colors.

2. **Depth-First Search (DFS):**
    - Implemented in the `DFS` function.
    - Utilizes **a stack** (`open_set`) to explore nodes deeply before backtracking.
    - Draws the explored path on the screen using different colors.

3. **Uniform Cost Search (UCS):**
    - Implemented in the `UCS` function.
    - Utilizes a priority queue (`open_set`) based on the cost of reaching each node.
    - Draws the explored path on the screen using different colors.

4. **A*:**
    - Implemented in the `AStar` and `AStar_Search` functions.
    - Utilizes a combination of actual cost (`cost`) and heuristic (`Manhattan`) for node prioritization.
    - Draws the explored path on the screen using different colors.

### Node Class

The `Node` class represents individual nodes in the graph. It includes methods for drawing nodes, setting colors, and drawing lines between nodes.

### Graph Class

The `Graph` class represents the entire graph. It includes methods for getting neighbors, checking if a node is the goal, and drawing the entire graph.

## Usage

To run the program, use the following command:

```bash
python main.py --algo ALGORITHM --start START_POSITION --goal GOAL_POSITION
```

Replace `ALGORITHM` with the desired algorithm (`DFS`, `BFS`, `UCS`, or `AStar`), `START_POSITION` with the starting node's value, and `GOAL_POSITION` with the goal node's value.

## Dependencies

- Python 3.x
- Pygame library

Make sure to install the required dependencies before running the program. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Contributors

- Lam Nguyen Luu Phuong Ngoc
- Anh Trinh Minh

## License

This project is licensed under the [MIT License](LICENSE). Feel free to contribute and share!
