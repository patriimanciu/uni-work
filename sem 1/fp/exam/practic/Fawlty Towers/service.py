from domain import Hotel, Reservation


class FileError(Exception):
    pass


class HotelService:
    def __init__(self, hotel: Hotel):
        self.__hotel = hotel

    def load(self, filename='file.txt'):
        try:
            with open(filename, 'r') as file:
                if file.readable() and len(file.read()) == 0:
                    raise FileError("File is empty!")
                file.seek(0)
                for line in file:
                    data = line.strip().split(',')
                    try:
                        _id = int(data[0])
                        room = int(data[1])
                        name = data[2]
                        guests = int(data[3])
                        arrival_day = int(data[4])
                        arrival_mon = int(data[5])
                        dep_day = int(data[6])
                        dep_mon = int(data[7])
                        self.__hotel.add(_id, room, name, guests, arrival_day, arrival_mon, dep_day, dep_mon)
                    except ValueError as err:
                        raise FileError(err)
        except FileNotFoundError as err:
            raise FileError(err)
