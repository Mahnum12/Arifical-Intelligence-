import random

def initialize_population(pop_size, string_length):
    return [''.join(random.choice('01') for _ in range(string_length)) for _ in range(pop_size)]

def calculate_fitness(individual):
    return individual.count('1')

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    selection_probs = [f / total_fitness for f in fitness_scores]
    
    parent1 = random.choices(population, weights=selection_probs, k=1)[0]
    parent2 = random.choices(population, weights=selection_probs, k=1)[0]
    
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring = parent1[:crossover_point] + parent2[crossover_point:]
    return offspring

def mutate(individual, mutation_rate):
    mutated_individual = []
    for bit in individual:
        if random.random() < mutation_rate:
            mutated_individual.append('1' if bit == '0' else '0')  
        else:
            mutated_individual.append(bit)  
    return ''.join(mutated_individual)

def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    generation_summary = []

    for generation in range(num_generations):
        
        fitness_scores = [calculate_fitness(individual) for individual in population]

        
        if max(fitness_scores) == string_length:
            print(f"Optimal solution found in generation {generation}: {population[fitness_scores.index(max(fitness_scores))]}")
            break

    
        if generation <= 10:
            best_fitness = max(fitness_scores)
            best_individual = population[fitness_scores.index(best_fitness)]
            generation_summary.append((generation, best_fitness, best_individual))

        
        new_population = []
        for _ in range(pop_size // 2):  
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            new_population.append(mutate(offspring1, mutation_rate))
            new_population.append(mutate(offspring2, mutation_rate))

        population = new_population

        if generation % 10 == 0 or generation == num_generations - 1:
            best_fitness = max(fitness_scores)
            best_individual = population[fitness_scores.index(best_fitness)]
            print(f"Generation {generation}: Best fitness = {best_fitness}, Best individual = {best_individual}")

    final_fitness_scores = [calculate_fitness(individual) for individual in population]
    best_individual = population[final_fitness_scores.index(max(final_fitness_scores))]
    print(f"Best individual after {num_generations} generations: {best_individual} with {calculate_fitness(best_individual)} ones")

    print("\nSummary of generations 0 to 10:")
    for gen, fitness, individual in generation_summary:
        print(f"Generation {gen}: Best fitness = {fitness}, Best individual = {individual}")


if __name__ == "__main__":
    
    string_lengths = [10] 
    population_sizes = [20]  
    mutation_rates = [0.01]  

    for string_length in string_lengths:
        for pop_size in population_sizes:
            for mutation_rate in mutation_rates:
                print(f"\nRunning Genetic Algorithm with string_length={string_length}, pop_size={pop_size}, mutation_rate={mutation_rate}")
                genetic_algorithm(string_length, pop_size, num_generations=50, mutation_rate=mutation_rate)