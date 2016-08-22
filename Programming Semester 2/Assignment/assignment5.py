__author__ = 'Ciaran'

import random

class Elevator(object):
    def __init__(self, num_of_floors, register_list, direction = "up", cur_floor=1):
        self.total_floors = num_of_floors
        self.reg_list = register_list
        self.floor = cur_floor
        self.direct = direction
    def move(self):
        """Moves the elevator one floor"""
        if self.total_floors == self.floor:
            self.direct = "down"
        if self.direct == "up":
            self.floor += 1
        else:
            self.floor -= 1
    def register_customer(self, customer):
        self.reg_list.append(customer)
    def cancel_customer(self, customer):
        self.reg_list.remove(customer)

class Building(object):
    def __init__(self, num_of_floors, customer_list, elevator):
        self.total_floors = num_of_floors
        self.customers = customer_list
    def run(self):
        while elevator.floor != 0:
            for customer in self.customers:
                if elevator.floor == customer.on_floor:
                    elevator.reg_list.append(customer)
                    customer.indicator = 1
                elif elevator.floor == customer.going_floor:
                    elevator.reg_list.remove(customer)
                    customer.indicator = 0
                    customer.fin = 1
            elevator.move()

    def output(self):
        pass

class Customer(object):
    def __init__(self, ID, num_of_floors, cur_floor=0, dst_floor=0, in_elevator[j]=0, finished=0):
        self.ident = ID
        self.indicator = in_elevator[j]
        self.fin = finished
        cur_floor = random.randint(1, num_of_floors)
        self.on_floor = cur_floor
        dst_floor = random.randint(1, num_of_floors)
        while dst_floor == cur_floor:
            dst_floor = random.randint(1, num_of_floors)
        self.going_floor = dst_floor


customer_count = int(input("How many customers are in the building?: "))
floor_count = int(input("How many floors does the building have?: "))
cus_list = []
for i in range(1, customer_count+1):
    cus_list.append(Customer(i, floor_count))
elevator = Elevator(floor_count, cus_list)
building = Building(floor_count, cus_list, elevator)
