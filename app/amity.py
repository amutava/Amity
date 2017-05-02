from person import Person, Fellow, Staff
from room import Room, Office, LivingSpace
import random


class Amity(object):
	def __init__(self):
		self.employees = []
		self.rooms = []
		self.offices = []
		self.living_spaces = []
		self.allocated_employees = []
		self.unallocated_employees = []
		self.allocated_rooms = {}


    def create_room(self, room_name, room_type):
		if room_type == "office":
			office = Office(room_name)
			self.offices.append(office)
		elif room_type == "living_space":
			living_space = LivingSpace(room_name)
			self.living_spaces.append(living_space)
		else:
			return "Invalid room type."					


	def add_person(self):
		full_name = input("Enter your fullname.")
		employee_type = input("Are you a fellow/staff?")
		if employee_type == "fellow":
			need_accomodation = input("Do you need to be accommodated by Andela? Type N/Y.")
			fellow = Fellow(full_name, employee_type, need_accomodation)
			self.employees.append(fellow)
		else:
			staff = Staff(full_name, employee_type)
			self.employees.append(staff)	


	def allocate_employee(self, person_name):
		secure_random = random.SystemRandom()
		random_room = secure_random.choice(self.rooms)
		office = Office()
		if len(self.allocated_rooms[random_room]) < office.room_capacity:
			self.allocated_rooms[random_room].append(person_name)
		else:
		    return "Room is already full."	


	def accomodate_fellow(self):
		pass

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
		pass

	def save_people(self):
		pass												
  

