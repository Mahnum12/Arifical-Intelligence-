import random

# Define items as (weight, value) tuples
items = [
    (2, 3),  # Item 1: weight 2, value 3
    (3, 4),  # Item 2: weight 3, value 4
    (4, 5),  # Item 3: weight 4, value 5
    (5, 6)   # Item 4: weight 5, value 6
]

weight_limit = 5  # Maximum weight the knapsack can carry

# Function to calculate the total value and weight of a solution
def calculate_value_weight(solution):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i]:  # If the item is included
            total_weight += items[i][0]
            total_value += items[i][1]
    return total_value, total_weight

# Function to create an initial population of solutions
def create_population(size):
    population = []
    for _ in range(size):
        # Each solution is a binary list indicating whether to include each item
        solution = [random.choice([0, 1]) for _ in range(len(items))]
        population.append(solution)
    return population

# Fitness function (value if within weight limit, else 0)
def fitness(solution):
    value, weight = calculate_value_weight(solution)
    return value if weight <= weight_limit else 0

# Selection (select the best solution)
def select(population):
    return max(population, key=fitness)

# Crossover (single-point crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child

# Mutation (bit-flip mutation)
def mutate(solution):
    idx = random.randint(0, len(solution) - 1)
    solution[idx] = 1 - solution[idx]  # Flip the bit

# Genetic Algorithm
def genetic_algorithm(pop_size, generations):
    population = create_population(pop_size)
    
    for _ in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # Mutation probability
                mutate(child)
            new_population.append(child)
        population = new_population
    
    best_solution = select(population)
    best_value, best_weight = calculate_value_weight(best_solution)
    return best_solution, best_value, best_weight

# Run the genetic algorithm
best_solution, best_value, best_weight = genetic_algorithm(pop_size=100, generations=1000)
print("Best solution (include items):", best_solution)
print("Total value:", best_value)
print("Total weight:", best_weight)