import unittest
from app.allocations import Person, Fellow, Staff, Amity, Room, Office, LivingSpace


class TestAmity(unittest.TestCase):

	def setUp(self):
		self.person = Person()
		self.fellow = Fellow()
		self.amity = Amity()
		self.office = Office()
		self.livingspace = LivingSpace()
		self.room = Room()

	def test_create_room(self):
		"""
		This method tests the create room functionality with the correct parameters passed for create room.
		"""
		self.assertEqual(self.amity.create_room(
			"Valhalla", "Living Space", 6), "Room created successfully.")

	def test_room_name(self):
	 	"""
		This method tests if staff has been added to room.
		"""

	 	self.assertEqual(self.amity.create_room(
			"", "Living Space", 6), "Add the room name.")

	def test_the_space_office(self):
		"""
		This method checks create room providesthe space parameter.
		"""
		self.assertEqual(self.amity.create_room(" Valhalla",
			" ", 6), "Do you want to create room/living space?")    

	def test_raises_value_error_if_x_parameter_is_invalid(self):
		"""
		This method tests that the room name is a valid argument.
		"""
		self.assertRaises(ValueError, self.amity.create_room,
						  12, "Living Space", 4)

	def test_raises_value_error_if_y_parameter_is_invalid(self):
		"""
		This method tests that the room capacity is a number.
		"""
		self.assertRaises(ValueError, self.amity.create_room,
						  "Camelot", "Office", 6)

	def test_raises_value_error_if_Z_parameter_is_invalid(self):
		"""
		This method tests that the room capacity is a number.
		"""
		self.assertRaises(ValueError, self.amity.create_room,
						  "Camelot", "Office", "4")

	def test_living_space_capacity(self):
		"""
		This method tests that office space capacity is 6.
		"""
		self.assertEqual(self.office.capacity, 6)

	def test_office_capacity(self):
		"""
		This method tests that living space capacity is 4.
		"""
		self.assertEqual(self.livingspace.capacity, 4)

	def test_add_fellow(self):
		"""
		This method adds a person to a room.
		"""
		self.assertEqual(self.room.add_person(
			"Angela Mutava", "Fellow", "Camelot"), "Fellow added successfuly to the room.")
	
	def test_the_fellow_added_room(self):
		"""
		This method tests if fellow has been added to room.
		"""
		self.assertEqual(self.room.add_person(
			"Angela Mutava", "Fellow", " "), "Add the room you want to be allocated to.")

	def test_the_fellow_added_name(self):
		"""
		This method checks fellow added name.
		"""
		self.assertEqual(self.room.add_person(" ",
			"Fellow", "Camelot"), "You didn't provide your name.")

	def test_the_employee_type_added_name(self):
		"""
		This method checks fellow added name.
		"""
		self.assertEqual(self.room.add_person("Angela Mutava",
			"", "Camelot"), "Are you a fellow/staff.")


	def test_add_staff(self):
		"""
		This method adds a person to a room.
		"""
		self.assertEqual(self.room.add_person(
			"Catherine Mutava", "Staff", "Camelot"), "Staff added successfuly to the room.")

	def test_the_staff_added_room(self):
		"""
		This method tests if staff has been added to room.
		"""
		self.assertEqual(self.room.add_person(
			"Catherine Mutava", "Staff", " "), "Add the room you want to be allocated to.")

	def test_the_staff_added_name(self):
		"""
		This method checks fellow added name.
		"""
		self.assertEqual(self.room.add_person("",
			"Staff", "Camelot"), "You didn't provide your name.")

	def test_the_employee_type_added_name(self):
		"""
		This method checks fellow added name.
		"""
		self.assertEqual(self.room.add_person("Angela Mutava",
			"", "Camelot"), "Are you a fellow or staff?")            

	def test_reallocation(self):
		"""This method tests whether a person has been reallocated successfully """
		self.assertEqual(self.room.reallocate(
			"Angela Mutava", "Valhalla"), "Person reallocated successfully.")

	def test_room_for_reallocation(self):
		"""This method tests whether a person has been reallocated successfully """
		self.assertEqual(self.room.reallocate(
			"Angela Mutava", ""),"Which room do you want to be realocated to?")

	
if __name__ == '__main__':
	unittest.main()
