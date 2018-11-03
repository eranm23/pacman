==============
Eran Meshulam 
ID:033957952
==============
==============
Maman 11
==============
1. DFS implementation:
	New class named 'Node' created with state, action, cost and parent node as properties.
	Parent node is the previous node which current node his successor.
	I implemented function called blindSearch that take data structure (Stack in this case for DFS) as parameter
	Solution path is calculated by method solution(node): which returns
	an actions list represent a solution from initial node to goal state node. this is done by accessing the parent node property of node.
	
   Explored order:
   The explore order is the opposite order (end to start, due to LIFO behavoir of Stack) of PositionSearchProblem.getSuccessores method,
	Which is Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST.
	This is fit to the order shown as UI.
	
   This solution is not optimal since the successors order arbitrary and we use stack so the exploring is arbitrary also,
    this is mean a not optimal path can be chosen.


2. BFS implementaion:
	use blindSreach with with Util.queue as parameter.

   BFS algorithem is not optimal, becouse the push order is arbitray per EACH LEVEL and so is the pop out (FIFO). 
   in case of cost is the same per each level, the solution will be optimal.


3. aStarSearch function inplemented with heuristic function as parameter, for UCS is used nullHeuristic methos
	with always return 0, so F = g(n) as for UCS.

4. Same aStarSearch function used as in q. 3, but with menhattan heuristic.

	When we use openMaze in most of the time all actions is allowed, which means in general we 
	will explore more nodes comparing mazes with walls.
	BFS, UCS explore same amount of nodes, because the cost of all action is 1 and therefore pop order was the same.
	The soltion is the same for the two of them but only becouse BFS 'got lacky', meaning with diffenet getSuccessores order BFS can return not optimal solution.
	AStar with menhattan explore less nodes then UCS since it explore 'better' seccessor first.
	DFS explore less node the BFS/UCS but more then Astar, but solution cose was the greater comparing all others,
	its look like pacman scan the maze for east to west until it get to the goal, and this is because the order of getSuccessores
	first east/west and then north/south.

5.
