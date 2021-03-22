# from mix_it.project.vehicle.vehicle import Vehicle
from project.vehicle.vehicle import Vehicle



class Bus(Vehicle):
    def __init__(self, available_seats, ticket_price):
        Vehicle.__init__(self, available_seats)
        self.ticket_price = ticket_price
        self.ticket_sold = 0

    def get_ticket(self, ticket_count):
        try:
            self.get_capacity(self.available_seats, ticket_count)
            self.available_seats -= ticket_count
            self.ticket_sold += ticket_count
        except Exception as ex:
            return str(ex)

    def get_total_profit(self):
        return self.ticket_sold * self.ticket_price

# bus = Bus(10, 5)
# print(bus.get_ticket(11))
# print(bus.get_ticket(9))
# print(bus.get_total_profit())