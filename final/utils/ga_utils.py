import random
def crossover(domain, solution_1, solution_2)  -> list:
    if len(domain)>2:
        gene = random.randint(1, len(domain) - 2)
    else: gene = random.randint(1, len(domain))
    return solution_1[0:gene] + solution_2[gene:]

def mutation(domain, step, solution) -> list:
    gene = random.randint(0, len(domain)-1)
    mutant = solution
    if random.random() < 0.5:
        if solution[gene] != domain[gene][0]:
            mutant = solution[0:gene]+[solution[gene]-step]+solution[gene+1:]
    else:
        if solution[gene] != domain[gene][1]:
            mutant = solution[0:gene]+[solution[gene]+step]+solution[gene+1:]
    return mutant

# No good results tbh( also doesn't work for benchmarks yet) #FIX-NEEDED
def multi_mutation(domain, step, solution) -> list:
    li = [i for i in range(domain[0][0], domain[0][1]+1)]
    gene = random.randint(0, len(domain)-1)
    if gene in li:
        li.remove(gene)
    gene2 = random.choice(li)
    mutant = solution
    if random.random() < 0.5:
        if solution[gene] != domain[gene][0]:
            mutant = solution[0:gene]+[solution[gene]-step]+solution[gene+1:]
    else:
        if solution[gene] != domain[gene][1]:
            mutant = solution[0:gene]+[solution[gene]+step]+solution[gene+1:]
    if random.random() < 0.5:
        if solution[gene2] != domain[gene2][0]:
            mutant = solution[0:gene2] + \
                [solution[gene2]-step]+solution[gene2+1:]
    else:
        if solution[gene2] != domain[gene2][1]:
            mutant = solution[0:gene2] + \
                [solution[gene2]+step]+solution[gene2+1:]

    return mutant


