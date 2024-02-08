import random
import timeit
from tabulate import tabulate


def print_menu():
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("1. Generate a list of n random natural numbers between 0 and 100.")
    print("2. Sort the list using the cocktail sort.")
    print("3. Sort the list using the comb sort.")
    print("4. Illustrate the runtime for Best Case.")
    print("5. Illustrate the runtime for Average Case.")
    print("6. Illustrate the runtime for Worst Case.")
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


def printFinalList(a: list):
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Your sorted list is", end=" -> ")
    print(a)
    print("")
    print("-------------------------------------------------------------")
    print("")


def printPrompt4() -> int:
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Now we'll illustrate the runtime of Cocktail sort, and then Comb sort, on the best case.")
    print("For both of these sorting algorithm, the best case is  when the list is already sorted.")
    print("")
    start_length = int(input("What should be the starting set's length? Length = "))
    print("")
    print("-------------------------------------------------------------")
    print("")
    return start_length


def printPrompt5() -> int:
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Now we'll illustrate the runtime of Cocktail sort, and then Comb sort, on an average case.")
    print("")
    start_length = int(input("What should be the starting set's length? Length = "))
    print("")
    print("-------------------------------------------------------------")
    print("")
    return start_length


def printPrompt6() -> int:
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("Now we'll illustrate the runtime of Cocktail sort, and then Comb sort, on the worst case.")
    print("For both of these sorting algorithm, the worst case is  when the list is sorted in reverse order.")
    print("")
    start_length = int(input("What should be the starting set's length? Length = "))
    print("")
    print("-------------------------------------------------------------")
    print("")
    return start_length



def generateRandomList(n: int) -> list:
    minListValue = 0
    maxListValue = 100

    randomList = []

    for i in range(n):
        randomList.append(random.randint(minListValue, maxListValue))

    return randomList


def cocktailSort(a: list) -> list:
    """
    The function sorts the array of numbers using the cocktail-sort algorithm
        > Cocktail sort is a variation of bubble sort, the only difference being
        that it traverses through the array both ways, not only left to right
    :param a: list of given numbers
    :return: the same list, but sorted using the cocktail-sort
    """

    """
    Complexity
    Best Case Complexity
        It occurs when there is no sorting required, i.e., the array is already sorted. 
        The best-case time complexity of cocktail sort is O(n), since it passes only once through the whole loop,
        after which the swapped variable will remain False, therefore the algorithm won't continue
    
    Worst Case Complexity 
        It occurs when the array elements are required to be sorted in reverse order. 
        That means suppose you have to sort the array elements in ascending order, but its elements are in descending 
        order. The worst-case time complexity of cocktail sort is O(n^2), since it will pass through the whole loop
        for each element before the swapped value remains False.
    """

    swapped = True
    last = len(a) - 1
    first = 0
    while swapped:
        swapped = False

        # loop runs through all components and bubble sort's them ascending
        for i in range(first, last):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        # the last element is at its final spot, therefore we will not be checking it anymore
        last = last - 1

        # loop runs through all components and bubble sort's them ascending, right to left
        for i in range(last, first, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swapped = True

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


def combSort(a: list) -> list:
    """
    Comb sort is a variation of bubble sort that compares values placed at a distance grater than 1 from each other
    The algorithm starts with a big gap that shrinks every time by 1.3
    It is more efficient since it removes more than one inversion with each step
    :param a: a list of given numbers
    :return: the same list, but sorted using the comb-sort
    """

    """
    Complexity
    The worst-case complexity of this algorithm is O(n^2) 
        The Worst case configuration is when all the elements are already or 
        nearly sorted but in reverse order.
        
    The Best Case complexity is O(n*log(n)).
        The best configuration occurs when all the elements are already sorted or nearly sorted. 
        In this case, the loop will be run only once.
    """

    # initial gap is the actual size of the list
    length = len(a)

    gap = length

    # swapped is used to make sure if the loop should or should not run, in case the list
    # has been already sorted (aka no changes were made previously)

    swapped = True

    while (gap != 1) or swapped:  # log(n)

        gap = getGap(gap)
        swapped = False
        for i in range(0, length - gap):  # n
            if a[i] > a[i + gap]:
                # swap the two elements
                a[i], a[i + gap] = a[i + gap], a[i]
                swapped = True

    return a


def cocktail_reversed(a: list) -> list:
    """
    This function uses the cocktail algorithm to sort the function in reverse
    :param a: given list
    :return: the same list reversed
    """
    swapped = True
    last = len(a) - 1
    first = 0
    while swapped:
        swapped = False

        # loop runs through all components and bubble sort's them ascending
        for i in range(first, last):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        # the last element is at its final spot, therefore we will not be checking it anymore
        last = last - 1

        # loop runs through all components and bubble sort's them ascending, right to left
        for i in range(last, first, -1):
            if a[i] > a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swapped = True

        if not swapped:
            break

        # the same as for last
        first = first + 1

    return a


def generate_row(a: list) -> list:
    """
    This function times each sorting algorithm and generates a list as follows:
        final[0] = length of the list
        final[1] = time for cocktail sort
        final[2] = time for comb sort
    This final list will then be appended into a table as one row
    :param a: given list
    :return: a list containing the specifications above
    """
    final = [len(a)]

    # made a copy for each list, so we don't work with the original one
    copied_for_cocktail = list(a)
    copied_for_comb = list(a)

    start_cocktail = timeit.default_timer()
    sortedList = cocktailSort(copied_for_cocktail)
    end_cocktail = timeit.default_timer()
    timer_cocktail = end_cocktail - start_cocktail

    final.append(timer_cocktail)

    start_comb = timeit.default_timer()
    sortedList = combSort(copied_for_comb)
    end_comb = timeit.default_timer()
    timer_comb = end_comb - start_comb

    final.append(timer_comb)

    return final


while True:
    print_menu()

    # defined the header for table
    col_names = ["Size", "Cocktail sort", "Comb sort"]

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
            NEW_LIST = cocktailSort(LIST)

            printFinalList(NEW_LIST)

    elif option == "3":
        if "LIST" not in locals():
            printErrorMessage()

        else:

            NEW_LIST = combSort(LIST)

            printFinalList(NEW_LIST)

    elif option == "4":
        # Illustrate time for best case
        length4 = printPrompt4()

        table = []

        for i in range(5):
            # list4 will be called as an already sorted list to illustrate the times for best case
            list4 = cocktailSort(generateRandomList(length4))

            table.append(generate_row(list4))

            length4 *= 2

        print(tabulate(table, headers=col_names, tablefmt="fancy_grid"))

    elif option == "5":
        # Illustrate time for average case
        length5 = printPrompt5()

        table = []

        for i in range(5):
            list5 = generateRandomList(length5)

            table.append(generate_row(list5))

            length5 *= 2  # for the next list

        print(tabulate(table, headers=col_names, tablefmt="fancy_grid"))

    elif option == "6":
        length6 = printPrompt6()

        table = []

        for i in range(5):
            # list4 will be called as an already sorted list in reverse to illustrate the times for worst case
            list6 = cocktail_reversed(generateRandomList(length6))

            table.append(generate_row(list6))

            length6 *= 2

        print(tabulate(table, headers=col_names, tablefmt="fancy_grid"))

    elif option == "0":
        print("Bye!")
        break
