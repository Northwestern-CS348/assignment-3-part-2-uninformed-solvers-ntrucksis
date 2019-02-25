
from solver import *

class SolverDFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Depth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here
        curr = self.currentState
        if (curr not in self.visited):
            self.visited[curr] = True
            if (curr.state == self.victoryCondition):
                return True
            if curr.nextChildToVisit == 0:
                for move in self.gm.getMovables():
                    self.gm.makeMove(move)
                    new_GameState = GameState(self.gm.getGameState(), curr.depth+1, move)
                    if new_GameState not in self.visited:
                        new_GameState.parent = self.currentState
                        curr.children.append(new_GameState)
                    self.gm.reverseMove(move)
            elif curr.nextChildToVisit < len(curr.children):
                child = curr.children[curr.nextChildToVist]
                self.currentState.nextChildToVisit += 1
                self.gm.makeMove(child.requiredMovable)
                self.currentState = child
                return self.solveOneStep()
            else:    
                self.currentState.nextChildToVisit += 1
                self.gm.reverseMove(curr.requiredMovable)
                self.currentState = curr.parent
                return self.solveOneStep()

            
                
                
        


class SolverBFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Breadth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here
        return True
