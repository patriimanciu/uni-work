#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print
# statements. Functions here communicate via function parameters, the return statement and raising of exceptions.
#
from random import randint, choice

"""
The way you store transactions:
    day (of the month in which the transaction was made, between 1 and 30 for simplicity), amount of money (transferred,
    positive integer), type (in - into the account, out – from the account), and description
"""


def get_day(transaction: dict) -> int:
    return transaction["day"]


def get_amount(transaction):
    return transaction["amount"]


def get_type(transaction):
    return transaction["type"]


def get_description(transaction):
    return transaction["description"]


def set_amount(transaction, amount):
    transaction["amount"] = int(amount)


def create_bank_account():
    """
    Creates an empty bank account.
    :return:
    """
    account = []
    return account


def create_transaction(day: int, money: int, _type: str, description: str):
    """
    Creates and returns a dictionary representing a financial transaction.
    :param day: An integer representing the day of the month when the transaction occurred.
    :param money: An integer representing the amount of money involved in the transaction.
    :param _type: A string indicating the type of transaction ("in" for income, "out" for expense).
    :param description: A string describing the nature of the transaction.
    :return: A dictionary representing a financial transaction.
    """
    return {"day": day, "amount": money, "type": _type, "description": description}


def to_list(money: dict) -> list:
    """
    Converts a transaction dictionary to a list.
    :param money: A dictionary representing a financial transaction.
    :return: A list containing the day, amount, type, and description of the transaction.
    """
    m = [money["day"], money["amount"], money["type"], money["description"]]
    return m


def get_random_transactions(bank_account):
    """
    Generates and adds random transactions to the given bank account.
    :param bank_account: A list representing a bank account.
    :return: The bank account with randomly generated transactions added.
    """
    types = ["in", "out"]
    descriptions = ["pizza", "salary", "rent", "eating out", "side hustle", "groceries", "school", "car", "pet", "vacation"]
    for i in range(10):
        day = randint(1, 30)
        money = randint(1, 100)
        _type = choice(types)
        description = choice(descriptions)
        new_transaction = create_transaction(day, money, _type, description)
        bank_account.append(new_transaction)
    return bank_account


def sort_bank_account(bank_account):
    """
    Sorts a bank account based on the day of each transaction in ascending order.
    :param bank_account: A list representing a bank account.
    :return: A sorted list representing the bank account.
    """
    bank_account_sorted = sorted(bank_account, key=lambda x: x["day"])
    return bank_account_sorted


def add_transaction(bank_account, args):
    """
    Adds a new transaction to the bank account.
    :param bank_account: A list representing a bank account.
    :param args: A list containing transaction details (amount, type, and description).
    :return: Raises: ValueError if the number of arguments is not valid.
    """
    if len(args) == 3:
        bank_account_sorted = sort_bank_account(bank_account)
        current_day = bank_account_sorted[-1]["day"]
        transaction = create_transaction(current_day, args[0], args[1], args[2])
        bank_account.append(transaction)
    elif len(args) == 4:
        transaction = create_transaction(int(args[0]), int(args[1]), args[2], args[3])
        bank_account.append(transaction)
    else:
        raise ValueError("Not enough arguments. Invalid command.")


def remove_day(bank_account, day):
    """
    Removes transactions with a specific day from the bank account.
    :param bank_account: A list representing a bank account.
    :param day: An integer representing the day of transactions to be removed.
    """
    if day is not None:
        bank_account[:] = [transaction for transaction in bank_account if get_day(transaction) != day]


def remove_transaction_between_dates(bank_account, start_day, end_day):
    """
    Removes transactions between two specified days from the bank account.
    :param bank_account: A list representing a bank account.
    :param start_day: An integer representing the start day of transactions to be removed.
    :param end_day: An integer representing the end day of transactions to be removed.
    """
    bank_account[:] = [transaction for transaction in bank_account if int(start_day) > get_day(transaction) or get_day(transaction) > int(end_day)]


def remove_type(bank_account, _type):
    """
    Removes transactions of a specified type from the bank account.
    :param bank_account: A list representing a bank account.
    :param _type: A string indicating the type of transactions to be removed.
    """
    bank_account[:] = [transaction for transaction in bank_account if get_type(transaction) != _type]


def remove_transactions(bank_account, args):
    """
    Removes transactions based on the provided criteria.
    :param bank_account: A list representing a bank account.
    :param args: A list containing criteria for removing transactions.
    :return: Raises: ValueError if the remove command is invalid.
    """
    if len(args) == 1 and (args[0] != "in" and args[0] != "out"):
        remove_day(bank_account, int(args[0]))
    elif len(args) == 3 and args[1] == 'to':
        remove_transaction_between_dates(bank_account, args[0], args[2])
    elif len(args) == 1 and args[0] in ['in', 'out']:
        remove_type(bank_account, _type=args[0])
    else:
        raise ValueError("Invalid remove command")


def replace_transaction(bank_account, args):
    """
    Replaces the amount of a specific transaction with a new amount.
    :param bank_account: A list representing a bank account.
    :param args: A list containing details for the replacement (day, type, description, "with", new amount).
    :return: Raises: ValueError if the replace command is invalid.
    """
    if len(args) == 5:
        for transaction in bank_account:
            if get_day(transaction) == int(args[0]) and get_type(transaction) == args[1] and get_description(transaction) == args[2] and args[3] == "with":
                set_amount(transaction, args[4])
                break
    else:
        raise ValueError("Invalid replace command")


def compute_balance(bank_account, args) -> int:
    """
    Computes the balance of the account up to a specified day.
    :param bank_account:  A list representing a bank account.
    :param args: A list containing criteria for computing the balance.
    :return: An integer representing the account balance.
    """
    balance = 0
    for transaction in bank_account:
        if get_day(transaction) <= int(args):
            if get_type(transaction) == "in":
                balance += get_amount(transaction)
            else:
                balance -= get_amount(transaction)
    return balance


def filter_type(bank_account, _type):
    """
    Filters transactions based on the specified type.
    :param bank_account: A list representing a bank account.
    :param _type: A string indicating the type of transactions to be filtered.
    :return: A filtered list of transactions.
    """
    return [transaction for transaction in bank_account if get_type(transaction) == _type]


def filter_amount(bank_account, value):
    """
    Filters transactions based on the specified amount.
    :param bank_account: A list representing a bank account.
    :param value: An integer representing the maximum amount for filtering.
    :return: A filtered list of transactions.
    """
    return [transaction for transaction in bank_account if get_amount(transaction) < int(value)]


def _filter(bank_account, args):
    """
    Filters transactions based on the provided criteria.
    :param bank_account: A list representing a bank account.
    :param args: A list containing criteria for filtering transactions.
    :return: A filtered list of transactions.
    """
    if len(args) == 1:
        new_bank = []
        if args[0] in ["in", "out"]:
            new_bank = filter_type(bank_account, args[0])
            return new_bank
        else:
            raise ValueError("Command line invalid. Too many arguments")
    elif len(args) == 2 and args[1].isdigit():
        new_bank = filter_type(bank_account, args[0])
        new_bank = filter_amount(new_bank, args[1])

        return new_bank
    else:
        raise ValueError("Command line invalid. Too many arguments")


def undo(bank_account, previous_state):
    """
    Undoes the last operation by restoring the previous state of the bank account.
    :param bank_account: A list representing a bank account.
    :param previous_state: A list containing previous states of the bank account.
    :return: Raises: ValueError if there are no operations to undo.
    """
    if previous_state:
        bank_account.clear()
        bank_account.extend(previous_state.pop())
    else:
        raise ValueError("No operations to undo.")
