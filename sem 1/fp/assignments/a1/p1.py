"""
    For a given natural number n find the largest natural number written with the same digits.
    (e.g. n=3658, m=8653).
"""

def digits(n: int) -> list:
    """
    Split the given number into its digits
    :param n: given number read from console
    :return: n's digits in a list
    """
    dig = [] # empty list
    while n > 0:
        dig.append(n % 10)
        n = n // 10
    return dig


def sort(s: list) -> list:
    """
    Sorts the list of digits using the 2 for's method
    :param s: list of the given number's digits
    :return: a list of the same digits, sorted descending
    """
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if s[i] <= s[j]:
                # swap 'cause i couldn't find a function
                aux = s[i]
                s[i] = s[j]
                s[j] = aux
    return s


def make_new(s: list) -> int:
    """
    Turns the list into an int
    :param s: list of given digits
    :return: an int made out of the digits found in the list s
    """

    new_number = 0
    for i in range(0, len(s)):
        new_number = new_number * 10 + s[i]
    return new_number


while True:
    print("1. Read a number from console")
    print("0. Exit")
    option = input(">")

    if option == "1":
        number_str = input("n = ")

        if number_str.isdigit():
            number = int(number_str)
            print(number)
            d = digits(number)
            # print(d)

            d2 = sort(d)
            # print(d2)
            m = make_new(d2)
            print(m)

        else:
            print("Input is not the correct format. Please enter a number.")

    if option == "0":
        print("Bye! ")
        break