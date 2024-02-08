"""
For the backtracking problem, implement both an iterative and a recursive algorithm

    The sequence a1, ..., an of -distinct- integer numbers is given.
    Display all subsets with a mountain aspect. A set has a mountain
    aspect if the elements increase up to a point and then they
    decrease. E.g. 10, 16, 27, 18, 14, 7.
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


def is_mountain(data: list) -> bool:
    """
    Teh function checks if the list provided has a mountain aspect or not
    :param data: given list
    :return: True is the list has a mountain aspect and False otherwise
    """
    # peak gets the index of the maximum element of a sequence
    # the max() function cannot be called on an empty list, therefore we first check if data has any elements
    if len(data):
        # index gets the index of the maximum element of data
        peak = data.index(max(data))

        # if peak is 0, it means that the first element is the maximum, therefore it cannot have a mountain aspect ->
        # we return False. Same goes for len(data) - 1, which means that the last element is the max
        if peak == 0 or peak == len(data) - 1:
            return False
    else:
        return False

    # we check for the fist part of the list to be sorted ascending, up to peak's index
    for i in range(peak):
        if data[i] > data[i + 1]:
            return False

    # we check for the last part of the list to be sorted descending, from peak's index to the end
    for i in range(peak, len(data) - 1):
        if data[i] < data[i + 1]:
            return False
    return True


def mountain_subset(data: list, res: list, sub: list, index: int):
    # T(n) = O(2^n * k)  aprox. O(2^n)
    if is_mountain(sub):
        res.append(list(sub))

    for i in range(index, len(data)):
        if data[i] not in sub or (data[i] > sub[-1] and is_mountain(sub + [data[i]])):
            sub.append(data[i])
            mountain_subset(data, res, sub, i + 1)
            sub.pop()


def subsets(data: list):
    """
    Generates all subsets of the data list
    :param data: list
    :return: the list containing all subsets
    """
    result = []
    mountain_subset(data, result, [], 0)
    return result


def mountain_iter(data: list):
    # time complexity: T(n) = O(2^n * k) where n is the length of the list and k is the length of each subset
    # space complexity: O(2^n)
    result = []
    length = len(data)

    # the number of all possible subsets of an array is 2^(len(data))
    total_subsets = 2 ** length

    for binary in range(0, total_subsets):
        subset = []
        for i in range(0, length):
            if (binary * 10 // (total_subsets // (2 ** i))) % 2:
                subset.append(data[i])
            """
            This condition checks if the i - th element should be included in the current subset.
                > (2 ** i) calculates a power of 2 corresponding to the index i, resulting in a number with only the 
                  i-th bit set to 1
                > total_subsets // (2 ** i) calculates a value that represents a divisor for binary, essentially scaling
                  the binary number to the same order as the elements in data
                > binary * 10 // (total_subsets // (2 ** i)) extracts the digit at position i from the binary representation 
                  of binary
                > (binary * 10 // (total_subsets // (2 ** i))) % 2 checks if the digit is 1, which determines whether the 
                  i-th element should be included in the current subset
            """
        if is_mountain(subset) and subset not in result:
            result.append(subset)

    return result


def mountain_iter_different(data: list):
    # T(n) = O(2^n * k)  aprox. O(2^n)
    result = []
    length = len(data)
    stack = [(0, [], 0)]

    while stack:
        index, subset, i = stack.pop()

        if is_mountain(subset):
            result.append(list(subset))

        while i < length:
            if data[i] not in subset or (data[i] > subset[-1] and is_mountain(subset + [data[i]])):
                subset.append(data[i])
                stack.append((index + 1, list(subset), i + 1))
                subset.pop()
            i += 1

    return result


if __name__ == "__main__":
    array = generateRandomList(6)
    # array = [10, 16, 27, 18, 14, 7]
    print(f"The original array is: {array}")
    res_recursive = subsets(array)
    res_iterative = mountain_iter_different(array)
    res_iterative_different = mountain_iter_different(array)

    print("------------- Recursive -------------")
    for sub in res_recursive:
        print(sub)
    print("------------- Iterative -------------")
    for subs in res_iterative:
        print(subs)
    print("------------- Iterative with stack -------------")
    for subs in res_iterative_different:
        print(subs)