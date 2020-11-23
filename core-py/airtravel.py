# sample input for the repl:
# f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
# f.allocate_seat("12A", "Guido van Rossum")
from pprint import pprint as pretty


class Flight:
    """
    A flight with the aircraft
    """

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) < 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{seat: None for seat in seats} for _ in rows]

    def allocate_seat(self, seat, passenger):
        """
        Allocate a seat to a passenger
        :param seat:
        :param passenger:
        :return:
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} taken')
        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat {row_text}')

        if row not in rows:
            raise ValueError(f'Invalid row number {row}')

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already taken")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def num_available_seats(self):
        return sum(
            sum(1 for s in row.values() if s is None)
            for row in self._seating
            if row is not None
        )

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}" \
             f" Flight: {flight_number}" \
             f" Seat: {seat}" \
             f" Aircraft: {aircraft}" \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flight():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("12B", "Rasmus Lerdorf")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15B", "Yukihiro Matsumoto")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat("12A", "Larry Wall")
    g.allocate_seat("12B", "Yukihiro Matsumoto")
    g.allocate_seat("4A", "Brian Kernighah")
    g.allocate_seat("4B", "Dennis Ritchie")

    return f, g


f, g = make_flight()
print(f.aircraft_model(), f.num_available_seats())
print(g.aircraft_model(), g.num_available_seats())
# f.make_boarding_cards(console_card_printer)

print('\nProgram Completed')
