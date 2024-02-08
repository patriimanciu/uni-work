import random


def print_menu():
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("1. Generate a list of n random natural numbers between 0 and 100.")
    print("2. Sort the list using the cocktail sort.")
    print("3. Sort the list using the comb sort.")
    print("0. Exit the program!")
    print("")
    print("-------------------------------------------------------------")
    print("")


def printErrorMessage():
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("The list is empty. Please generate a list first!!")
    print("")
    print("-------------------------------------------------------------")
    print("")


def getLengthOfList() -> int:
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("What should be the length of the list?")
    print("")
    length = int(input("Length = "))
    print("")
    print("-------------------------------------------------------------")
    print("")
    return length


def getStep() -> int:
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("What should be frequency with which the partially sorted list should be printed?")
    print("")
    step = 0
    while not step:

        step = int(input("Step = "))
        if step == 0:
            print("")
            print("The step should be greater than 0.")
            print("")
        else:
            print("")
            print("-------------------------------------------------------------")
            print("")
            return step


def printFinalList(a: list):
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Your sorted list is", end=" -> ")
    print(a)
    print("")
    print("-------------------------------------------------------------")
    print("")


def generateRandomList(n: int) -> list:
    minListValue = 0
    maxListValue = 100

    randomList = []

    for i in range(n):
        randomList.append(random.randint(minListValue, maxListValue))

    return randomList


def cocktailSort(a: list, step: int) -> list:
    """
    The function sorts the array of numbers using the cocktail-sort algorithm
        > Cocktail sort is a variation of bubble sort, the only difference being
        that it traverses through the array both ways, not only left to right
    :param a: list of given numbers
    :param step: an int that tells us how often to print the sorting algorithm's progress
    :return: the same list, but sorted using the cocktail-sort
    """

    iteration = 0
    swapped = True
    last = len(a) - 1
    first = 0
    while swapped:
        swapped = False

        iteration = iteration + 1

        # loop runs through all components and bubble sort's them ascending
        for i in range(first, last):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not iteration % step:
            print(a)

        if not swapped:
            break

        swapped = False

        iteration = iteration + 1

        # the last element is at its final spot, therefore we will not be checking it anymore
        last = last - 1

        # loop runs through all components and bubble sort's them ascending, right to left
        for i in range(last, first, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swapped = True

        if not iteration % step:
            print(a)

        if not swapped:
            break

        # the same as for last
        first = first + 1

    return a


def getGap(gap: int) -> int:
    # divide the gap each time by 1.3 and get the int part
    gap = (gap * 10) // 13

    # the gaps stop at 1
    if gap < 1:
        return 1
    return gap


def combSort(a: list, step: int) -> list:
    """
    Comb sort is a variation of bubble sort that compares values placed at a distance grater than 1 from eachother
    The algorithm starts with a big gap that shrinks every time by 1.3
    It is more efficient since it removes more than one inversion with each step
    :param a: a list of given numbers
    :param step: an int that tells us how often to print the sorting algorithm's progress
    :return: the same list, but sorted using the comb-sort
    """

    # initial gap is the actual size of the list
    length = len(a)

    gap = length

    # swapped is used to make sure if the loop should or should not run, in case the list
    # has been already sorted (aka no changes were made previously)

    swapped = True

    iteration = 0

    while (gap != 1) or (swapped):

        iteration = iteration + 1

        gap = getGap(gap)
        swapped = False
        for i in range(0, length - gap):
            if a[i] > a[i + gap]:
                # swap the two elements
                a[i], a[i + gap] = a[i + gap], a[i]
                swapped = True

        if not iteration % step:
            print(a)

    return a


while True:
    print_menu()

    # list that is going be used for sorting

    # given_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # used for testing the algorithms

    option = input(">")

    if option == "1":
        len_list = getLengthOfList()

        LIST = generateRandomList(len_list)

        print("Your list is", end=" -> ")
        print(LIST)

    elif option == "2":
        # LIST hasn't been generated yet
        if "LIST" not in locals():
            printErrorMessage()

        else:
            STEP = getStep()

            NEW_LIST = cocktailSort(LIST, STEP)

            printFinalList(NEW_LIST)

    elif option == "3":
        if "LIST" not in locals():
            printErrorMessage()

        else:
            STEP = getStep()

            NEW_LIST = combSort(LIST, STEP)

            printFinalList(NEW_LIST)

    elif option == "0":
        print("Bye!")
        break
