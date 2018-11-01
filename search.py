# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Actions
from game import Directions


class Node:

    def __init__(self, state, action, cost, parent):
      self.state = state
      self.action = action
      self.cost = cost
      self.parent = parent
    
    def __str__(self):
      return str(self.state) + ", " + str(self.action) + ", " + str(self.cost)

    def __eq__(self, node):
      return self.action == node.action and self.state == node.state and self.cost == node.cost

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

debug = False
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    frontier = util.Stack()
    return blindSearch(problem, frontier)
 
def blindSearch(problem, frontier):
  node = Node(problem.getStartState(), None, 0, None)
  frontier.push(node)
  explored = []
  while True:
    if frontier.isEmpty():
      print "ERROR in blindSearch function: frontier is empty!"
      return []
    node = frontier.pop()
    if(debug): print "Exploring node: ", node
    if(debug): raw_input("Press Enter to continue...")
    
    successors = problem.getSuccessors(node.state)
    if(debug): print "new successors:", successors
    for successor in successors:
      childNode = Node(successor[0], successor[1], node.cost + successor[2], node)
      if (childNode.state not in explored) and (childNode not in frontier.list) :
        if(problem.isGoalState(childNode.state)):
          return solution(childNode)
        frontier.push(childNode)
        if(debug): print "Child node pushed: ", childNode
      else:
        if(debug): print "Child node not pushed: ", childNode
        
    explored.append(node.state)

def solution(node):
  """
  returns an actions list represent a solution from initial node to goal state node.
  """
  actions = []
  while node != None and node.action != None:
    actions.append(node.action)
    node = node.parent
  actions.reverse()  
  return actions


    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    frontier = util.Queue()
    return blindSearch(problem, frontier)
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    node = Node(problem.getStartState(), None, 0, None)
    frontier.push(node, node.cost)
    explored = []
    while True:
      if frontier.isEmpty():
        print "ERROR in uniformCostSearch function: frontier is empty!"
        return []
      node = frontier.pop()
      if(debug): print "Exploring node: ", node
      if(debug): raw_input("Press Enter to continue...")
      
      successors = problem.getSuccessors(node.state)
      if(debug): print "new successors:", successors
      for successor in successors:
        childNode = Node(successor[0], successor[1], node.cost + successor[2], node)
        if not existsInPriorityQueue(frontier.heap, childNode) :
          if(problem.isGoalState(childNode.state)):
            return solution(childNode)
          if (childNode.state not in explored):
            frontier.push(childNode, node.cost)
          else:
            frontier.update(childNode, node.cost)
          if(debug): print "Child node pushed: ", childNode
        else:
          if(debug): print "Child node not pushed: ", childNode
          
      explored.append(node.state)

def existsInPriorityQueue(heap, item):
  """
  This is utility function that check if raw item exists in heapq (python class).
  """
  for heapItem in heap:
    if(heapItem[2] == item):
      return True
  return False


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
