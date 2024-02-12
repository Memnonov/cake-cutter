"""
random_kakku_taster.py - Maistelee satunnaisia kakkuja.

    A random taster (pun intended) for testing the cake
    cutting algorithm.

    @Author: Mikko Memonen, 2024
"""

import random
import timeit
import cake
import cutter


# UNUSED
def get_random_cake_dimensions(max_size):
    """
    Return random cake dimensions based on max_size
    """
    return [random.randint(1, max_size), random.randint(1, max_size)]


def get_random_flowers(flower_amount, *cake_dimensions):
    """
    Return the given amount of randomly placed flowers in the
    given cake.
    """
    count = 0
    flowers_list = set()
    while count < flower_amount:
        flower = (
            random.randint(1, cake_dimensions[0]),
            random.randint(1, cake_dimensions[1]),
        )
        if flower not in flowers_list:
            flowers_list.add(flower)
            count += 1
    return flowers_list


if __name__ == "__main__":
    # Get input
    inp = input("anna alueen sivun koko\n > ")
    cake_w = cake_h = int(inp)
    inp = input("anna kukkien lukumäärä (nro)\ndefault --> 1/4 alueen alasta\n > ")
    try:
        flower_amount = int(inp)
    except ValueError:
        flower_amount = (cake_w * cake_h) // 4

    # Create cake
    flowers = get_random_flowers(flower_amount, cake_h, cake_w)
    random_cake = cake.Cake(cake_w, cake_h, flowers)
    print("start")
    random_cake.print_cake()

    # Ready, set, cut!
    start = timeit.default_timer()
    cutter.Cutter.cut_the_cake(random_cake)
    run_time = timeit.default_timer() - start

    # Done, print results
    print("end")
    random_cake.print_cake()
    random_cake.print_pieces()
    print("Took", run_time)
    print(f"dimensions: {random_cake.width}, {random_cake.height}")
    print("flowers", len(random_cake.flowers))
