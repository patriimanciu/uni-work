class Command:
    def __init__(self, name, params):
        self.__name = name
        self.__params = params

    def call(self):
        return self.__name(*self.__params)

    def __call__(self, *args, **kwargs):
        return self.call()


class Operation:
    def __init__(self, undo_command: Command, redo_command: Command):
        self.__undo = undo_command
        self.__redo = redo_command

    def undo(self):
        self.__undo()

    def redo(self):
        self.__redo()


class UndoRedoError(Exception):
    pass


class UndoService:
    def __init__(self):
        self.__history = []
        self.undo_index = 0
        self.redo_index = 0
        self.__index = 0

    def record(self, operation: Operation):
        # if self.__index < len(self.__history):
        #    self.__history = self.__history[:self.__index]
        self.__history.append(operation)
        self.__index += 1

    def undo(self):
        # print("undo", self.__index)
        # print(self.__history[self.__index])
        if self.__index == 0:
            raise UndoRedoError("Nothing to undo! ")
        self.__index -= 1
        self.__history[self.__index].undo()

    def redo(self):
        # print("redo", self.__index)
        if self.__index >= len(self.__history):
            raise UndoRedoError("Nothing to redo! ")

        self.__history[self.__index].redo()
        self.__index += 1

    def list_history(self):
        return self.__history

    def reset_history(self):
        self.__history = []
        self.__index = 0
