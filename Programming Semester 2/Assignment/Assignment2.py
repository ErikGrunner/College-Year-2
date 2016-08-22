__author__ = 'Ciaran'
"""
Object orientated programming
Aaignment 2
Date:3/04/2015
The aim of this assignment was to create a lift simulator using 3 classes, Building, person, and elevator.
My program is relatively simple with all the necessary code contained within main()
The elevator starts off at a random floor with the user entering the number of floors and the number of people in the building
wanting to use the elevator.
The program outputs the location of the people in the building and where they want to go before the elevator starts moving, after this the elevator is shown to be moving towards
the first customer.
It goes through all customers and when all customers are where they want to be the simulation ends



"""
import random
import time

class Building(object):
    """Docstring for the class Building
    This class is fairly simple it holds the variable for the building ie how many people are in the building, how many floors
    are in the building etc"""
    def __init__(self,no_elevators,no_floors,no_people ):
        self.no_elevators=no_elevators
        self.no_floors=no_floors
        self.no_people=no_people




class Elevator(object):
    """Again this is fairly simple this class is the elevator class and it holds the data for what floor the elevator is on and how many people are in the
    elevator
    """
    current_floor=1
    def __init__(self,no_people_elevator=0,current_floor=1,next_floor=0 ):
        self.no_people_elevator=no_people_elevator
        self.current_floor=current_floor
        self.next_floor=next_floor


class Person(object):
    """This is the class for people, it holds the id number for the instance of the class as well as generating a random floor for the person
    to be on as well as generating a random floor for them to want to go to, it also holds the flag for whether the person is waiting for the elevator
    whether the in the elevator or whether they have been delivered
    """
    def __init__(self,id,current_floor=0,wanted_floor=0,in_elevator=0):
        self.id=id
        self.current_floor=random.randint(1,Building.no_floors)#code to generate a random floor for the person to be on
        self.wanted_floor=random.randint(1,Building.no_floors)#code to generate a random floor fo them to want to go to
        self.in_elevator=in_elevator#flag


def main():#main program
    cus_list=[]
    current_floor=[]
    wanted_floor=[]
    in_elevator=[]
    check1=0

    while(check1==0):#Loop to validate user input, if the user enters in an invalid character they get a message telling them so
        try:
            Building.no_people=int(input("How many Customers will there be?"))
            Building.no_floors=int(input("How many Floors will there be?"))
            check1=1
        except ValueError:
            print("Invalid input, please input a number")


    Elevator.current_floor=random.randint(1,Building.no_floors)#random floor for the elevator to start on

    j=-1
    for i in range (1,int(Building.no_people)+1):#creates multiple instances of  a  person
        cus_list.append(Person(i))

    for i in range (1,int(Building.no_people)+1):#Places random values into variables for the instances of the person
        current_floor.append(Person(i).current_floor)
        wanted_floor.append(Person(i).wanted_floor)
        in_elevator.append(Person(i).in_elevator)

    check=0
    for i in range (1,int(Building.no_people)+1):#This is the main part of the program
        in_elevator[j]=0
        j+=1
        k=-1
        if check==0:
            for i in range (1,int(Building.no_people)+1):#prints the location of each person in the building and where they want to go
                k+=1
                print("Current position of customer",current_floor[k])
                print("Current position of wanted floor",wanted_floor[k])
                check=1

        print("Elevator Current Position",Elevator.current_floor)
        while in_elevator[j]!=2:#loop for the elevator will end when everyone has got to their desired floors
            k=-1
            for i in range (1,int(Building.no_people)+1):#go through every person and see if anyone is at the floor and whants to get on
                        k+=1
                        if Elevator.current_floor==current_floor[k] and in_elevator[k]!=1 and in_elevator[k]!=2:#checks to see if the person here has already gotten on or has
                            # already been delivered
                            in_elevator[k]=1#sets their flag
                            print("Person Collected")
                            #checks through all the people to see if any of them have to get of at the current floor
                        if Elevator.current_floor==wanted_floor[k] and in_elevator[k]==1:
                            in_elevator[k]=2
                            print("Person Dropped off")

            if Elevator.current_floor<current_floor[j] and in_elevator[j]!=1 and in_elevator[j]!=2:#checks to see if the person that has pressed the button is above them
                #and moves the elevator towards them
                k=-1
                Elevator.current_floor+=1
                time.sleep(.5)
                print("Elevator Current Position",Elevator.current_floor)


            elif Elevator.current_floor>current_floor[j] and in_elevator[j]!=1 and in_elevator[j]!=2:#checks to see if there below them
                k=-1
                Elevator.current_floor-=1
                time.sleep(.5)
                print("Elevator Current Position",Elevator.current_floor)



            if Elevator.current_floor==wanted_floor[j] and in_elevator[j]==1:#If someone has been collected ie their flag has been set to 1
                #they are registered as being collected and if they are at the floor they want to go to they are registered as being delivered
                in_elevator[j]=2
                print("Person Dropped off")
                k=-1



            elif Elevator.current_floor<wanted_floor[j] and in_elevator[j]==1:#checks to see if the elevator has to go up to deliver someone
                Elevator.current_floor+=1
                time.sleep(.5)
                print("Elevator Current Position",Elevator.current_floor)
                k=-1
                for i in range (1,int(Building.no_people)+1):
                    k+=1
                    if Elevator.current_floor==wanted_floor[k] and in_elevator[k]==1:
                            in_elevator[k]=2
                            print("Person Dropped off")


            elif Elevator.current_floor>wanted_floor[j] and in_elevator[j]==1:#checks to see if the elevator has to go down to deliver someone
                Elevator.current_floor-=1
                time.sleep(.5)
                print("Elevator Current Position",Elevator.current_floor)
                k=-1
                for i in range (1,int(Building.no_people)+1):
                    k+=1
                    if Elevator.current_floor==wanted_floor[k]  and in_elevator[k]==1:
                            in_elevator[k]=2
                            print("Person Dropped off")




main()#starts the program