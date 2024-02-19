from domain.board import BoardError
from domain.game import Game, GameError
from domain.player import Player


class UI(Game):
    def __init__(self):
        super().__init__()

    def get_move(self):
        move = input("Please choose a valid move: ")
        try:
            # symbol should always be X for human
            self.move(move, "X")
            if self.mill_ui(move, self.human):
                removed = self.remove_piece_ui(self.human)
                while not removed:
                    removed = self.remove_piece_ui(self.human)
            comp = self.strategy(move)
            self.move(comp)
            print(f"Computer made a move to {comp}")
            if self.mill_ui(comp, self.computer):
                removed = self.remove_piece_ui(self.computer)
                while not removed:
                    removed = self.remove_piece_ui(self.computer)
            return True
        except BoardError as e:
            print("ERROR: " + str(e))
            return False

    def computer_slide_fly(self):
        if not self.blocked(self.computer) and len(self.computer) > 3:
            from_here, to_here = self.slide_strategy()
            self.slide(self.computer, from_here, to_here)
            print(f"Computer made a move to {to_here}")
            if self.mill_ui(to_here, self.computer):
                self.remove_piece_ui(self.computer)
        elif self.blocked(self.computer):
            self.blocked_game()
        elif not self.blocked(self.computer) and len(self.computer) == 3:
            from_here, to_here = self.fly_strategy()
            self.fly(self.computer, from_here, to_here)
            print(f"Computer made a move to {to_here}")
            if self.mill_ui(to_here, self.computer):
                self.remove_piece_ui(self.computer)

    def sliding(self):
        if not self.blocked(self.human) and len(self.human) > 3:
            move = input("Please choose a valid slide: ")
            try:
                args = move.strip().split(' ')
                if len(args) == 2:
                    mov1 = args[0]
                    mov2 = args[1]
                    self.slide(self.human, mov1, mov2)
                    if self.mill_ui(mov2, self.human):
                        removed = self.remove_piece_ui(self.human)
                        while not removed:
                            removed = self.remove_piece_ui(self.human)
                    self.computer_slide_fly()
                else:
                    print("You must have exactly 2 arguments")
            except GameError as e:
                print("ERROR: " + str(e))
                return False
        elif self.blocked(self.human):
            self.blocked_game()
        elif not self.blocked(self.human) and len(self.human) == 3:
            print("Note that you have 3 pieces left, therefore you can jump wherever.")
            move = input("Please choose a move: ")
            try:
                args = move.strip().split(' ')
                mov1 = args[0]
                mov2 = args[1]
                self.fly(self.human, mov1, mov2)
                if self.mill_ui(mov2, self.human):
                    removed = self.remove_piece_ui(self.human)
                    while not removed:
                        removed = self.remove_piece_ui(self.human)
                self.computer_slide_fly()
            except GameError as e:
                print("ERROR: " + str(e))
                return False
        elif len(self.human) < 3:
            pass

    def mill_ui(self, point, player: Player):
        arg1, arg2, arg3 = self.mill(point, player)
        if arg1:
            if arg3 == "O":
                print(f"Computer formed a mill! {point} - {arg2[0]} - {arg2[1]}")
            elif arg3 == "X":
                print(f"YOU formed a mill! {point} - {arg2[0]} - {arg2[1]}")
        return arg1

    def remove_piece_ui(self, player: Player):
        if player.symbol() == "X":
            remove = input("Please choose a piece of the opponent's to be removed: ")
            try:
                self.remove(remove, self.human, self.computer)
                return True
            except GameError as e:
                print("ERROR: " + str(e))
                return False
        elif player.symbol() == "O":
            try:
                rmv = self.best_remove()
                # print(rmv)
                self.remove(rmv, self.computer, self.human)
                print(f"The computer removed your {rmv} piece.")
                return True
            except GameError as e:
                print("ERROR: " + str(e))
                return False

    def blocked_game(self):
        if self.blocked(self.human):
            game.won = True
            game.winner = self.computer.symbol()
            self.end_game()
        elif self.blocked(self.computer):
            game.won = True
            game.winner = self.human.symbol()
            self.end_game()
        return game.won

    @staticmethod
    def end_game():
        if game.winner == "X":
            print("Congrats! You won!")
        elif game.winner == "O":
            print(f"GAME OVER! Computer won!")
        else:
            print(game.winner)

    def play(self):
        print("PHASE 1: Placing pieces")
        # self.board_display()
        while not self.human.placed_all():
            self.board_display()
            self.get_move()

        print("PHASE 2 and 3: Moving pieces and Flying")
        print("\t Now the sliding started! please enter the values as such: <from here> <to here>")
        while not game.won:
            self.board_display()
            self.sliding()
        # self.end_game()


if __name__ == "__main__":
    game = UI()
    game.play()
