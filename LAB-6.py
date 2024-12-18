class AlphaBetaPruning:
    def __init__(self, depth, game_state, player):
        self.depth = depth
        self.game_state = game_state
        self.player = player  
        self.nodes_evaluated = 0  

    def is_terminal(self, state):
        for i in range(3):
            if state[i].count('X') == 3 or [state[j][i] for j in range(3)].count('X') == 3:
                return 'X'  
            if state[i].count('O') == 3 or [state[j][i] for j in range(3)].count('O') == 3:
                return 'O'  
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != ' ':
            return state[0][0]  
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != ' ':
            return state[0][2]  
        if any(' ' in row for row in state):
            return None 
        return 'Draw'  
    def utility(self, state):
        result = self.is_terminal(state)
        if result == 'X':
            return 1 
        elif result == 'O':
            return -1  
        return 0  

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        self.nodes_evaluated += 1 

        if depth == 0 or self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':
                        state[i][j] = 'X'  
                        eval = self.alphabeta(state, depth - 1, alpha, beta, False)
                        state[i][j] = ' '  
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break  
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':
                        state[i][j] = 'O'  
                        eval = self.alphabeta(state, depth - 1, alpha, beta, True)
                        state[i][j] = ' '
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break  
            return min_eval

    def best_move(self):
        best_value = float('-inf')
        move = (-1, -1)  
        alpha = float('-inf')
        beta = float('inf')

        for i in range(3):
            for j in range(3):
                if self.game_state[i][j] == ' ':
                    self.game_state[i][j] = 'X' 
                    move_value = self.alphabeta(self.game_state, self.depth, alpha, beta, False)
                    self.game_state[i][j] = ' '  

                    if move_value > best_value:
                        best_value = move_value
                        move = (i, j)

        return move, self.nodes_evaluated

initial_state = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

alphabeta = AlphaBetaPruning(3, initial_state, 'X')
best_move, nodes_evaluated = alphabeta.best_move()

if best_move != (-1, -1):
    print(f"Best move for 'X': Row {best_move[0]}, Column {best_move[1]}")
    print(f"Nodes evaluated: {nodes_evaluated}")
else:
    print("No valid moves available.")