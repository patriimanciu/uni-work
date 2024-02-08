#
# Write the implementation for A5 in this file
#

"""
    Implement a menu-driven console application that provides the following functionalities:

    1. Read a list of complex numbers (in z = a + bi form) from the console.
    2. Display the entire list of numbers on the console.
    3. Display on the console the sequence, subarray or numbers required by the properties that were assigned to you.
       Each student will receive one property from Set A and another one from Set B.
    4. Exit the application.

Set A
    5. Length and elements of the longest subarray of numbers where each number's modulus is in the [0, 10] range.
    Obs: Elements of a subarray are in consecutive order of their appearance in the array,

Set B
    9. The length and elements of the longest increasing subsequence, when considering each number's modulus
"""

from random import randint
import math

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def get_real(numbers):    
    return numbers[1]


def get_imaginary(numbers):
    return numbers[2]


def get_id(numbers):
    return numbers[0]


def create_complex_number(_id: int, real: int, imag: int):
    return {0: _id, 1: real, 2: imag}


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

"""
def get_real(numbers):
    return numbers["real"]


def get_imaginary(numbers):
    return numbers["imag"]


def get_id(numbers):
    return numbers["id"]


def create_complex_number(_id: int, real: int, imag: int):
    return {"id": _id, "real": real, "imag": imag}"""

#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def to_str(numbers):
    real_part = get_real(numbers)
    imag_part = get_imaginary(numbers)
    _id = get_id(numbers)
    modulus = get_number_modulus(numbers)

    if real_part == 0 and imag_part != 0:
        return f"z{_id} = {imag_part}i, modulus = {modulus}"
    elif real_part == 0 and imag_part == 0:
        return f"z{_id} = 0, modulus = {modulus}"
    elif real_part and imag_part == 0:
        return f"z{_id} = {real_part}, modulus = {modulus}"
    else:
        return f"z{_id} = {real_part} + {imag_part}i, modulus = {modulus}"


def generate_random_complex_numbers(n: int) -> list:
    result = []
    _id = 1

    while n > 0:
        real = randint(-10, 10)
        imag = randint(-10, 10)

        number = create_complex_number(_id, real, imag)
        _id += 1

        result.append(number)
        n -= 1

    return result


# |z| = √(a^2 + b^2)
def get_number_modulus(number):
    real = get_real(number)
    imag = get_imaginary(number)
    modulus = math.sqrt(real ** 2 + imag ** 2)
    return modulus


# Set A
#    Length and elements of the longest subarray of numbers where each number's modulus is in the [0, 10] range.
#    Obs: Elements of a subarray are in consecutive order of their appearance in the array
def setA_naive(numbers):
    index = 0
    index_max = 0
    length = 0
    length_max = 0

    for i in range(len(numbers)):
        modulus = get_number_modulus(numbers[i])
        if 0 <= modulus <= 10:
            length += 1
        else:
            if length > length_max:
                length_max = length
                index_max = index
            length = 0
            index = i + 1

    if length > length_max:
        length_max = length
        index_max = index

    return length_max, index_max


# Set B
#     The length and elements of the longest increasing subsequence, when considering each number's modulus
#     OBS: subsequences can skip elements
def setB_dynamic_programming(numbers):
    length = len(numbers)

    # data structure used for DP is a list that saves the length of the longest increasing sequence up to index i
    longest_increasing_sequence = [1] * length

    # the longest increasing subsequence for index 0 is 1 => we start checking from index 1
    for i in range(1, length):
        # we check all elements before i
        for j in range(0, i):
            modulus_i = get_number_modulus(numbers[i])
            modulus_j = get_number_modulus(numbers[j])
            # modulus_j <= modulus_i -> increasing
            if modulus_j <= modulus_i:
                longest_increasing_sequence[i] = max(longest_increasing_sequence[i], longest_increasing_sequence[j] + 1)


    maximum_length = max(longest_increasing_sequence)
    maximum_index = longest_increasing_sequence.index(maximum_length)

    # since we know only the index of the maximum length, we have to reconstruct the subsequence, going backwards
    # from maximum_index

    # Retrace the steps
    subsequence = []

    i = maximum_index
    l = maximum_length
    while i >= 0 and l > 0:
        if longest_increasing_sequence[i] == l:
            subsequence.append(numbers[i])
            l -= 1
        i -= 1

    subsequence.reverse()

    return len(subsequence), subsequence


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def print_menu():
    print("")
    print("-------------------------------------------------------------")
    print("")
    print("1. Read a list of complex numbers from console.")
    print("2. Display the list of numbers.")
    print("3. Display:")
    print("\t a. Length and elements of the longest subarray of numbers where each number's modulus is in ∈ [0, 10]")
    print("\t b. The length and elements of the longest increasing subsequence, when considering each number's modulus")
    print("0. Exit.")
    print("")
    print("-------------------------------------------------------------")
    print("")


def write_complex_numbers_list(numbers: list):
    print("The list of complex numbers:")
    for num in numbers:
        print(to_str(num))


def read_and_add_number_to_list(numbers):
    input_str = input("Enter a list of numbers (a + bi) separated by a comma (e.g. 1 + 3i, 2 + -2i, 3 + 0i): ")
    num_strings = input_str.split(sep=',')
    for num in num_strings:
        sections = num.split("+")
        if len(sections) != 2:
            print("Invalid input. The format should be a + bi.")
            continue

        real_str = sections[0].strip()
        imag_str = sections[1].strip(' i')

        try:
            real = int(real_str)
            if imag_str:
                imag = int(imag_str)
            else:
                imag = 0
            new_num = create_complex_number(get_id(numbers[-1]) + 1, real, imag)
            numbers.append(new_num)
        except ValueError as ve:
            print("Invalid input. Please enter a valid complex number.")
            print(ve)
    return numbers


def property_a(numbers):
    print("Property A:")
    print(
        " The length and elements of a longest subarray of numbers where each number's modulus is in the [0, 10] range.")
    length, index = setA_naive(numbers)
    print(f"The maximum length of the subarray is {length} and the according elements are: ")
    while length:
        print(to_str(numbers[index]))
        index += 1
        length -= 1


def property_b(numbers):
    print("")
    print("Property B:")
    print(" The length and elements of the longest increasing subsequence, when considering each number's modulus.")
    length, subsequence = setB_dynamic_programming(numbers)
    print(f"The maximum length of the subsequence is {length} and the according elements are: ")
    for sub in subsequence:
        print(to_str(sub))


def given_properties(numbers):
    property_a(numbers)
    property_b(numbers)


def start():
    """
        1. Print main menu
        2. Read user options
        3. Call the function that solves the request
    """

    complex_num = generate_random_complex_numbers(10)

    while True:
        print_menu()

        option = input(">")

        if option == "1":
            read_and_add_number_to_list(complex_num)
        elif option == "2":
            write_complex_numbers_list(complex_num)
        elif option == "3":
            given_properties(complex_num)
        elif option == "0":
            print("Bye!")
            return
        else:
            print("Invalid input!")


if __name__ == "__main__":
    start()
