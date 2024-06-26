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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    #Prohledávání do hloubky (depth-first search) vždy prohledává prvního následníka každého uzlu, pokud jej ještě nenavštívil. 
    #Pokud narazí na uzel, z nějž už nelze dále pokračovat (nemá žádné následníky nebo byli všichni navštíveni), vrací se zpět backtrackingem.
    #Pro prohledávání do hloubky se používá zásobník.

    # využijeme předdefinovaný zásobník pro uložení uzlů při procházení stromu
    stack = util.Stack()

    visitedNodes = [] #sem budeme ukládat navštívené nody

    # startovací uzel = (počátečný stav, [pole akcí])
    startNode = (problem.getStartState(), [])

    stack.push(startNode)

    while stack:
        currentNode, actions = stack.pop()

        #ověříme, zda jsme uzel již nenavštívili, případně přidáme do navštívených
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            #pokud jsme našli cílový stav, vrátíme pole akcí a končíme
            if problem.isGoalState(currentNode):
                return actions 
            
            #přidáme následníky do zásobníku
            for successor in problem.getSuccessors(currentNode):
                successorState, successorAction, successorCost = successor
                nextActions = actions + [successorAction]
                nextNode = (successorState, nextActions)
                stack.push(nextNode)
    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Prohledávání do šířky nejprve projde všechny sousedy startovního uzlu, pak sousedy sousedů atd.
    # Každý uzel navštívíme nejvýše jednou.

    # využijeme předdefinovanou frontu pro uložení uzlů při procházení stromu
    queue = util.Queue()

    visitedNodes = [] #sem budeme ukládat navštívené nody

    # startovací uzel = (počátečný stav, [pole akcí])
    startNode = (problem.getStartState(), [])

    queue.push(startNode)

    while queue:
        currentNode, actions = queue.pop()

        #ověříme, zda jsme uzel již nenavštívili, případně přidáme do navštívených
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            #pokud jsme našli cílový stav, vrátíme pole akcí a končíme
            if problem.isGoalState(currentNode):
                return actions 
            
            #přidáme následníky do fronty
            for successor in problem.getSuccessors(currentNode):
                successorState, successorAction, successorCost = successor
                nextActions = actions + [successorAction]
                nextNode = (successorState, nextActions)
                queue.push(nextNode)
    return None
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Prohledávání se stejnoměrnou cenou.
    #Uzly následníků jsou uspořádany ve frontě s prioritou podle nižší ceny přechodu k následníkovi a v tomto pořadí je procházíme.

    # využijeme předdefinovanou frontu (viz utils.py) pro uložení uzlů při procházení stromu
    """
      PriorityQueue implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    queue = util.PriorityQueue()

    visitedNodes = [] #sem budeme ukládat navštívené nody

    # startovací uzel = (počátečný stav, [pole akcí], cena)
    startNode = (problem.getStartState(), [], 0)

    queue.push(startNode, 0)

    while queue:
        currentNode, actions, currentCost = queue.pop()

        #ověříme, zda jsme uzel již nenavštívili, případně přidáme do navštívených
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            #pokud jsme našli cílový stav, vrátíme pole akcí a končíme
            if problem.isGoalState(currentNode):
                return actions 
            
            #přidáme následníky do fronty
            for successor in problem.getSuccessors(currentNode):
                successorState, successorAction, successorCost = successor
                nextActions = actions + [successorAction]
                #zjistíme cenu dalšího uzlu
                nextCost = problem.getCostOfActions(nextActions)
                nextNode = (successorState, nextActions, nextCost)
                queue.push(nextNode, nextCost)
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # První v tomto příkladu infromované (heuristické) prohledávání

    # využijeme předdefinovanou frontu (viz utils.py) pro uložení uzlů při procházení stromu
    """
      PriorityQueue implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    queue = util.PriorityQueue()

    visitedNodes = [] #sem budeme ukládat navštívené nody

    # startovací uzel = (počátečný stav, [pole akcí], cena)
    startNode = (problem.getStartState(), [])
    # spočítáme heuristiku výchozího uzlu
    startHeuristic = heuristic(problem.getStartState(), problem)

    queue.push(startNode, startHeuristic)

    while queue:
        currentNode, actions = queue.pop()

        #ověříme, zda jsme uzel již nenavštívili, případně přidáme do navštívených
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            #pokud jsme našli cílový stav, vrátíme pole akcí a končíme
            if problem.isGoalState(currentNode):
                return actions 
            
            #přidáme následníky do fronty
            for successor in problem.getSuccessors(currentNode):
                successorState, successorAction, successorCost = successor
                nextActions = actions + [successorAction]
                #zjistíme cenu dalšího uzlu a přičteme k tomu vypočtenou pomocí funkce heuristiku
                nextCost = problem.getCostOfActions(nextActions) + heuristic(successorState, problem)
                nextNode = (successorState, nextActions)
                queue.push(nextNode, nextCost)
    return None

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
