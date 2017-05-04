from person import Person, Fellow, Staff
from room import Room, Office, LivingSpace
import random


class Amity(object):
    def __init__(self):
        self.employees = []
        self.rooms = []
        self.allocated_employees = []
        self.unallocated_employees = []
        self.allocated_rooms = {}

    def create_room(self, room_name, room_type):
        if room_type.lower() == "office":
            office = Office(room_name)
            self.rooms.append(office)
            print("Office created successfully.")
        elif room_type.lower() == "living_space":
            living_space = LivingSpace(room_name)
            self.rooms.append(living_space)
            print("Living space created successfully.")
        else:
            return "Invalid room type."

    def add_person(self, name, employee_type, need_accomodation="N"):
        if employee_type.lower() == "fellow":
            if need_accomodation.upper() == "Y":
                fellow = Fellow(name, employee_type, need_accomodation)
                self.employees.append(fellow)
                print("Fellow added successfully.")
                # accomodate fellow
                fellow_space = self.accomodate_fellow()
                if fellow_space != None:
                    if len(fellow_space.room_occupants) < fellow_space.room_capacity:
                        self.allocated_rooms[fellow_space.room_name] = fellow_space.room_occupants.append(name)
                        print("Fellow accomodated successfully.")
                    else:
                        return "Room is full."
            else:
                fellow = Fellow(name, employee_type, need_accomodation)
                self.employees.append(fellow)
                fellow_space = self.accomodate_fellow()
                if fellow_space != None:
                    if len(fellow_space.room_occupants) < fellow_space.room_capacity:
                        self.allocated_rooms[fellow_space.room_name] = fellow_space.room_occupants.append(name)
                        print("Fellow allocated successfully.") 
                    else:
                        return "Room is full."
        elif employee_type.lower() == "staff" :
            staff = Staff(name, employee_type, need_accomodation)
            self.employees.append(staff)
            # allocate staff
            staff_room = self.allocate_employee()
            if staff_room != None:
                if len(staff_room.room_occupants) < staff_room.room_capacity:
                    self.allocated_rooms[staff_room.room_name] = room_occupants.append(name)
                else:
                    return "The office is already full."

        else:
            return "Invalid employee type."

    def allocate_employee(self):
        if len(self.rooms) == 0:
            print("No rooms available.")
        else:
            secure_random = random.SystemRandom()
            random_room = secure_random.choice(self.rooms)
            return random_room
            

    def accomodate_fellow(self):
        if len(self.rooms) == 0:
            print("No rooms available")
        else:
            secure_random = random.SystemRandom()
            random_room = secure_random.choice(self.rooms)
            return random_room

    def reallocate_employee(self):
        pass

    def print_room_occupants(self):
        pass

    def print_allocated_rooms(self):
        pass

    def print_unallocated_room(self):
        pass

    def print_rooms(self):
        pass

    def load_people(self):
        try:
            employees = open("employee.txt", "r")
            for employee in employees.readlines():
                name = employee.split()[0] + " "+ employee.split()[1]
                employee_type = employee.split()[2].lower()
                if len(employee.split()) == 4:
                    need_accomodation = employee.split()[3].upper()
                else:
                    need_accomodation = "N"
                self.add_person(name, employee_type, need_accomodation)     
                
              

        except IOError:
            print ("Error: can\'t find file or read data.")
        else:
            print ("Read content from the file successfully.")     

    def save_people(self):
        pass

amity = Amity()
amity.create_room("camelot", "office")
amity.add_person("Angela Mutava", "fellow", "N")

#print(amity.load_people())
