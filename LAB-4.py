

class PuzzleNode:
    def __init__(self, state, parent, move, g_cost, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    def generate_children(self):
        children = []
        for i in range(9):
            if self.state[i] == 0:
                for j in [(i-3), (i+3), (i-1), (i+1)]:
                    if 0 <= j < 9 and abs(i-j) in [1, 3]:
                        new_state = list(self.state)
                        new_state[i], new_state[j] = new_state[j], new_state[i]
                        children.append(PuzzleNode(new_state, self, (i, j), self.g_cost + 1, 0))
        return children

    def calculate_heuristic(self, goal_state):
        self.h_cost = sum([abs(self.state.index(i) - goal_state.index(i)) for i in range(1, 9)])
        self.f_cost = self.g_cost + self.h_cost

class AStarSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.open_list = []
        self.closed_list = []

    def solve(self):
        start_node = PuzzleNode(self.start_state, None, None, 0, 0)
        start_node.calculate_heuristic(self.goal_state)
        self.open_list.append(start_node)

        while self.open_list:
            current_node = min(self.open_list, key=lambda x: x.f_cost)
            self.open_list.remove(current_node)
            self.closed_list.append(current_node)

            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            for child in current_node.generate_children():
                child.calculate_heuristic(self.goal_state)
                if child.state not in [node.state for node in self.closed_list]:
                    self.open_list.append(child)

        return None

    def trace_solution(self, node):
        solution = []
        while node:
            solution.append(node.state)
            node = node.parent
        return solution[::-1]

    def is_solvable(self, state):
        inversions = 0
        for i in range(9):
            for j in range(i+1, 9):
                if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                    inversions += 1
        return inversions % 2 == 0


start_state = [1, 2, 3, 4, 0 , 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solver = AStarSolver(start_state, goal_state)
if solver.is_solvable(start_state):
    solution = solver.solve()
    if solution:
        print("Solution in states:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")
else:
    print("Puzzle is not solvable.")
