__author__ = 'Ciaran'

class Building:
    no_people=0
    no_floors=0
    no_elevators=0

    def __init__(self,no_elevators,no_floors,no_people ):
        self.no_elevators=no_elevators
        self.no_floors=no_floors
        self.no_people=no_people





class Elevator:
    no_people_elevator=0
    current_floor=0
    next_floor=0

    def __init__(self,no_people_elevator,current_floor,next_floor ):
        self.no_people_elevator=no_people_elevator
        self.current_floor=current_floor
        self.next_floor=next_floor


class Person:
    current_floor=0
    wanted_floor=0
    elevator_called=0

    def __init__(self,current_floor,wanted_floor,elevator_called):
        self.current_floor=current_floor
        self.wanted_floor=wanted_floor
        self.elevator_called=elevator_called

def main():
    Building.no_floors=3
    Building.no_people=1

    Elevator.current_floor=1

    Person.current_floor=3
    Person.wanted_floor=1



