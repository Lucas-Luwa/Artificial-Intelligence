# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    nextNodes = util.Stack()
    #Tuple needed here 
    nextNodes.push((problem.getStartState(), []))
    visitedSet = set()
    while not nextNodes.isEmpty():
        currNode = nextNodes.pop();
        if (currNode[0] not in visitedSet): 
            # print("hi")
            visitedSet.add(currNode[0])
            if (problem.isGoalState(currNode[0])):
                return currNode[1]
            # if not currNode[0] in visitedSet:
                #Marking node as visited
                # visitedSet.add(currNode[0])
            for nextVal in problem.getSuccessors(currNode[0]):
                # Contains successor
                if (not nextVal[0] in visitedSet):
                    nextNodes.push((nextVal[0], currNode[1] + [nextVal[1]]))
        # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    nextNodes = util.Queue()
    visitedSet = set()
    nextNodes.push((problem.getStartState(), []))
    # visitedSet.add(problem.getStartState())
    while not nextNodes.isEmpty():
        currNode = nextNodes.pop()
        if (currNode[0] not in visitedSet): 
            visitedSet.add(currNode[0])
            if (problem.isGoalState(currNode[0])):
                return currNode[1]
            for nextVal in problem.getSuccessors(currNode[0]):
                    if (not nextVal[0] in visitedSet):
                        # visitedSet.add(nextVal[0])
                        nextNodes.push((nextVal[0], currNode[1] + [nextVal[1]]))


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    nextNodes = util.PriorityQueue()
    visitedSet = set()
    nextNodes.push((problem.getStartState(), [], 0),0)
    # visitedSet.add(problem.getStartState())
    while not nextNodes.isEmpty():
        currNode = nextNodes.pop()
        if (currNode[0] not in visitedSet): 
            # print("hello")
            visitedSet.add(currNode[0])
            if (problem.isGoalState(currNode[0])):
                return currNode[1]
            for nextVal in problem.getSuccessors(currNode[0]):
                # print("in loop", nextVal[0])
                if (not nextVal[0] in visitedSet):
                    # print("im here", nextVal[0])
                    # visitedSet.add(nextVal[0])
                    nextNodes.push((nextVal[0], currNode[1] + [nextVal[1]], nextVal[2] + currNode[2]), nextVal[2] + currNode[2])
                # print(nextNodes.heap)



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    nextNodes = util.PriorityQueue()
    visitedSet = set()
    nextNodes.push((problem.getStartState(), [], 0),0)
    while not nextNodes.isEmpty():
        currNode = nextNodes.pop()
        # print(heuristic(currNode[0],problem))
        if (currNode[0] not in visitedSet): 
            visitedSet.add(currNode[0])
            if (problem.isGoalState(currNode[0])):
                return currNode[1]
            for nextVal in problem.getSuccessors(currNode[0]):
                if (not nextVal[0] in visitedSet):
                    #Additional heuristic feature added (really just adding heuristic to priority)
                    nextNodes.push((nextVal[0], currNode[1] + [nextVal[1]], 
                                    nextVal[2] + currNode[2]), 
                                    nextVal[2] + currNode[2] + heuristic(nextVal[0],problem))
    # util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
