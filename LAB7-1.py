import random

# Distance matrix (example with 5 cities)
distance_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 15],
    [25, 30, 5, 15, 0]
]

# Function to calculate the total distance of a tour
def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return total_distance

# Function to create an initial population of tours
def create_population(size):
    population = []
    for _ in range(size):
        tour = list(range(len(distance_matrix)))
        random.shuffle(tour)
        population.append(tour)
    return population

# Fitness function (inverse of distance)
def fitness(tour):
    return 1 / calculate_distance(tour)

# Selection (tournament selection)
def select(population):
    tournament = random.sample(population, 5)
    return max(tournament, key=fitness)

# Crossover (order crossover)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    
    current_pos = end % len(parent1)
    for city in parent2:
        if city not in child:
            child[current_pos] = city
            current_pos = (current_pos + 1) % len(parent1)
    
    return child

# Mutation (swap mutation)
def mutate(tour):
    idx1, idx2 = random.sample(range(len(tour)), 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

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
    
    best_tour = max(population, key=fitness)
    return best_tour, calculate_distance(best_tour)

# Run the genetic algorithm
best_tour, best_distance = genetic_algorithm(pop_size=100, generations=1000)
print("Best tour:", best_tour)
print("Best distance:", best_distance)