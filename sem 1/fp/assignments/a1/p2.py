"""
    Find the smallest number m from the Fibonacci sequence,
    defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2,
    larger than the given natural number n. (e.g. for n = 6, m = 8).
"""

def Fibb(number: int) -> int:
    """
    Generates the Fibonacci sequence, memorizing only the last 2 elements
    :param number: given number from console
    :return: b - smallest number larger than the number given
    """
    a = 1
    b = 1
    while number >= b:
        c = a
        a = b
        b = a + c
    return b


while True:
    print("1. Read a number from console")
    print("0. Exit")

    option = input(">")

    if option == "1":
        n = int(input("n = "))
        m = Fibb(n)
        print("Smallest Fibonacci number larger than given n is", m)

    elif option == "0":
        print("Bye!")
        break