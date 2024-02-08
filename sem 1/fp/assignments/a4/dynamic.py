"""
    Given an array of integers A, maximize the value of the expression A[m] - A[n] + A[p] - A[q], where m, n, p, q are
    array indices with m > n > p > q. For A = [30, 5, 15, 18, 30, 40], the maximum value is 32,
    obtained as 40 - 18 + 15 - 5. Display both the maximum value and the expression used to calculate it.
"""
import random


def generateRandomList(n: int) -> list:
    """
    Generates a list of random distinct numbers
    :param n: length of list
    :return: generated list
    """
    minListValue = 0
    maxListValue = 100

    randomList = []

    while len(randomList) < n:
        number = random.randint(minListValue, maxListValue)
        if number not in randomList:
            randomList.append(number)

    return randomList


def maximum_sum_naive(A: list):
    max_sum = 0
    for Q in range(len(A) - 3):
        for P in range(Q+1, len(A) - 2):
            for N in range(P+1, len(A) - 1):
                for M in range(N+1, len(A)):
                    if A[M] - A[N] + A[P] - A[Q] >= max_sum:
                        max_sum = A[M] - A[N] + A[P] - A[Q]
                        m, n, p, q = M, N, P, Q

    print(f"The maximum summ is {max_sum} = {A[m]} - {A[n]} + {A[p]} - {A[q]}")


def formatted(m: int, n: int, p: int, q: int, summ: int):
    s = "The maximum value is: {} = {} - {} + {} - {}"
    return s.format(summ, m, n, p, q)


def maximum_sum(A: list) -> tuple:
    length = len(A)
    if length < 4:
        raise ValueError("The list must contain at least four elements.")

    # initialize the lists with 0. max will hold the index of the maximum value to the right of all values in A
    maximum_value_index_right = [0] * length
    minimum_value_index_left = [0] * length

    minimum_value_index_left[0] = 0

    for i in range(1, length):
        min_index = 0
        for j in range(i):
            if A[j] < A[min_index]:
                min_index = j
        minimum_value_index_left[i] = min_index

    maximum_value_index_right[-1] = length - 1

    for i in range(length - 1):
        max_index = length - 1
        for j in range(i + 1, length):
            if A[j] > A[max_index]:
                max_index = j
        maximum_value_index_right[i] = max_index

    maximum_expression_value = float('-inf')
    maximum_expression = ""
    expression_indexes = (0, 0, 0, 0)

    # Print the max_value_to_the_right_of_index array
    print("maximum_value_index_right:")
    for i in range(length):
        print(f"{maximum_value_index_right[i]}", end=" ")

    print()

    # Print the min_value_to_the_left_of_index array
    print("minimum_value_index_left:")
    for i in range(length):
        print(f"{minimum_value_index_left[i]}", end=" ")

    print()

    for i in range(length - 1):
        for j in range(i + 1, length):
            if minimum_value_index_left[i] != i and maximum_value_index_right[j] != j:
                if minimum_value_index_left[i] != maximum_value_index_right[j] and minimum_value_index_left[i] != j and maximum_value_index_right[j] != i:
                    # minimum_value_index_left[i] != j, so I don't subtract the same element twice
                    # minimum_value_index_left[i] != maximum_value_index_right[j], so I don't add the element and then
                    # subtract it
                    # maximum_value_index_right[j] != i, so I don't add the same element twice
                    # m > n > p > q
                    expression_value = A[maximum_value_index_right[j]] - A[j] + A[i] - A[minimum_value_index_left[i]]

                    """
                    print(f"Values so far: {A[maximum_value_index_right[j]]}, {A[j]}, {A[i]}, {A[minimum_value_index_left[i]]}")
                    print(f"               {maximum_value_index_right[j]}, {j}, {i}, {minimum_value_index_left[i]}")
                    """

                    if expression_value > maximum_expression_value:
                        maximum_expression_value = expression_value
                        maximum_expression = formatted(A[maximum_value_index_right[j]], A[j], A[i], A[minimum_value_index_left[i]], maximum_expression_value)
                        expression_indexes = (maximum_value_index_right[j], j, i, minimum_value_index_left[i])

    return maximum_expression_value, maximum_expression, expression_indexes


if __name__ == "__main__":
    lista = generateRandomList(10)

    print(f"The list we're working with is {lista}")

    maximum_sum_naive(lista)
    print(maximum_sum(lista))
