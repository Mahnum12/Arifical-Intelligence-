#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

class PuzzleBFS:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        self.rows = 3
        self.cols = 3

    def print_board(self, board):
        for row in board:
            print(" ".join(str(x) if x != 0 else " " for x in row))
        print()

    def get_blank_position(self, board):
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == 0:
                    return i, j

    def is_goal(self, board):
        return board == self.goal

    def get_neighbors(self, board):
        neighbors = []
        blank_i, blank_j = self.get_blank_position(board)
        for move in self.moves:
            new_i, new_j = blank_i + move[0], blank_j + move[1]
            if 0 <= new_i < self.rows and 0 <= new_j < self.cols:
                new_board = [row[:] for row in board]
                new_board[blank_i][blank_j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[blank_i][blank_j]
                neighbors.append(new_board)
        return neighbors

    def bfs(self, start):
        queue = deque([(start, [])])
        visited = set()

        while queue:
            current_board, path = queue.popleft()

            if self.is_goal(current_board):
                return path

            visited.add(tuple(map(tuple, current_board)))

            for neighbor in self.get_neighbors(current_board):
                if tuple(map(tuple, neighbor)) not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None 

    def print_solution(self, solution):
        if solution is None:
            print("No solution found.")
        else:
            print("Initial State:")
            self.print_board(self.board)
            for idx, move in enumerate(solution):
                print(f"Step {idx + 1}:")
                self.print_board(move)
            print("Goal Reached!")


initial_board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

puzzle_bfs = PuzzleBFS(initial_board, goal_board)
bfs_solution = puzzle_bfs.bfs(initial_board)
print("BFS Solution:")
puzzle_bfs.print_solution(bfs_solution)

