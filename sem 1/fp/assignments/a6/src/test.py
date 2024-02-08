from functions import sort_bank_account, create_bank_account, add_transaction, remove_day, \
    remove_transaction_between_dates, remove_type, remove_transactions, replace_transaction, compute_balance, \
    filter_type, filter_amount, undo
from ui import passed


def test_sort_bank_account():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]

    sorted_bank_account = sort_bank_account(bank_account)

    assert sorted_bank_account == [
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]


def test_add_transaction():
    bank_account = create_bank_account()
    add_transaction(bank_account, [15, 100, "in", "salary"])
    assert len(bank_account) == 1
    assert bank_account[0] == {"day": 15, "amount": 100, "type": "in", "description": "salary"}

    try:
        add_transaction(bank_account, [15, "in"])
        assert False
    except:
        assert True


def test_remove_day():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    remove_day(bank_account, 3)
    assert bank_account == [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]


def test_remove_transaction_between_dates():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    remove_transaction_between_dates(bank_account, 3, 6)
    assert bank_account == [
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]


def test_remove_type():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    remove_type(bank_account, "in")
    assert bank_account == [
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"}
    ]


def test_remove_transactions():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    remove_transactions(bank_account, ["in"])
    assert bank_account == [
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"}
    ]


def test_replace_transaction():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    replace_transaction(bank_account, [3, "out", "groceries", "with", 75])
    assert bank_account == [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 75, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]


def test_compute_balance():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    balance = compute_balance(bank_account, 6)
    assert balance == 50


def test_filter_type():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    filtered_transactions = filter_type(bank_account, "in")
    assert filtered_transactions == [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]


def test_filter_amount():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    filtered_transactions = filter_amount(bank_account, 75)
    assert filtered_transactions == [
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"}
    ]


def test_undo():
    bank_account = [
        {"day": 5, "amount": 100, "type": "in", "description": "salary"},
        {"day": 3, "amount": 50, "type": "out", "description": "groceries"},
        {"day": 7, "amount": 200, "type": "in", "description": "bonus"}
    ]
    previous_state = [bank_account]

    add_transaction(bank_account, [10, 150, "out", "shopping"])

    previous_state.append(bank_account)

    undo(bank_account, previous_state)

    assert bank_account == previous_state[0]


def tests():
    test_sort_bank_account()
    test_add_transaction()
    test_remove_day()
    test_remove_transaction_between_dates()
    test_remove_type()
    test_remove_transactions()
    test_replace_transaction()
    test_compute_balance()
    test_filter_type()
    test_filter_amount()
    test_undo()


tests()
passed()
