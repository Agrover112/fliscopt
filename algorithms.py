import random
import sys
def random_search(domain, fitness_function,initial=[],epochs=10000):
  best_cost = sys.maxsize
  scores=[]
  if len(initial) > 0:
    solution = initial
  else:
    solution = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
  for i in range(epochs):
    if i!=0:
      solution = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
    cost=fitness_function(solution,'FCO')
    if cost< best_cost:
      best_cost=cost
      best_solution=solution
    scores.append(best_cost)
  return best_solution,best_cost,scores

def hill_climb(domain,fitness_function,initial=[],epochs=1000):
  count=0
  scores=[]
  if len(initial) > 0:
    solution = initial
  else:
    solution = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
  while True:
    neighbors=[]
    for i in range(len(domain)):
      if solution[i]>domain[i][0]:
        if solution[i]!=domain[i][1]: #cannot change value of 9 to 10
          neighbors.append(solution[0:i]+[solution[i]+1]+solution[i+1:])
      if solution[i]< domain[i][1]:
        if solution[i]!=domain[i][0]:
          neighbors.append(solution[0:i] + [solution[i] - 1] + solution[i + 1:])

    actual = fitness_function(solution,'FCO')
    best = actual
    for i in range(len(neighbors)):
      count += 1
      cost = fitness_function(neighbors[i],'FCO')
      if cost < best:
        best = cost
        solution = neighbors[i]
      scores.append(best)

    if best == actual:
      print('Count: ', count)
      break

  return solution,best,scores
    
