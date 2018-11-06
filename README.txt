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

5. Corners Problem

	State is location and not visited corners location list : (location, notVisitedCornerList)
    Start state is start location and all corners list
    Goul state is any location and empty corner list, meanning all corner visited.

	When exploring node, if location is one of the NV corners, we remove the corner from the NV corners list.

6. Heuristic calculation:
        summary the manhattan distances from current location to nearest corner, and from this corner the next colset corner and so on.
        this value will be shorter path, since in our problem we have also walls inside the maze, the actual path will be equal or greater from this value.
        Therefore this is an admissible heuristic.

7. Food Search Heuristic:
	For each food map of current state we will find all corners. 
	Number of corners can be greater from 4, example belowe:
	
		  X	
	Xx    x  xX
	xx
       x   x
	X    x      X
	    Xx    X 


	X x xxx X
	 xxx   X 
	xxX
	X




	   X      x  X
	X        x
	xxxx  xx       X
	X

	findCorners function:
		function accept list of x,y tuples of foodLocation, the list should be ordered accending by x 
    	and then accending by y, for example: (1,1) (1,3) (1,7) (2,1) (2,2) (3,1) (3,3) (3,4).
    	and return a list of corners from the food list.

	

		first we scanning columns start from left column and go right for searching corners,
    	we sacn until we reach column with no corners.

		now ,  scanning columns from right column and go left and find corners of the other columns,
    	scan is stops when we reach column already has corner (from first scan).

		after we have corners of the food list we use the same heuristic function as in corner problem see 6 above. that heristic still be addmisible 
		becouse the we do it only on corners and ignoreing the inner food if exist, whitch means actual cost can be greater but no less.


	8. finding closest food was done by first finding the goal, I use findClosetManhattanDistance(locationList, currentLocation).
		Function get list of x,y tuples of locations and current loction (x,y) tuple as parameters
    	and return tuple of closet location and its manhatten distance from current location
		
		This function already use in corners problem and in food search problem, but now location list is all food list and not just corners as in other previos usages.
	