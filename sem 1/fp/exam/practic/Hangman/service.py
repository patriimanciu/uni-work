from Hangman.repository import Repo


class ServiceError(Exception):
    pass


class Service:
    def __init__(self, repo: Repo):
        self.__repo = repo
        self.tries = 0  # number of letters in hangman
        self._hangman = ["" for i in range(7)]

    def add(self, new: str):
        words = new.strip().split(' ')
        if len(words) < 2:
            raise ServiceError("Sentence must have at least 2 words.")
        for w in words:
            if len(w) < 3:
                raise ServiceError("Each word must have at least 3 letters")
        self.__repo.add(new)

    def reveal(self, letter):
        return self.__repo.reveal(letter)

    def won(self):
        return self.__repo.won()

    def lost(self):
        return self._hangman[-1] == "n"

    def hangman(self):
        h = "hangman"
        self._hangman[self.tries] = h[self.tries]
        self.tries += 1
        return self._hangman

    def __str__(self):
        return str(self.__repo)
