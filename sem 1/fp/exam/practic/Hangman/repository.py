from random import choice


class RepositoryError(Exception):
    pass


class Repo:
    def __init__(self):
        self.__sentences = []
        self.__chosen_sentence = ""
        self._load()
        self._choose()
        self.__chosen_coded = ["_" for i in range(len(self.__chosen_sentence))]
        self.__letters = []  # the letters not revealed yet
        self._coded()

    def add(self, new: str):
        self.__sentences.append(new)

    def _load(self, filename='sentences.txt'):
        try:
            with open(filename, 'r') as file:
                if file.readable() and len(file.read()) == 0:
                    raise RepositoryError("Empty")
                file.seek(0)
                for line in file:
                    data = line.strip('\n')
                    self.__sentences.append(data)
        except FileNotFoundError as err:
            raise RepositoryError(err)

    def _choose(self):
        self.__chosen_sentence = choice(self.__sentences)

    def sentences(self):
        return self.__sentences

    def chosen(self):
        return self.__chosen_sentence

    def chosen_coded(self):
        return self.__chosen_coded

    def reveal(self, letter: str):
        if letter in self.__letters:
            for i in range(len(self.__chosen_sentence)):
                if self.__chosen_sentence[i] == letter:
                    self.__chosen_coded[i] = self.__chosen_sentence[i]
            self.__letters.remove(letter)
            return True
        return False

    def _coded(self):
        # letters = []
        self.__chosen_coded[0] = self.__chosen_sentence[0]
        self.reveal(self.__chosen_sentence[0])
        self.__chosen_coded[-1] = self.__chosen_sentence[-1]
        self.reveal(self.__chosen_sentence[-1])
        for i in range(1, len(self.__chosen_sentence) - 1):
            if self.__chosen_sentence[i] == " ":
                self.__chosen_coded[i] = " "
            elif self.__chosen_sentence[i + 1] == " " or self.__chosen_sentence[i - 1] == " ":
                self.__chosen_coded[i] = self.__chosen_sentence[i]
                if self.__chosen_sentence[i] not in self.__letters:
                    self.__letters.append(self.__chosen_sentence[i])
                self.reveal(self.__chosen_sentence[i])
            else:
                self.__letters.append(self.__chosen_sentence[i])
        # self.__letters = letters

    def __str__(self):
        coded_sentence = ''.join(letter for letter in self.__chosen_coded)
        return f"{coded_sentence}"

    def won(self):
        if "_" not in self.__chosen_coded:
            return True
        return False
