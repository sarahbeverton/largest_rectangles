
__author__ = "Sarah Beverton"

import itertools


def main():
    """Generates a list of tuples of (width, height) from 2-9 
    in descending order based on enclosed area"""
    one_side = [2, 3, 4, 5, 6, 7, 8, 9]
    sides = list(itertools.combinations_with_replacement(one_side, 2))
    areas = sorted(sides, key=lambda x: (x[0]-1)*(x[1]-1), reverse=True)
    print(areas)
    return areas


if __name__ == '__main__':
    main()
