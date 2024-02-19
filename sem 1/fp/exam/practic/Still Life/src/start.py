from src.board import Board
from src.game import Game, GameError


class UI:
    def __init__(self):
        self.__board = Board()
        self.__game = Game(self.__board)

    @staticmethod
    def get_command():
        print("Please enter a valid command as such: place [pattern] [i],[j]; tick [n], save filename")
        cmd = input("> ")
        data = cmd.strip().split()
        return data[0], data[1:]

    def start(self):
        # loading = input("Do you want to load a previous game(Y/N)? > ")

        # if loading == "Y":
        #     self.__game.load()
        # elif loading == "N":
        #     pass
        # else:
        #     print("Not a valid command.")
        while True:
            print(self.__board)
            action, param = self.get_command()
            # self.get_command()
            if action == "place":
                try:
                    self.__game.place(param)
                except GameError as e:
                    print(e)
            elif action == "tick":
                try:
                    if param:
                        self.__game.tick(int(param[0]))
                    else:
                        self.__game.tick()
                except GameError as e:
                    print(e)
            elif action == "save":
                if param:
                    self.__game.save(param[0])
                else:
                    self.__game.save()
            elif action == "load":
                try:
                    if param:
                        self.__game.load(param[0])
                    else:
                        self.__game.load()
                except GameError as e:
                    print(e)
            else:
                print("Not a valid command.")


if __name__ == "__main__":
    ui = UI()
    ui.start()
