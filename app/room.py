import random
class Room(object):
	def __init__(self, room_name,  room_capacity ):
		self.room_name = room_name
		
		self.room_capacity = room_capacity
		self.room_occupants = []

	def allocate_space(self, person):
		if self.is_full == True:
			return "The room is full try other rooms."
		else:
			room_occupants.append(person)
					

class Office(Room):
	def __init__(self, room_name):
		super(Office, self).__init__(room_name,room_capacity = 6)

	def allocate_office_space(self, person):
			pass

	def is_full(self):
		if len(self.room_capacity) == self.room_capacity:
			return True		
		return len(self.room_capacity)
		
   

class LivingSpace(Room):
    def __init__(self, room_name):
		super(LivingSpace, self).__init__(room_name, room_capacity = 4)

	def allocate_living_space(self, person):
		pass

	def is_full(self):
		if len(self.room_capacity) == self.room_capacity:
			return True		
		return len(self.room_capacity)		
		