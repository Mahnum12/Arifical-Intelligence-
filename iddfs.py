

class PuzzleIDDFS:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        self.rows = 3
        self.cols = 3

    

    def get_blank_position(self, board):
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == 0:
                    return i, j

    def is_goal(self, board):
        return board == self.goal


    def iddfs(self, start):
        def dls(board, depth, path, visited):
            if self.is_goal(board):
                return path
            if depth <= 0:
                return None

            visited.add(tuple(map(tuple, board)))

            for neighbor in self.get_neighbors(board):
                if tuple(map(tuple, neighbor)) not in visited:
                    result = dls(neighbor, depth - 1, path + [neighbor], visited)
                    if result:
                        return result

            visited.remove(tuple(map(tuple, board)))
            return None

        depth = 0
        while True:
            visited = set()
            result = dls(start, depth, [], visited)
            if result is not None:
                return result
            depth += 1

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

puzzle_iddfs = PuzzleIDDFS(initial_board, goal_board)
iddfs_solution = puzzle_iddfs.iddfs(initial_board)
print("IDDFS Solution:")
puzzle_iddfs.print_solution(iddfs_solution)

