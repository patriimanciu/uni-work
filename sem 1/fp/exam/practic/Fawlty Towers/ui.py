from datetime import date

from texttable import Texttable

from domain import Hotel
from service import HotelService


class UI:
    def __init__(self):
        self.__hotel = Hotel()
        self.__service = HotelService(self.__hotel)

    def print_sorted(self):
        res = self.__hotel.sort_res(date(2023, 1, 1), date(2023, 12, 31))
        t = Texttable()
        head = ["Date", "Name", "Guests"]
        t.header(head)
        for i in res:
            t.add_row([i.arrival(), i.name(), i.guests()])
        return t.draw()

    def monthly_report(self, month: int):
        t = Texttable()
        d = date(2023, month, 1)
        begin = d.weekday()
        head = ["M", "T", "W", "T", "F", "S", "S"]
        t.header(head)
        first_row = [" " for i in range(begin)]
        day = 1
        while begin < 7:
            first_row.append(f"{day} / ?")
            day += 1
            begin += 1
        t.add_row(first_row)
        while day < 31:
            row = []
            new = 0
            while new < 7 and day < 31:
                row.append(f"{day} / ?")
                day += 1
                new += 1
            if new < 7:
                for i in range(7 - new):
                    row.append(" ")
            t.add_row(row)
        return t.draw()


    def start(self):
        self.__service.load()
        print(str(self.__hotel))
        print(self.print_sorted())
        print(self.monthly_report(2))


if __name__ == "__main__":
    ui = UI()
    ui.start()
