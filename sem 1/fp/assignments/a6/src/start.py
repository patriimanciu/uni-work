#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#

# REQUIREMENTS
# user interface that accepts given commands exactly as stated
# handle the case of incorrect user input by displaying error messages
# use getters and setters
# tests for all non-UI functions related to functionalities (A) and (B)

from ui import (display_error, get_user_input, parse_command, print_bank_account_table,
                add_transaction_ui, remove_transactions_ui, replace_transactions_ui, list_ui, filter_type_ui, undo_ui, exit_program)
from functions import create_bank_account, get_random_transactions


def start():

    bank = create_bank_account()
    previous_state = create_bank_account()
    bank = get_random_transactions(bank)
    print_bank_account_table(bank)
    while True:
        command = get_user_input()
        action, args = parse_command(command)
        # Parse the command and call the appropriate function
        if action == 'add' or action == 'insert':
            previous_state.append(list(bank))
            add_transaction_ui(bank, args)
        elif action == 'remove':
            previous_state.append(list(bank))
            remove_transactions_ui(bank, args)
        elif action == 'replace':
            previous_state.append(list(bank))
            replace_transactions_ui(bank, args)
        elif action == 'list':
            list_ui(bank, args)
        elif action == 'filter':
            filter_type_ui(bank, args)
        elif action == 'undo':
            undo_ui(bank, previous_state)
        elif action == 'exit':
            exit_program()
            break
        else:
            display_error("Invalid command")


if __name__ == "__main__":
    start()
