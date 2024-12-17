class Node:
    def __init__(self, state, parent, move, h_cost):
        self.state = state            
        self.parent = parent         
        self.move = move              
        self.h_cost = h_cost          
        self.zero_position = self.find_zero()  

    def find_zero(self):

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)

    def generate_children(self):

        children = []
        x, y = self.zero_position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:  
                new_state = [row[:] for row in self.state] 
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                h_cost = self.calculate_heuristic(new_state)
                children.append(Node(new_state, self, (new_x, new_y), h_cost))
        return children

    def calculate_heuristic(self, goal_state):
        h_cost = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:  
                    goal_x = (self.state[i][j] - 1) // 3
                    goal_y = (self.state[i][j] - 1) % 3
                    h_cost += abs(i - goal_x) + abs(j - goal_y)
        return h_cost


class GreedyBestFirstSearch:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.open_list = [] 
        self.closed_list = set()  

    def solve(self):

        start_node = Node(self.start_state, None, None, 0)
        self.open_list.append(start_node)

        while self.open_list:
            self.open_list.sort(key=lambda node: node.h_cost)
            current_node = self.open_list.pop(0)  

            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            self.closed_list.add(tuple(map(tuple, current_node.state)))  


            for child in current_node.generate_children():
                if tuple(map(tuple, child.state)) not in self.closed_list:
                    self.open_list.append(child)

        return None  

    def trace_solution(self, node):

        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1] 


start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

gbfs = GreedyBestFirstSearch(start_state, goal_state)
solution_path = gbfs.solve()

if solution_path:
    for step in solution_path:
        for row in step:
            print(row)
        print("->")  
else:
    print("No solution found.")