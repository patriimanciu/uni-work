from service import BoardError, BoardService, FileError
from domain import Board


class UI:
    def __init__(self):
        self.__board = Board()
        self.__service = BoardService(self.__board)

    @staticmethod
    def get_input():
        command = input("> ")
        data = command.strip().split(' ')
        return data

    def start(self):
        # get input from user => either a move or saving the current state of the board
        # make a move
        self.load_previous()

        print(self.__board)
        while True:
            if self.__service.full_board():
                print("The board is full, Chaos won...")
                break
            data = self.get_input()
            if len(data) == 1 and data[0] == "save":
                self.save_board()
            elif len(data) < 3:
                print("Invalid input, must have at least 3 elements.")
            elif len(data) == 3:
                try:
                    self.move(data)
                    print("Moved successfully!")
                    if self.__service.check_if_won():
                        print("Congrats! Order won!!")
                        break
                    comp = self.computer_move()
                    print(f"Computer moved to ({comp[0]}, {comp[1]}) with {comp[2]}.")
                    if self.__service.check_if_won():
                        print("Congrats! Order won!!")
                        break
                    print(self.__board)
                except BoardError as e:
                    print(e)

    def save_board(self):
        self.__service.save()

    def move(self, data: list):
        self.__service.move(data[0], data[1], data[2])

    def computer_move(self):
        return self.__service.computer_move()

    def load_previous(self):
        while True:
            loading = input("Do you want to load the previous game (Y/N)? > ")
            if loading == "Y":
                try:
                    self.__service.load('file.txt')
                    return
                except FileError as e:
                    print(e)
                    return
            elif loading == "N":
                return
            else:
                print("Wrong input!")


if __name__ == "__main__":
    ui = UI()
    ui.start()
