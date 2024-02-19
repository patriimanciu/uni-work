from city import City, CityError


class Controller:
    def __init__(self):
        self.__repo = City()

    def change(self, acres, feed, plant):
        grain = acres * self.__repo.land_price
        if grain > self.__repo.grain_in_store and grain > 0:
            raise CityError("You don't have enough grain to buy this much land.")
        if acres < 0 and abs(acres) > self.__repo.acres:
            raise CityError("You don't have enough acres to sell.")
        if feed > self.__repo.grain_in_store:
            raise CityError("You don't have enough grain to feed the population.")
        if plant > self.__repo.acres:
            raise CityError("You don't have enough acres to plant.")
        if plant > self.__repo.population * 10:
            raise CityError("You don't have enough population to plant this much land.")
        if plant > self.__repo.grain_in_store - feed:
            raise CityError("You don't have enough grain to plant this much land.")
        self.__repo.change(acres, feed, plant)

    def new_year_stat(self):
        self.__repo.new_year_stat()

    def __str__(self):
        return str(self.__repo)