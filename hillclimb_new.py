import time
from nqueens_common import *


def get_lowest_heuristic_state(states):
    lowest_heuristic_state = states[0]
    lowest_heuristic_value = heuristic(states[0])
    for state in states:
        heuristic_value = heuristic(state)
        if heuristic_value < lowest_heuristic_value:
            lowest_heuristic_state = state
            lowest_heuristic_value = heuristic_value
    return lowest_heuristic_state, lowest_heuristic_value


def multi_steepest_ascent(number_of_episodes, number_of_queens):
    return multi(number_of_episodes, number_of_queens, steepest_ascent)


def at_least_one_solution_steepest_ascent(number_of_queens):
    return at_least_one(number_of_queens, steepest_ascent)


def steepest_ascent(number_of_queens):
    best_state = initialize(number_of_queens)
    last_heuristic_value = heuristic(best_state)
    step_counter = 0
    successful = False
    while True:
        if valid_state(best_state):
            successful = True
            break
        next_states = generate_next_states(best_state)
        best_state, best_value = get_lowest_heuristic_state(next_states)
        if best_value >= last_heuristic_value:
            break
        else:
            last_heuristic_value = best_value
            step_counter += 1
    return successful, step_counter, best_state


if __name__ == '__main__':
    n = int(input("Enter the number of Queens : "))
    ep = int(input("Enter the number of Episodes : "))
    start = time.time()
    number_of_queens = n
    number_of_episodes = ep
    metadata = multi_steepest_ascent(number_of_episodes, number_of_queens)
    end = time.time()
    parse_output(metadata)
    print("Total Time in seconds : " + str(end - start))
