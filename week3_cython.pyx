import time


def sum_quadrant():
    quadrant_list = []
    for i in range(1, 10000):
        quadrant_list += [(1/(i**2))]

    return sum(quadrant_list)

def run():
    start_time = time.time()
    for i in range(500):
        sum_quadrant()
    print("It took %s seconds to compute the sum 500 times." % (time.time() - start_time))


if "__main__" == __name__:
    run()