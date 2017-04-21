#from unittest import TestCase, mock
import mock
from app.amity import Amity
import unittest


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        

    def test_add_person(self):
    	""" This method tests that a person can be added successfully to the system."""
        self.assertEqual(self.amity.add_person("Catherine Mutava", "Staff", "N"),
                         "Employee added successfully.")

    def test_create_room(self):
    	""" This method creates rooms of the given type """
    	self.assertEqual(self.amity.create_room(["Valhalla", "Camelot", "Krypton", "Accra", "Hogwarts"], "Office"), "Rooms created successfully.")
    
    def test_create_room_duplicates(self):
        """ This method creates rooms of the given type """
        self.amity.create_room("Valhalls", "Office")
        self.assertEqual(self.amity.create_room(["Valhalla", "Camelot", "Krypton", "Accra", "Hogwarts"], "Office"), "Sorry system does not allow duplicate rooms.")


    def test_allocate_employee(self):
    	""" This method allocates employee to the office they request."""
    	self.amity.add_person("Catherine Mutava", "Staff", "N")
    	self.amity.create_room(["Hogwarts"], "Office")
        self.assertEqual(self.amity.allocate_employee("Angela Mutava", "Hogwarts"), "Employee allocated successfully.")

    def test_allocate_employee_more_than_6_in_an_office(self):
        """ This method allocates employee to the office they request."""
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.amity.create_room(["Hogwarts"], "Office")
        self.assertEqual(self.amity.allocate_employee("Angela Mutava", "Hogwarts"), "Room is full.Office cannot accomodate more than 6 employees.")

    def test_accomodate_fellow(self):
    	""" This method adds a fellow to the requested."""
    	self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.create_room(["Jade"], "Living Space")
    	self.assertEqual(self.amity.accomodate_fellow("Angela Mutava", "Jade"), "Fellow accomodated successfully.")

    def test_accomodate_fellow_more_than_4_in_living_space(self):
        """ This method adds a fellow to the requested."""
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.add_person("Angela Mutava", "Fellow", "Y")
        self.amity.create_room(["Jade"], "Living Space")
        self.assertEqual(self.amity.accomodate_fellow("Angela Mutava", "Jade"), "A maximum of 4 people in space.")     

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
        sample_path = os.path.dirname(os.path.realpath(__file__))+"/" + sample_file
        self.amity.load_people(file_path)
        self.assertEqual(self.amity.load_people(file_path), sample_file)		    	    	



if __name__ == '__main__':
    unittest.main()
