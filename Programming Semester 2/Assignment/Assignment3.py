__author__ = 'Ciaran'
import random
import time

class Building(object):

    def __init__(self,no_elevators,no_floors,no_people ):
        self.no_elevators=no_elevators
        self.no_floors=no_floors
        self.no_people=no_people
    no_floors=4




class Elevator(object):
    current_floor=1
    def __init__(self,no_people_elevator=0,current_floor=1,next_floor=0 ):
        self.no_people_elevator=no_people_elevator
        self.current_floor=current_floor
        self.next_floor=next_floor
    def move(self):
        cus_list=[]
        current_floor=[]
        wanted_floor=[]
        in_elevator=[]

        j=-1
        for i in range (1,int(Building.no_people)+1):
            cus_list.append(Person(i))

        for i in range (1,int(Building.no_people)+1):
            current_floor.append(Person(i).current_floor)
            wanted_floor.append(Person(i).wanted_floor)
            in_elevator.append(Person(i).in_elevator)

        check=0
        for i in range (1,int(Building.no_people)+1):
            in_elevator[j]=0
            j+=1
            k=-1
            if check==0:
                for i in range (1,int(Building.no_people)+1):
                    k+=1
                    print("Current position of customer",current_floor[k])
                    print("Current position of wanted floor",wanted_floor[k])
                    check=1

            print("Elevator Current Position",Elevator.current_floor)
            while in_elevator[j]!=2:
                time.sleep(1)
                k=-1
                for i in range (1,int(Building.no_people)+1):
                            k+=1
                            if Elevator.current_floor==current_floor[k]and in_elevator[k]!=1 and in_elevator[k]!=2:
                                in_elevator[k]=1
                                print("Person Collected")
                if Elevator.current_floor==current_floor[j] and in_elevator[j]!=1  and in_elevator[j]!=2:
                        in_elevator[j]=1
                        k=-1
                        print("Elevator Current Position",Elevator.current_floor)
                        print("Person Collected")

                        for i in range (1,int(Building.no_people)+1):
                            k+=1
                            if Elevator.current_floor==current_floor[k] and in_elevator[k]!=1 and in_elevator[k]!=2:
                                in_elevator[k]=1
                                print("Person Collected")

                elif Elevator.current_floor<current_floor[j] and in_elevator[j]!=1 and in_elevator[j]!=2:
                    k=-1
                    Elevator.current_floor+=1
                    print("Elevator Current Position",Elevator.current_floor)
                    for i in range (1,int(Building.no_people)+1):
                        k+=1
                        if Elevator.current_floor==current_floor[k] and in_elevator[k]!=1 and in_elevator[k]!=2:
                            in_elevator[k]=1
                            print("Person Collected")


                elif Elevator.current_floor>current_floor[j] and in_elevator[j]!=1 and in_elevator[j]!=2:
                    k=-1
                    Elevator.current_floor-=1
                    print("Elevator Current Position",Elevator.current_floor)
                    for i in range (1,int(Building.no_people)+1):
                        k+=1
                        if Elevator.current_floor==current_floor[k] and in_elevator[k]!=1 and in_elevator[k]!=2:
                                in_elevator[k]=1
                                print("Person Collected")



                if Elevator.current_floor==wanted_floor[j] and in_elevator[j]==1  :
                    in_elevator[j]=2
                    print("Person Dropped off")
                    k=-1
                    for i in range (1,int(Building.no_people)+1):
                        k+=1
                        if Elevator.current_floor==wanted_floor[k] and in_elevator[k]==1:
                                in_elevator[k]=2
                                print("Person Dropped off")



                elif Elevator.current_floor<wanted_floor[j] and in_elevator[j]==1:
                    Elevator.current_floor+=1
                    print("Elevator Current Position",Elevator.current_floor)
                    k=-1
                    for i in range (1,int(Building.no_people)+1):
                        k+=1
                        if Elevator.current_floor==wanted_floor[k] and in_elevator[k]==1:
                                in_elevator[k]=2
                                print("Person Dropped off")
                elif Elevator.current_floor>wanted_floor[j] and in_elevator[j]==1:
                    Elevator.current_floor-=1
                    print("Elevator Current Position",Elevator.current_floor)
                    k=-1
                    for i in range (1,int(Building.no_people)+1):
                        k+=1
                        if Elevator.current_floor==wanted_floor[k]  and in_elevator[k]==1:
                                in_elevator[k]=2
                                print("Person Dropped off")

class Person(object):

    def __init__(self,id,current_floor=0,wanted_floor=0,in_elevator=0):
        self.id=id
        self.current_floor=random.randint(1,Building.no_floors)
        self.wanted_floor=random.randint(1,Building.no_floors)
        self.in_elevator=in_elevator


def main():

    Building.no_people=input("How many Customers will there be?")
    Elevator.move(self)




main()