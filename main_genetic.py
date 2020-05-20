import time
from generation import Generation


if __name__ == '__main__':
    print('Looking for a solution...')
    start_time = time.time()

    # Make the first generation
    next_generation = Generation()

    # Continue to generate generations until we find the solution
    while not next_generation.found_solution():
        next_generation = next_generation.get_next_generation()

    print('Solution Found in {}s'.format(round(time.time() - start_time, 2)))

    # Show the solution
    next_generation.get_fittest().show()
    Generation.show_result_graph()
