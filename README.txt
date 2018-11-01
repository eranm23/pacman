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
	I use a stack as Node object container for DFS implementation LIFO.
	Solution path is calculated by method solution(node): which returns
	an actions list represent a solution from initial node to goal state node. this is done by accessing the parent node property of node.
	
   Explored order:
   The explore order is the opposite order (end to start) of PositionSearchProblem.getSuccessores method,
	Which is Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST.
	This is fit to the order shown as UI.
	
   This solution is not optimal since the successors order arbitrary and we use stack so the exploring is arbitrary also,
    this is mean a not optimal path can be chosen.


2. BFS implementaion:
	Same as DFS, except frontier is Util.queue.

   BFS algorithem is not optimal, becouse the push order is arbitray per EACH LEVEL and so is the pop out. 
   in case of cost is the same per each level, the solution will be optimal.
	