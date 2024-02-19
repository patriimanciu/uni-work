from city import CityError, GameOver
from controller import Controller


class UI:
    def __init__(self):
        self.__repo = Controller()

    def start(self):
        for i in range(5):
            print(str(self.__repo))
            try:
                acres = int(input("Acres to buy/sell -> "))
                feed = int(input("Units to feed the population -> "))
                plant = int(input("Acres to plant -> "))
                self.__repo.change(acres, feed, plant)
                self.__repo.new_year_stat()
            except CityError as e:
                print(e)
                return
            except GameOver as e:
                print(e)
                break
            except ValueError as e:
                print("Invalid input.")
                return
        print(str(self.__repo))


ui = UI()
ui.start()
