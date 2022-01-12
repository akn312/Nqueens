import time
from scipy import special as sc
import itertools
from nqueens_common import *

POPULATION_SIZE = 100
MIXING_NUMBER = 2
MUTATION_RATE = 0.05


def fitness(chromosome):
    return int(get_number_of_attacks(buildastate(nq, chromosome)))


def buildastate(chromosome):
    board = []
    for x in range(nq):
        board.append([0] * nq)
    nparray = np.array(board)
    for i in range(nq):
        nparray[nq - 1 - chromosome[i]][i] = 1
    return nparray


def multi_genetic_algo(number_of_episodes, number_of_queens):
    return multi(number_of_episodes, number_of_queens, genetic_main_call)


def fitness_score(seq):
    score = 0

    for row in range(nq):
        col = seq[row]

        for other_row in range(nq):

            # queens cannot pair with itself
            if other_row == row:
                continue
            if seq[other_row] == col:
                continue
            if other_row + seq[other_row] == row + col:
                continue
            if other_row - seq[other_row] == row - col:
                continue
            # score++ if every pair of queens are non-attacking.
            score += 1

    # divide by 2 as pairs of queens are commutative
    return score / 2


def selection(population):
    parents = []

    for ind in population:
        # select parents with probability proportional to their fitness score
        if random.randrange(sc.comb(nq, 2) * 2) < fitness_score(ind):
            parents.append(ind)

    return parents


def crossover(parents):
    # random indexes to cross states with
    cross_points = random.sample(range(nq), MIXING_NUMBER - 1)
    offsprings = []

    # all permutations of parents
    permutations = list(itertools.permutations(parents, MIXING_NUMBER))

    for perm in permutations:
        offspring = []

        # track starting index of sublist
        start_pt = 0

        for parent_idx, cross_point in enumerate(cross_points):  # doesn't account for last parent

            # sublist of parent to be crossed
            parent_part = perm[parent_idx][start_pt:cross_point]
            offspring.append(parent_part)

            # update index pointer
            start_pt = cross_point

        # last parent
        last_parent = perm[-1]
        parent_part = last_parent[cross_point:]
        offspring.append(parent_part)

        # flatten the list since append works kinda differently
        offsprings.append(list(itertools.chain(*offspring)))

    return offsprings


def mutate(seq):
    for row in range(len(seq)):
        if random.random() < MUTATION_RATE:
            seq[row] = random.randrange(nq)
    return seq


def print_found_goal(population, to_print=True):
    for idx, ind in enumerate(population):
        score = fitness_score(ind)
        # if to_print:
        #    print(f'{ind}. Score: {score}')
        if score == sc.comb(nq, 2):
            if to_print:
                print('Solution found')
                print(f'{ind}. Score: {score}')
            return True
    return False


def evolution(population):
    # select individuals to become parents
    parents = selection(population)

    # recombination. Create new offsprings
    offsprings = crossover(parents)

    # mutation
    offsprings = list(map(mutate, offsprings))

    # introduce top-scoring individuals from previous generation and keep top fitness individuals
    new_gen = offsprings

    for ind in population:
        new_gen.append(ind)

    new_gen = sorted(new_gen, key=lambda ind: fitness_score(ind), reverse=True)[:POPULATION_SIZE]

    return new_gen


def generate_population():
    population = []

    for individual in range(POPULATION_SIZE):
        new = [random.randrange(nq) for idx in range(nq)]
        population.append(new)

    return population


def genetic_main_call(nq):
    # Running the experiment
    generation = 0
    successful = False
    population = generate_population()
    ind0 = []

    while not print_found_goal(population):
        print(f'Generation: {generation}')
        print_found_goal(population)
        population = evolution(population)
        generation += 1

    for idx, ind in enumerate(population):
        score = fitness_score(ind)
        if score == sc.comb(nq, 2):
            ind0 = ind.copy()
            successful = True
            break

    return successful, generation, buildastate(ind0)


if __name__ == "__main__":
    maxFitness = 0
    nq = int(input("Enter Number of Queens: "))  # say N = 8
    ep = int(input("Enter Number of Episodes: "))  # say Episodes = 2, keep it small (ex: 1 )for high number of queens
    start = time.time()
    metadata = multi_genetic_algo(ep, nq)
    end = time.time()
    parse_output(metadata)
    print("Total Time in seconds : " + str(end - start))
