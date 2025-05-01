import random

def individual(length=200):
    return ''.join(str(random.randint(0, 1)) for _ in range(length))

def fitness(ind):
    return len([c for c in ind if c == '1'])

population = [individual() for _ in range(1000)]

def generation(pop):
    fitnesses = [fitness(i) for i in pop]
    return random.choices(pop, weights=fitnesses, k=len(pop))

def print_evaluation(pop):
    fitnesses = [fitness(i) for i in population]
    print(max(fitnesses))
    print(min(fitnesses))
    print(sum(fitnesses) / len(fitnesses))

print_evaluation(population)
for i in range(2000):
    population = generation(population)
print_evaluation(population)
