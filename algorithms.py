import math
import random
import sys
import heapq

def random_search(domain, fitness_function, init=[], epochs=100):

    best_cost = sys.maxsize
    scores = []
    if len(init) > 0:
        solution = init
    else:
        solution = [random.randint(domain[i][0], domain[i][1])
                    for i in range(len(domain))]
    for i in range(epochs):
        if i != 0:
            solution = [random.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]
        cost = fitness_function(solution, 'FCO')
        if cost < best_cost:
            best_cost = cost
            best_solution = solution
        scores.append(best_cost)
    return best_solution, best_cost, scores


def hill_climb(domain, fitness_function, init=[], epochs=100):
    count = 0
    scores = []
    if len(init) > 0:
        solution = init
    else:
        solution = [random.randint(domain[i][0], domain[i][1])
                    for i in range(len(domain))]
    while True:
        neighbors = []
        for i in range(len(domain)):
            if solution[i] > domain[i][0]:
                if solution[i] != domain[i][1]:  # cannot change value of 9 to 10
                    neighbors.append(
                        solution[0:i]+[solution[i]+1]+solution[i+1:])
            if solution[i] < domain[i][1]:
                if solution[i] != domain[i][0]:
                    neighbors.append(
                        solution[0:i] + [solution[i] - 1] + solution[i + 1:])

        actual = fitness_function(solution, 'FCO')
        best = actual
        for i in range(len(neighbors)):
            count += 1
            cost = fitness_function(neighbors[i], 'FCO')
            if cost < best:
                best = cost
                solution = neighbors[i]
            scores.append(best)

        if best == actual:
            print('Count: ', count)
            break

    return solution, best, scores


def simulated_annealing(domain, fitness_function, init=[], temperature=50000.0, cooling=0.95, step=1):
    count = 0
    scores = []
    simulated_annealing.temp = []

    if len(init) > 0:
        solution = init
    else:
        solution = [random.randint(domain[i][0], domain[i][1])
                    for i in range(len(domain))]

    while temperature > 0.1:
        i = random.randint(0, len(domain) - 1)
        direction = random.randint(-step, step)
        temp_solution = solution[:]
        temp_solution[i] += direction
        if temp_solution[i] < domain[i][0]:
            temp_solution[i] = domain[i][0]
        elif temp_solution[i] > domain[i][1]:
            temp_solution[i] = domain[i][1]

        count += 1
        cost = fitness_function(solution, 'FCO')
        cost_temp = fitness_function(temp_solution, 'FCO')
        prob = pow(math.e, (-cost_temp - cost) / temperature)
        best = cost
        if (cost_temp < cost or random.random() < prob):
            best = cost_temp
            solution = temp_solution
        scores.append(best)

        temperature = temperature * cooling
        simulated_annealing.temp.append(temperature)

    print('Count: ', count)
    return solution, best, scores


def mutation(domain,step,solution):
  gene=random.randint(0,len(domain)-1)
  mutant=solution
  if random.random() < 0.5:
    if solution[gene] !=domain[gene][0]:
      mutant=solution[0:gene]+[solution[gene]-step]+solution[gene+1:]
  else:
      if solution[gene] !=domain[gene][1]:
        mutant=solution[0:gene]+[solution[gene]+step]+solution[gene+1:]
  return mutant

def crossover(domain,solution_1,solution_2):
  gene = random.randint(1, len(domain) - 2)
  return solution_1[0:gene] + solution_2[gene:]

def genetic_algorithm(domain, fitness_function,init=[], population_size = 100, step = 1,
            probability_mutation = 0.2, elitism = 0.2,
            number_generations = 500, search = False):
  population = []
  scores=[]
  for i in range(population_size):
    if search == True:
      solution = random_search(domain, fitness_function)
    if len(init)>0:
        solution=init
    else:
      solution = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
    
    population.append(solution)

  number_elitism = int(elitism * population_size)

  for i in range(number_generations):
    costs = [(fitness_function(individual,'FCO'), individual) for individual in population]
    #costs.sort()
    heapq.heapify(costs)
    ordered_individuals = [individual for (cost, individual) in costs]
    population = ordered_individuals[0:number_elitism]
    scores.append(fitness_function(population[0],'FCO'))
    while len(population) < population_size:
      if random.random() < probability_mutation:
        m = random.randint(0, number_elitism)
        population.append(mutation(domain, step, ordered_individuals[m]))
      else:
        i1 = random.randint(0, number_elitism)
        i2 = random.randint(0, number_elitism)
        population.append(crossover(domain, ordered_individuals[i1], ordered_individuals[i2]))
  return costs[0][1],costs[0][0],scores