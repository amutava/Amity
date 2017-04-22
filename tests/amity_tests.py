#from unittest import TestCase, mock
import mock
from app.amity import Amity
import unittest


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.persons = []
        self.rooms = []
        

    def test_add_person(self):
    	""" This method tests that a person can be added successfully to the system."""
        self.persons.append(self.amity.add_person("Catherine Mutava", "Staff", "N"))
        self.assertGreater(len(self.persons),
                         0)

    def test_add_person_duplicate(self):
        """ This method tests that a person can be added successfully to the system."""
        self.persons.append(self.amity.add_person("Catherine Mutava", "Staff", "N"))
        self.assertIn("Catherine Mutava", self.persons,
                         "Employee with the given name exists in the system.")

    def test_create_room(self):
    	""" This method creates rooms of the given type """
    	self.assertEqual(self.amity.create_room(["Valhalla", "Camelot", "Krypton", "Accra", "Hogwarts"], "Office"), "Rooms created successfully.")
    
    def test_create_room_duplicates(self):
        """ This method creates rooms of the given type """
        self.amity.create_room("Valhala", "Office")
        self.assertEqual(self.amity.create_room(["Valhalla", "Camelot", "Krypton", "Accra", "Hogwarts"], "Office"), "Sorry system does not allow duplicate rooms.")


    def test_allocate_employee(self):
    	""" This method allocates employee to the office they request."""
    	self.amity.add_person("Catherine Mutava", "Staff", "N")
    	self.amity.create_room(["Hogwarts"], "Office")
        self.assertEqual(self.amity.allocate_employee("Catherine Mutava", "Hogwarts"), "Employee allocated successfully.")

    def test_allocate_employee_to_the_same_room(self):
        """ This method allocates employee to the office they request."""
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.create_room(["Hogwarts"], "Office")
        self.amity.allocate_employee("Catherine Mutava", "Hogwarts")
        self.assertEqual(self.amity.allocate_employee("Catherine Mutava", "Hogwarts"), "You already have a space in the room.")    

    def test_allocate_employee_more_than_6_in_an_office(self):
        """ This method allocates employee to the office they request."""
        self.amity.add_person("Christina Sass", "Staff", "N")
        self.amity.add_person("Jeremy Johnson", "Staff", "N")
        self.amity.add_person("Shem Ogumbe", "Staff", "N")
        self.amity.add_person("Maureen Nyakio", "Staff", "N")
        self.amity.add_person("Mirabel Ekwenugo", "Staff", "N")
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.add_person("Angela Mutava", "Fellow", "N")
        self.amity.create_room(["Hogwarts"], "Office")
        self.amity.allocate_employee("Christina Sass", "Hogwarts")
        self.amity.allocate_employee("Jeremy Johnson", "Hogwarts")
        self.amity.allocate_employee("Mirabel Ekwenugo", "Hogwarts")
        self.amity.allocate_employee("Maureen Nyakio", "Hogwarts")
        self.amity.allocate_employee("Shem  Ogumbe", "Hogwarts")
        self.amity.allocate_employee("Angela Mutava", "Hogwarts")

        self.assertEqual(self.amity.allocate_employee("Catherine Mutava", "Hogwarts"), "Room is full.Office cannot accomodate more than 6 employees.")

    def test_accomodate_fellow(self):
    	""" This method adds a fellow to the requested."""
    	self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.create_room(["Jade"], "Living Space")
    	self.assertEqual(self.amity.accomodate_fellow("Angela Mutava", "Jade"), "Fellow accomodated successfully.")

    def test_accomodate_fellow_same_space(self):
        """ This method adds a fellow to the requested."""
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.create_room(["Jade"], "Living Space")
        self.amity.accomodate_fellow("Angela Mutava", "Jade")
        self.assertEqual(self.amity.accomodate_fellow("Angela Mutava", "Jade"), "Fellow already in the given space.")    

    def test_accomodate_fellow_duplicates(self):
        """ This method adds a fellow to the requested."""
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.create_room(["Jade"], "Living Space")
        self.amity.create_room(["Hamilton"], "Living Space")
        self.amity.accomodate_fellow("Angela Mutava", "Jade")
        self.assertEqual(self.amity.accomodate_fellow("Angela Mutava", "Hamilton"), "Fellow can only be accomodated in one room.")

    def test_accomodate_fellow_unregistered(self):
        """ This method adds a fellow to the requested."""
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.create_room(["Jade"], "Living Space")
        self.assertEqual(self.amity.accomodate_fellow("Valeria Chemtai", "Jade"), "Sorry employee not in our system.")

    def test_accomodate_fellow_more_than_4_in_living_space(self):
        """ This method adds a fellow to the requested."""
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.add_person("Rose Wambui", "Fellow", "Y")
        self.amity.add_person("Valeria Chemtai", "Fellow", "Y")
        self.amity.add_person("Joan Awinja", "Fellow", "Y")
        self.amity.add_person("Caroline Wanjiku", "Fellow", "Y")
        self.amity.create_room(["Jade"], "Living Space")
        self.amity.accomodate_fellow("Angela Mutava", "Jade")
        self.amity.accomodate_fellow("Rose Wambui", "Jade")
        self.amity.accomodate_fellow("Valeria Chemtai", "Jade")
        self.amity.accomodate_fellow("Joan Awinja", "Jade")
        self.assertEqual(self.amity.accomodate_fellow("Caroline Wanjiku", "Jade"), "A maximum of 4 people in space.")     

    def test_accomodate_staff(self):
        """ This method adds a fellow to the requested."""
        self.amity.add_person("Christina Sass", "Staff", "N")
        self.amity.create_room(["Jade"], "Living Space")
        self.assertEqual(self.amity.accomodate_fellow("Christina Sass", "Jade"), "Sorry staffs are not accomodated.")    

    def test_reallocate_fellow(self):
    	""" This method reallocates one person from one room to another."""
    	self.amity.add_person("Angela Mutava", "Fellow", "Y")
    	self.amity.create_room(["Camelot", "Krypton"], "office")
    	self.amity.allocate_employee("Angela Mutava", "Camelot")
        self.assertEqual(self.amity.reallocate_employee("Angela Mutava", "Krypton"), "Fellow reallocated successfully.")

    def test_reallocate_fellow_unregistered(self):
        """ This method reallocates one person from one room to another."""
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.create_room(["Camelot", "Krypton"], "office")
        self.amity.allocate_employee("Angela Mutava", "Camelot")
        self.assertEqual(self.amity.reallocate_employee("Valeria Chemtai", "Krypton"), "Sorry the fellow is not added to the system.")

    def test_reallocate_staff(self):
        """ This method reallocates one person from one room to another."""
        self.amity.add_person("Angela Mutava", "Staff", "N")
        self.amity.create_room(["Camelot", "Krypton"], "office")
        self.amity.allocate_employee("Angela Mutava", "Camelot")
        self.assertEqual(self.amity.reallocate_employee("Angela Mutava", "Krypton"), "Staff reallocated successfully.")

    def test_print_rooms(self):
    	""" This method prints all the rooms."""
    	self.amity.create_room(["Valhalla", "Camelot", "Cairo"], "Office")
    	self.assertEqual(self.amity.print_rooms(), ("Valhalla", "Camelot", "Cairo"))

    def test_print_unallocated_rooms(self):
    	"""This method prints the rooms that have not been allocated employees yet."""
    	self.amity.create_room(["Hogwarts", "Camelot"], "Office")
    	self.amity.allocate_employee("Angela Mutava", "Camelot")
    	self.assertEqual(self.amity.print_unallocated_room(), "Hogwarts")
    	

    def test_print_allocated_rooms(self):
    	"""This method prints the rooms that have  been allocated employees yet."""
    	self.amity.create_room(["Hogwarts", "Camelot"], "Office")
    	self.amity.allocate_employee("Angela Mutava", "Camelot")
    	self.assertEqual(self.amity.print_unallocated_room(), "Camelot")

    def test_load_people(self, file_path):
        sample_file = "employees.txt"
        sample_path = os.path.dirname(os.path.realpath(__file__))+ "/" + sample_file
        self.assertEqual(self.amity.load_people(file_path), sample_path)		    	    	



if __name__ == '__main__':
    unittest.main()