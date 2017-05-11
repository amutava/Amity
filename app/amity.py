import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from  person import Fellow, Staff
from  room import Office, LivingSpace
from  model import Base, Employees, Offices, LivingSpaces

engine = create_engine('sqlite:///amity_db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


class Amity(object):
    employee = []

    def __init__(self):
        self.employees = []
        self.offices = []
        self.living_spaces = []
        self.allocated_employees = []
        self.unallocated_employees = []
        self.allocated_rooms = []
        self.unaccomodated_fellows = []

    def create_room(self, room_name, room_type):

        if room_type.lower() == "office":
            if [office
                for office in self.offices
                    if room_name == office.room_name]:
                return "{} is already created.".format(room_name)

            else:
                office = Office(room_name)
                self.offices.append(office)
                return "Office {} created successfully.".format(room_name)

        elif room_type.lower() == "living_space":
            if [living_space
                    for living_space in self.living_spaces
                    if room_name == living_space.room_name]:
                return "{} is already created.".format(room_name)
            else:
                living_space = LivingSpace(room_name)
                self.living_spaces.append(living_space)
                return "LivingSpace {} created successfully.".format(room_name)
        else:
            return "Invalid room type."

    def add_person(self, name, employee_type, need_accomodation= "N"):
        if name in [employee.name for employee in self.employees]:
            return "{} already in the system".format(name)
        else:
            if employee_type.lower() == "fellow":
                fellow_office = self.allocate_employee()
                if need_accomodation.upper() == "Y":
                    fellow = Fellow(name, employee_type, need_accomodation)
                    self.employees.append(fellow)
                    fellow_space = self.accomodate_fellow()
                    if fellow_space:
                        fellow_space.room_occupants.append(name)
                        return "{}  a {} accomodated in living space.".format(
                            name, employee_type)
                        self.allocated_rooms.append(fellow_space)
                    else:
                        self.unaccomodated_fellows.append(name)
                        return "Room is full."
                else:
                    fellow = Fellow(name, employee_type, need_accomodation)
                    self.employees.append(fellow)
                    fellow_office = self.allocate_employee()
                    if fellow_office:
                        fellow_office.room_occupants.append(name)
                        return "{}  a {} added in the office space.".format(
                            name, employee_type)
                    else:
                        self.unallocated_employees.append(name)
                        return "Room is full."
            elif employee_type.lower() == "staff":
                if need_accomodation.upper() == "Y":
                    return "Sorry only fellows can be accomodated."
                else:
                    staff = Staff(name, employee_type, need_accomodation)
                    self.employees.append(staff)
                    staff_room = self.allocate_employee()
                    if staff_room:
                        staff_room.room_occupants.append(name)
                        return "{} a {} added successfully.".format(
                            name, employee_type)
                    else:
                        self.unallocated_employees.append(name)
                        return "The office is already full."

            else:
                return "Invalid employee type."

    def allocate_employee(self):
        if len(self.offices) == 0:
            print("No office space available.")
        else:
            secure_random = random.SystemRandom()
            random_room = secure_random.choice(self.offices)
            if len(random_room.room_occupants) < random_room.room_capacity:
                return random_room

    def accomodate_fellow(self):
        if len(self.living_spaces) == 0:
            print("No living space available.")
        else:
            secure_random = random.SystemRandom()
            random_room = secure_random.choice(self.living_spaces)
            if len(random_room.room_occupants) < random_room.room_capacity:
                return random_room

    def reallocate_employee(self, employee_name, new_room_name):
        #import ipdb
        #ipdb.set_trace()
        if self.check_employee(employee_name):
            if self.check_office(new_room_name):
                if self.check_old_employee_room(
                        employee_name).room_name == new_room_name:
                    return "{} cannot be reallocated to the same office.".\
                        format(
                            employee_name)
                else:
                    for offices in self.offices:
                        if new_room_name == offices.room_name:
                            if len(offices.room_occupants) < 6:
                                self.check_old_employee_room(
                                    employee_name).room_occupants.\
                                    remove(employee_name)
                                offices.room_occupants.append(employee_name)
                                return "{} reallocated to {}.".format(
                                    employee_name, new_room_name)
                            else:
                                return "{} if full.".format(new_room_name)

            elif self.check_living_space(new_room_name):
                if self.check_old_employee_room(employee_name).\
                        room_name == new_room_name:
                    return "{} cannot be reallocated to the same living space.".\
                        format(employee_name)
                else:
                    for spaces in self.living_spaces:
                        if new_room_name == spaces.room_name:
                            if len(spaces.room_occupants) < 4:
                                self.check_old_employee_room(
                                    employee_name).room_occupants.\
                                    remove(employee_name)
                                spaces.room_occupants.append(employee_name)
                                return "{} reallocated to {}.".format(
                                    employee_name, new_room_name)
                            else:
                                return "{} if full.".format(new_room_name)
            else:
                return "Amity has no room with the name {}".\
                    format(new_room_name)
        else:
            return "{} is not in the system.".format(
                employee_name)

    def print_room(self, room_name):
        """This methods the people in the room name passed."""
        for rooms in self.offices + self.living_spaces:
            if rooms.room_name == room_name:
                print("---------occupants----------")
                for occupants in rooms.room_occupants:
                    print(occupants)

    def print_allocations(self, filename):
        people = ""

        for rooms in self.living_spaces + self.offices:
            people += rooms.room_name +"\n"
            people += '-' * 20 + '\n'
            if len(rooms.room_occupants) > 0:
                people += "\n".join(rooms.room_occupants)

            else:
                return "{} is empty.".format(rooms.room_name)

        if filename:
            with open(filename, "w") as output_file:
                output_file.write(people)
                print ("Allocations has been saved to {}".format(
                    filename))
        return people

    def print_unallocated(self, filename):
        employees = ""
        if len(self.unallocated_employees) == 0:
            for employees in self.unallocated_employees:
                employees += "\n".join(employees)

        else:
            return "All the employees are allocated rooms"

        if filename:
            with open(filename, "w") as output_file:
                output_file.write(employees)
                print ("Allocations has been saved to {}".format(
                    filename))
        return employees

    def check_office(self, room_name):
        """A helper method to check a room_name is an office."""
        for office in self.offices:
            if room_name == office.room_name:
                return True

    def check_living_space(self, room_name):
        """A helper method to check a room_name is a living space."""
        for space in self.living_spaces:
            if room_name == space.room_name:
                return True

    def check_employee(self, employee_name):
        """A helper method to check an employee
         from a list of all employees."""
        for employee in self.employees:
            if employee.name == employee_name:
                return employee

    def check_old_employee_room(self, employee_name):
        """A helper method to check the room an \
        employee was initially allocated."""
        for rooms in self.offices + self.living_spaces:
            if employee_name in [
                    occupants for occupants in rooms.room_occupants]:
                return rooms

    def load_state(self, db_name=None):
        # gets the employees from the employee table
        try:
            get_employee = session.query(Employees).one()
            name = get_employee.employee_name
            employee_type = get_employee.employee_type
            need_accomodation = get_employee.need_accomodation
            fellow = Fellow(name, employee_type, need_accomodation)
            self.employees.append(fellow)
            print("Employee data obtained successfully.")
        except MultipleResultsFound:
            get_employees = session.query(Employees).all()
            for employee in get_employees:
                name = employee.employee_name
                employee_type = employee.employee_type
                need_accomodation = employee.need_accomodation
                fellow = Fellow(name, employee_type, need_accomodation)
                self.employees.append(fellow)
            print("All employee data obtained successfully.")

        except NoResultFound:
            print("The employees table is empty.")

        # gets the offices from the office table
        try:
            get_office = session.query(Offices).one()
            room_name = get_office.room_name
            room_capacity = get_office.room_capacity
            room_occupants = get_office.room_occupants.split(',')
            office = Office(room_name)
            self.offices.append(office)
            get_office.room_occupants = room_occupants
            print("Office data obtained successfully.")
        except MultipleResultsFound:
            get_offices = session.query(Offices).all()
            for offices in get_offices:
                room_name = offices.room_name
                room_capacity = offices.room_capacity
                room_occupants = offices.room_occupants.split(',')
                office = Office(room_name)
                self.offices.append(office)
                office.room_occupants = room_occupants
            print("All office data obtained successfully.")

        except NoResultFound:
            print("The employees table is empty.")

        # gets livingspaces from the living_spaces table living_spaces
        try:
            get_living_spaces = session.query(Employees).one()
            room_name = get_office.room_name
            room_capicity = get_office.room_capacity
            room_occupants = get_office.room_occupants.split(',')
            space = LivingSpace(room_name)
            self.living_spaces.append(space)
            print("Livingspace data obtained successfully.")
        except MultipleResultsFound:
            get_living_spaces = session.query(LivingSpaces).all()
            for spaces in get_living_spaces:
                room_name = spaces.room_name
                room_capacity = spaces.room_capacity
                room_occupants = spaces.room_occupants.split(',')
                space = LivingSpace(room_name)
                self.living_spaces.append(space)
                spaces.room_occupants = room_occupants
            print("All livingspace data obtained successfully.")

        except NoResultFound:
            print("The employees table is empty.")

    def load_people(self, filename):
        """This method loads people from a \
        text file and adds them to the system."""
        try:
            employees = open(filename, "r")
            for employee in employees.readlines():
                name = employee.split()[0] + " " + employee.split()[1]
                employee_type = employee.split()[2].lower()
                if len(employee.split()) == 4:
                    need_accomodation = employee.split()[3].upper()
                else:
                    need_accomodation = "N"
                self.add_person(name, employee_type, need_accomodation)
                print("added employees")        

        except IOError:
            return "Error: can\'t find file or read data."
        else:
            return "Read content from the file successfully."        

    def save_state(self, db_name):
        """This methods saves the people in the app to a database"""

        if len(self.employees) > 0:
            for employees in self.employees:
                employee = Employees(
                    employees.name, employees.employee_type,
                    employees.need_accomodation)
                try:
                    session.add(employee)
                    session.commit()
                    print("Employees added to database successfully.")
                except Exception as e:
                    print("-------Error-------: {}".format(e))
                    session.rollback()
        else:
            print("Amity has no employees.")

        if len(self.offices) > 0:
            for rooms in self.offices:
                office_occupants = ','.join(rooms.room_occupants)
                office = Offices(
                    rooms.room_name, rooms.room_capacity, office_occupants)
                try:
                    session.add(office)
                    session.commit()
                    print("Offices added to database successfully.")
                except Exception as e:
                    print("-------Error-------: {}".format(e))
                    session.rollback()
        else:
            print("Amity has no offices.")

        if len(self.living_spaces) > 0:
            for spaces in self.living_spaces:
                space_occupants = ','.join(spaces.room_occupants)
                spaces = LivingSpaces(spaces.
                                      room_name, spaces.room_capacity,
                                      space_occupants)
                try:
                    session.add(spaces)
                    session.commit()
                    print("LivingSpaces added to database successfully.")
                except Exception as e:
                    print("-------Error-------: {}".format(e))
                    session.rollback()
        else:
            print("Amity has no living spaces.")

    def get_employees(self):
        """This methods returns all employee objects."""
        for employees in self.employees:
            return employees

