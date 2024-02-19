from random import randint


class GameOver(Exception):
    pass


class CityError(Exception):
    pass


class City:
    def __init__(self):
        self.__year = 1
        self.__population = 100
        self.__acres = 1000
        self.__acres_to_plant = 0
        self.__starved = 0
        self.__new_people = 0
        self.__harvest_unit = 3
        self.__rats_ate = 200
        self.__land_price = 20
        self.__grain_in_store = 2800

    @property
    def year(self):
        return self.__year

    @property
    def population(self):
        return self.__population

    @property
    def acres(self):
        return self.__acres

    @property
    def acres_to_plant(self):
        return self.__acres_to_plant

    @property
    def starved(self):
        return self.__starved

    @property
    def new_people(self):
        return self.__new_people

    @property
    def harvest_unit(self):
        return self.__harvest_unit

    @property
    def rats_ate(self):
        return self.__rats_ate

    @property
    def land_price(self):
        return self.__land_price

    @property
    def grain_in_store(self):
        return self.__grain_in_store

    def __str__(self):
        starved = self.__starved
        new_people = self.__new_people
        self.__starved = 0
        self.__new_people = 0
        return f"In year {self.__year} {starved} people starved. {new_people} came to the city. " \
               f"City population is now {self.__population}. City owns {self.__acres} acres of land. " \
               f"Harvest was {self.__harvest_unit} units per acre. Rats ate {self.__rats_ate} units. " \
               f"Land price is {self.__land_price} units per acre. Grain stocks are {self.__grain_in_store} units."

    def change(self, acres, feed, plant):
        grain = acres * self.__land_price
        self.__acres += acres
        self.__grain_in_store -= grain
        self.__grain_in_store -= feed
        people_fed = feed // 20
        if people_fed < self.__population:
            self.__starved = self.__population - people_fed
            if 2 * self.__starved > self.__population:
                raise GameOver("You are a terrible ruler. You let more than half of your population starve.")
            self.__population = people_fed
        self.__acres_to_plant = plant
        self.__grain_in_store -= plant

    def new_year_stat(self):
        if self.__year == 5:
            if self.__population < 100 or self.__acres < 100:
                raise GameOver("You are a terrible ruler. GAME OVER.")
            else:
                raise GameOver("You are a great ruler. You won the game.")
        self.__land_price = randint(15, 25)
        if self.__starved == 0:
            self.__new_people = randint(0, 10)
        self.__population += self.__new_people
        self.__harvest_unit = randint(1, 6)
        self.__grain_in_store += self.__acres_to_plant * self.__harvest_unit
        rats = randint(1,5)
        if rats == 1:
            procent = randint(1,10 )
            self.__rats_ate = procent * self.__grain_in_store // 100
        self.__grain_in_store -= self.__rats_ate
        self.__year += 1
