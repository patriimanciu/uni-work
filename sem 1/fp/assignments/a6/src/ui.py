#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements)
# are found here
#
from tabulate import tabulate
from functions import (to_list, add_transaction, sort_bank_account, remove_transactions, replace_transaction, get_type,
                       compute_balance, get_amount, _filter, undo)
from colorama import Fore, Style


def get_user_input():
    print()
    print(Fore.LIGHTMAGENTA_EX + "--------------------------------------")
    commands = """
    add <value> <type> <description>
    insert <day> <value> <type> <description>
    remove <day>
    remove <start day> to <end day>
    remove <type>
    replace <day> <type> <description> with <value>
    list
    list <type>
    list [ < | = | > ] <value>
    list balance <day>
    filter <type>
    filter <type> <value>
    undo         
    """
    print()
    print("Supported commands look like this:")
    print(f"{commands}" + Style.RESET_ALL)
    return input("Enter command: ")


def display_error(message):
    print(Fore.RED + f"Error: {message}" + Style.RESET_ALL)


def parse_command(command):
    tokens = command.split()
    action = tokens[0].lower()
    args = tokens[1:]
    return action, args


def print_bank_account_table(bank_account):
    bank_account_sorted = sort_bank_account(bank_account)
    col_names = ["Day", "Amount", "Type", "Description"]
    table = []
    print("")
    print("--------------------------------------")
    print("")
    print("Transactions: ")
    print("")
    for money in bank_account_sorted:
        table.append(to_list(money))
    print(tabulate(table, headers=col_names, tablefmt="fancy_grid"))
    print("")
    print("--------------------------------------")
    print("")


def add_transaction_ui(bank_account, args):
    try:
        add_transaction(bank_account, args)
    except ValueError as ve:
        print(Fore.RED + "There was a problem in adding the transaction.")
        print(str(ve) + Style.RESET_ALL)


def remove_transactions_ui(bank_account, args):
    try:
        remove_transactions(bank_account, args)
    except ValueError as ve:
        print(Fore.RED + "There was a problem when removing the transaction.")
        print(str(ve) + Style.RESET_ALL)


def replace_transactions_ui(bank_account, args):
    try:
        replace_transaction(bank_account, args)
    except ValueError as ve:
        print(Fore.RED + "There was a problem when replacing the transaction.")
        print(str(ve) + Style.RESET_ALL)


def list_type(bank_account, args):
    new_transactions = []
    for transaction in bank_account:
        if get_type(transaction) == args[0]:
            new_transactions.append(transaction)

    print_bank_account_table(new_transactions)


def list_balance(bank_account, args):
    print("Balance at the end of day " + Fore.GREEN + str(args[1]) + Style.RESET_ALL + " is " + Fore. MAGENTA + str(compute_balance(bank_account, args[1])) + Style.RESET_ALL)


def list_smaller(bank_account: list, value: int):
    new_transactions = []
    for transaction in bank_account:
        if get_amount(transaction) < value:
            new_transactions.append(transaction)
    print_bank_account_table(new_transactions)


def list_bigger(bank_account: list, value: int):
    new_transactions = []
    for transaction in bank_account:
        if get_amount(transaction) > value:
            new_transactions.append(transaction)
    print_bank_account_table(new_transactions)


def list_equal(bank_account: list, value: int):
    new_transactions = []
    for transaction in bank_account:
        if get_amount(transaction) == value:
            new_transactions.append(transaction)
    print_bank_account_table(new_transactions)


def list_amount(bank_account, args):
    if args[0] == "<":
        list_smaller(bank_account, int(args[1]))
    elif args[0] == ">":
        list_bigger(bank_account, int(args[1]))
    elif args[0] == "=":
        list_equal(bank_account, int(args[1]))
    else:
        print(Fore.RED + "Invalid command." + Style.RESET_ALL)


def list_ui(bank_account, args):
    if len(args) == 0:
        print_bank_account_table(bank_account)
    elif len(args) == 1:
        list_type(bank_account, args)
    elif len(args) == 2 and args[0] == "balance":
        list_balance(bank_account, args)
    elif len(args) == 2:
        list_amount(bank_account, args)
    else:
        print(Fore.RED + "There was a problem when listing the transactions." + Style.RESET_ALL)


def filter_type_ui(bank_account, args):
    try:
        new_bank = _filter(bank_account, args)
        print_bank_account_table(new_bank)
    except ValueError as ve:
        print(Fore.RED + "There was a problem when filtering the data.")
        print(str(ve) + Style.RESET_ALL)


def undo_ui(bank_account, previous_state):
    try:
        undo(bank_account, previous_state)
    except ValueError as ve:
        print(Fore.RED + "There was a problem.")
        print(str(ve) + Style.RESET_ALL)


def exit_program():
    print(Fore.GREEN + "Bye! :) " + Style.RESET_ALL)


def passed():
    print(Fore.GREEN + "All tests have passed :)" + Style.RESET_ALL)
