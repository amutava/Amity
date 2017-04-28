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


    def create_room(self):
		num_rooms = input("How many rooms do you want to create?")
		for rooms in int(num_rooms):
			room_name = input("Enter room name")
			self.rooms.append(room_name)
		print("Rooms added successfully.")	
		return self.rooms			


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


	def allocate_employee(self):
		secure_random = random.SystemRandom()
		random_room = secure_random.choice(self.rooms)


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
  

