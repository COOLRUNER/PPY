class Event:
    def __init__(self, name, date, ticket_price):
        self.name = name
        self.date = date
        self.ticket_price = ticket_price


class Concert(Event):
    def __init__(self, capacity, name, date, ticket_price):
        super().__init__(name, date, ticket_price)
        self.capacity = capacity

    def get_info(self):
        print(f"{self.name} {self.date} {self.ticket_price} {self.capacity}")


class Ticket:
    def __init__(self, event, seat_number):
        self.event = event
        self.seat_number = seat_number


class TicketReservationSystem:
    def __init__(self):
        self.events = []
        self.takenSeats = []

    def add_event(self):
        self.events.append(Event)

    def show_events(self):
        for event in self.events:
            print(event.name)

    def make_reservation(self, event, seat_number):
        self.takenSeats.append(seat_number)

    def show_taken_seats(self):
        for seat in self.takenSeats:
            print(seat)

    def cancel_reservation(self, seat_number):
        self.takenSeats.remove(seat_number)
