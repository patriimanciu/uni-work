"""
    Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,...
    obtained from the sequence of natural numbers by replacing composed numbers with
    their prime divisors, each divisor d being written d times, *without memorizing the
    elements of the sequence*.
"""

def is_prime(n: int) -> bool:

    """
    Basic is_prime function
    :param n: given n, integer
    :return: True is the given number is prime, False if otherwise
    """

    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i < n:
            if n % i == 0:
                return False
            i += 1
    return True


def divisors(number: int) -> list:

    """
    Finds the prime divisors of a given number and adds them into a list
    :param number: given number, integer
    :return: list of the prime divisors of a number
    """

    data = [] # empty list
    for i in range(2, number):
        if number % i == 0:
            if is_prime(i):
                data.append(i)
    return data


def print_n(number: int, cnt: int, n: int) -> bool:
    """
    The funtion prints the number only if we haven't reached the n-th iteration
    :param number: the current number we're on
    :param cnt: number of iterations (the nuber of times the funtion has been called)
    :param n: given number entered by the user
    :return: True if we're at the n-th iteration, False if we haven't reached n yet
    """

    if cnt == n:
        print(number)
        print("The " + str(n) + "-th value is " + str(number))
        return True
    elif cnt < n:
        print(number, end=" ")
        return False


while True:
    print("")
    num = int(input("n = "))
    count = 0 # initial value of printed numbers
    exists = False
    for i in range(1, num + 1):
        if exists == False:

            d = divisors(i)

            # if len(d) > 0 it means that the number has prime divisors, so that each divisor d is written d times
            if len(d):

                for j in range(0, len(d)): # run through all divisors
                    for k in range(0, d[j]): # print each divisor * its value
                        count = count + 1

                        # turns True iff the print_n funtion reached its n-th iteration
                        exists = print_n(d[j], count, num)

                        if exists == True:
                            i = num + 1 # bring the initial loop to end
                            break

            else:
                count = count + 1
                exists = print_n(i, count, num)

                if exists == True:
                    i = num + 1
                    break
    # the program stops when a value <= 0 is entered since you cannot print the n-th number of the sequence
    if num <= 0:
        print("Invalid.")
        break