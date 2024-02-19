from itertools import product, combinations, permutations
import numpy as np


def num_of_bases(n):
    """
    This function calculates the number of bases of the vector space Z_2^n over Z_2
    with the following formula: 2^n - 2^i, where i = 0, 1, ..., n-1
    """
    result = 1
    for i in range(n):
        result *= (2**n-2**i)
    return result


def generate_bases(n):
    # vectors generates a list of tuples that include all possible vectors of length n
    vectors = list(product([0, 1], repeat=n))
    bases = []

    for r in range(1, n + 1):
        for combo in permutations(vectors, r):
            # a loop that iterates over all combinations of vectors taken r at a time from the list vectors
            # for example, if vectors is [(0, 0), (0, 1), (1, 0), (1, 1)] and r is 2 => combinations(vectors, r):
            # [(0, 0), (0, 1)]
            # [(0, 0), (1, 0)]
            # [(0, 0), (1, 1)]
            # [(0, 1), (1, 0)]
            # [(0, 1), (1, 1)]
            # [(1, 0), (1, 1)]
            basis = []
            for vector in combo:
                basis.append(list(vector))

            # checks is the basis is linearly independent and if the number of generators is equal with n (power of Z2)
            if is_linearly_independent(basis, n):
                bases.append(basis)

    return bases


def is_linearly_independent(vectors, n):
    # this modified version of "is_linearly_independent" checks the determinant of the matrix formed by the generators
    # to be different from 0
    result = []
    to_check = list(permutations(vectors, n))
    for vect in to_check:
        det = np.linalg.det(vect)
        if det % 2:
            result.append(vect)

    return result


def write_bases_to_file(filename, bases, n):
    with open(filename, 'w') as file:
        file.write("")
        file.write("------------------------------------------------")
        file.write(f"\nVector Space Z2^{n} over Z2:\n")
        file.write(f"Number of vectors: {2 ** n}\n")
        file.write(f"Dimension: {n}\n")
        file.write(f"Number of bases: {num_of_bases(n)}\n")
        file.write("------------------------------------------------")
        file.write("")
        if 0 < n < 5:
            for i, basis in enumerate(bases, 1):
                file.write(f"\nBasis {i}:\n")
                for vector in basis:
                    file.write(str(vector) + '\n')


def write_bases_to_file_short(filename, n):
    with open(filename, 'w') as file:
        file.write("")
        file.write("------------------------------------------------")
        file.write(f"\nVector Space Z2^{n} over Z2:\n")
        file.write(f"Number of vectors: {2 ** n}\n")
        file.write(f"Dimension: {n}\n")
        file.write(f"Number of bases: {num_of_bases(n)}\n")
        file.write("------------------------------------------------")
        file.write("")


def print_bases_and_count(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        n = int(file.readline().strip())

    if 0 < n < 5:
        bases = generate_bases(n)
        write_bases_to_file(output_filename, bases, n)

        print("Bases written to", output_filename)
    else:
        print("The value of n is too high to generate all bases.")
        write_bases_to_file_short(output_filename, n)


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    print_bases_and_count(input_filename, output_filename)
