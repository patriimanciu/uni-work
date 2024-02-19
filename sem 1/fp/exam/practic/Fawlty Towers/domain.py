from datetime import date
from texttable import Texttable


class Reservation:
    def __init__(self, _id: int, room_number: int, name: str, number_guests: int, arrival: date, departure: date):
        self.__id = _id
        self.__room = room_number
        self.__name = name
        self.__guests = number_guests
        self.__arrival = arrival
        self.__departure = departure

    def id(self):
        return self.__id

    def room(self):
        return self.__room

    def name(self):
        return self.__name

    def guests(self):
        return self.__guests

    def arrival(self):
        return self.__arrival

    def departure(self):
        return self.__departure


class Rooms:
    def __init__(self):
        self.load_config()
        self.single = 0
        # holds the dates in which it is reserved
        self.single_res = [[] for i in range(self.single)]
        self.double = 0
        self.double_res = [[] for i in range(self.double)]
        self.family = 0
        self.family_res = [[] for i in range(self.family)]

    def load_config(self, filename='rooms.txt'):
        try:
            with open(filename, 'r') as file:
                if file.readable() and len(file.read()) == 0:
                    return
                file.seek(0)
                for line in file:
                    data = line.strip().split(' = ')
                    if data[0] == 'single rooms':
                        self.single = int(data[1])
                    elif data[0] == 'double rooms':
                        self.double = int(data[1])
                    elif data[0] == 'family rooms':
                        self.family = int(data[1])
        except FileNotFoundError:
            pass


class Hotel:
    def __init__(self):
        # key is the unique id
        self.reservations = {}
        self.rooms = Rooms()

    def add(self, _id: int, room: int, name: str, guests: int, arrival_day: int, arrival_mon: int, dep_day: int, dep_mon: int):
        if _id not in self.reservations.keys():
            self.reservations[_id] = Reservation(_id, room, name, guests, date(2023, arrival_mon, arrival_day), date(2023, dep_mon, dep_day))

    def sort_res(self, from_date: date, to_date: date):
        reserv = []
        for res in self.reservations.values():
            if from_date <= res.arrival() <= to_date:
                reserv.append(res)
        ress = sorted(reserv, key=lambda item: (item.arrival(), item.name()))
        return ress

    def __str__(self):
        t = Texttable()
        hed = ["Date", "Name", "Guests", "Room", "ID"]
        t.header(hed)
        for res in self.reservations.values():
            t.add_row([str(res.arrival()) + " - " + str(res.departure()), res.name(), res.guests(), res.room(), res.id()])
        return t.draw()
