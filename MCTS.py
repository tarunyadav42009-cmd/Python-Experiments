import math
import random

class NumberGameState:
    """
    A simple game environment for testing MCTS.
    The goal is to reach exactly the number 10 by adding 1 or 2.
    If you hit 10, you win (1 point). If you go over, you lose (-1 point).
    """
    def __init__(self, current_sum=0):
        self.current_sum = current_sum

    def get_legal_actions(self):
        if self.is_terminal():
            return []
        return [1, 2]  # Available actions

    def is_terminal(self):
        return self.current_sum >= 10

    def take_action(self, action):
        return NumberGameState(self.current_sum + action)

    def get_reward(self):
        if self.current_sum == 10:
            return 1.0  # Perfect win
        else:
            return -1.0 # Lost (went over 10)


class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state          
        self.parent = parent        
        self.children = {}          
        self.visits = 0             
        self.value = 0.0            

    @property
    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_legal_actions())

    @property
    def is_terminal(self):
        return self.state.is_terminal()


class MCTS:
    def __init__(self, exploration_constant=1.414):
        self.c = exploration_constant  

    def search(self, root_state, iterations=500):
        root = MCTSNode(root_state)

        for _ in range(iterations):
            node = self._select_and_expand(root)
            reward = self._simulate(node.state)
            self._backpropagate(node, reward)

        if not root.children:
            return None, None
        
        # Corrected lambda function to read the node's visits property properly
        best_action, child_node = max(root.children.items(), key=lambda item: item[1].visits)
        return best_action, child_node

    def _select_and_expand(self, node):
        while not node.is_terminal:
            if not node.is_fully_expanded:
                return self._expand(node)
            else:
                node = self._best_uct_child(node)
        return node

    def _expand(self, node):
        legal_actions = node.state.get_legal_actions()
        for action in legal_actions:
            if action not in node.children:
                next_state = node.state.take_action(action)
                new_child = MCTSNode(next_state, parent=node)
                node.children[action] = new_child
                return new_child

    def _best_uct_child(self, node):
        best_score = float('-inf')
        best_child = None

        for child in node.children.values():
            exploitation = child.value / child.visits
            exploration = self.c * math.sqrt(math.log(node.visits) / child.visits)
            uct_score = exploitation + exploration

            if uct_score > best_score:
                best_score = uct_score
                best_child = child

        return best_child

    def _simulate(self, state):
        current_state = state
        while not current_state.is_terminal():
            actions = current_state.get_legal_actions()
            action = random.choice(actions)
            current_state = current_state.take_action(action)
        return current_state.get_reward()

    def _backpropagate(self, node, reward):
        while node is not None:
            node.visits += 1
            node.value += reward
            node = node.parent


if __name__ == "__main__":
    # Start the game at sum = 8. The best move should be 2 to hit 10 perfectly.
    starting_state = NumberGameState(current_sum=8)
    print(f"Starting game state sum: {starting_state.current_sum}")
    
    mcts_solver = MCTS()
    best_move, child_node = mcts_solver.search(starting_state, iterations=1000)
    
    print(f"MCTS calculated the best next move is: +{best_move}")
    print(f"Confidence (Visits to this path): {child_node.visits}/1000")
