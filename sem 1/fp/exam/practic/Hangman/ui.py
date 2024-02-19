from Hangman.repository import Repo
from Hangman.service import Service


class UI:
    def __init__(self):
        self.__repo = Repo()
        self.__service = Service(self.__repo)

    def start(self):
        # print(self.__repo.sentences())
        # print(self.__repo.chosen())
        # print(self.__repo.chosen_coded())

        while True:
            print(str(self.__repo))
            letter = input(">").lower()
            if len(letter) > 1:
                print("You have to choose just 1 letter")
            else:
                try:
                    int(letter)
                    print("You must choose a LETTER")
                except ValueError:
                    pass

            # good input
            self.reveal(letter)
            if self.__service.won():
                print("YOU WON!")
                break

            if self.__service.lost():
                print("you lost...")
                break

    def reveal(self, letter: str):
        if not self.__service.reveal(letter):
            self.print_hangman()

    def print_hangman(self):
        h = ''.join(h for h in self.__service.hangman())
        print(h)


if __name__ == "__main__":
    ui = UI()
    ui.start()
