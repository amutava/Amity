from unittest import TestCase

from .. app.amity import Amity
from .. app.room import Office, LivingSpace
from .. app.person import Fellow

import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class TestAmity(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_create_room(self):
        """ This method creates rooms of the given type."""
        self.assertEqual(self.amity.create_room(
            "Camelot", "office"), "Office {} created successfully.".format(
            "Camelot"))
        self.assertEqual(self.amity.create_room(
            "Jade", "living_space"),
            "LivingSpace {} created successfully.".format(
            "Jade"))

    def test_create_room_duplicates(self):
        """ This method tests that there are no room duplicates."""
        self.amity.create_room("Camelot", "office")
        self.assertEqual(self.amity.create_room(
            "Camelot", "office"), "{} is already created.".format(
            "Camelot"))
        self.amity.create_room("Jade", "living_space")
        self.assertEqual(self.amity.create_room(
            "Jade", "living_space"), "{} is already created.".format(
            "Jade"))

    def test_invalid_room_type(self):
        """ This method tests that an invalid room type."""
        self.assertEqual(self.amity.create_room(
            "Camelot", "open_office"), "Invalid room type.")

    def test_add_person(self):
        """ This method tests that a person \
        can be added successfully to the system."""
        self.amity.create_room('Camelot', "office")
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'Staff', 'N'),
            "{} a {} added successfully.".format(
            "Catherine Mutava", "Staff"))

    def test_add_person_duplicate(self):
        """ This method tests duplicate additions to the system."""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Catherine Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'Staff', 'N'),
            "{} already in the system".format(
            "Catherine Mutava"))

    def test_invalid_employee_type(self):
        """This method tests that only staff and fellow."""
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'surbodinate', 'N'), "Invalid employee type.")

    def test_accomodate_staff(self):
        """This tests ensures that staff cannot be accomodated."""
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'Staff', 'Y'),
            "Sorry only fellows can be accomodated.")

    def test_reallocation_office(self):
        """This test an employee reallocation to a new office"""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Angela Mutava', 'Staff', 'N')
        self.amity.create_room("Krypton", "office")
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Krypton"), "{} reallocated to {}.".format(
            "Angela Mutava", "Krypton"))

    def test_reallocation_living_space(self):
        """This test an employee reallocation to a new living_space"""
        self.amity.create_room("Jade", "living_space")
        self.amity.add_person('Angela Mutava', 'fellow', 'Y')
        self.amity.create_room("Hamilton", "living_space")
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Hamilton"), "{} reallocated to {}.".format(
            "Angela Mutava", "Hamilton"))

    def test_reallocate_employee_not_registered(self):
        """This tests reallocation of an unregistered\
         employee to a new room."""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Angela Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.reallocate_employee(
            "Mark Mutava", "Camelot"), "{} is not in the system.".format(
                "Mark Mutava"))

    def test_reallocate_employee_to_non_existing_room(self):
        """ This tests reallocation to a room that does not exist."""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Catherine Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.reallocate_employee(
            "Catherine Mutava", "Hogwarts"),
            "Amity has no room with the name {}".format("Hogwarts"))

    def test_reallocate_to_same_office(self):
        """Tests that an employee cannot be reallocated to the same room."""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Mark Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.reallocate_employee(
            "Mark Mutava", "Camelot"),
            "{} cannot be reallocated to the same office.".format(
                "Mark Mutava"))

    def test_reallocate_to_same_living_space(self):
        """Tests that an employee cannot be reallocated to the same room."""
        self.amity.create_room("Jade", "living_space")
        self.amity.add_person('Catherine Mutava', 'fellow', 'Y')
        self.assertEqual(self.amity.reallocate_employee(
            "Catherine Mutava", "Jade"),
            "{} cannot be reallocated to the same living space.".format(
            "Catherine Mutava"))

    def test_reallocate_to_room_of_another_type(self):
        """This tests that an employee cannot be reallocated\
         from an office to a living space and vice versa"""
        self.amity.create_room("Camelot", "office")
        self.amity.create_room("Jade", "living_space")
        self.amity.add_person("Angela Mutava", "staff", "N")
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Jade"), "{} cannot be reallocated to different room type.".format("Angela Mutava"))

    def test_load_people_from_non_existing_file(self):
        """This method tests loading people form a file that doesn't exist."""
        self.amity.create_room("accra", "office")
        self.amity.create_room("Jade", "living_space")
        self.assertEqual(self.amity.load_people("employees.txt"),
                         "Error: can\'t find file or read data.")

    def test_load_people(self):
        """This method tests that people are loaded from a textfile successfully."""
        self.amity.create_room("Jade", "living_space")
        self.amity.create_room("accra", "office")
        self.assertEqual(self.amity.load_people("employee.txt"),
                         "Read content from the file successfully.")

    def test_print_allocations(self):
        """This method tests that allocated employees are added to a textfile."""
        self.amity.create_room("accra", "office")
        self.amity.create_room("Jade", "living_space")
        self.amity.load_people("employee.txt")
        self.assertEqual(self.amity.print_allocations("allocations.txt"), "Allocations has been saved to {}".format(
            "allocations.txt"))

    def test_print_unallocated(self):
        """This method tests that unallocated employees are saved to a textfile."""
        self.amity.create_room("accra", "office")
        self.amity.create_room("Jade", "living_space")
        self.amity.load_people("employee.txt")
        self.assertEqual(self.amity.print_unallocated(
            "unallocated.txt"), "Allocations has been saved to {}".format("unallocated.txt"))

    def test_print_room(self):
        """Tests that all employees are printed to screen."""
        self.amity.create_room("accra", "office")
        self.amity.add_person("Angela Mutava", "staff", "N")
        self.assertEqual(self.amity.print_room("accra"),
                         "Printed all occupants on screen.")

    def test_save_state(self):
        """Tests the save state without any employees in the app"""
        office = Office("accra", "office")
        living_space = LivingSpace("Jade", "living_space")
        self.amity.offices.append(office)
        self.amity.living_spaces.append(living_space)
        self.assertEqual(self.amity.save_state(
            "amity.db"), "Amity has no employees.")

    def test_save_state(self):
        """Tests the save state saves employee to database"""
        office = Office("accra", "office")
        fellow = Fellow("Angela Mutava", "fellow", "Y")
        self.amity.offices.append(office)
        self.amity.employees.append(fellow)
        self.assertEqual(self.amity.save_state("amity.db"),
                         "Employees added to database successfully.")

    def test_check_office(self):
        """Tests whether the object returned is office."""
        office = Office("accra", "office")
        self.amity.offices.append(office)
        self.assertEqual(self.amity.check_office("accra"), office)

    def test_check_employee(self):
        """Tests whether the object returned is office."""
        fellow = Fellow("Angela Mutava", "fellow", "N")
        self.amity.employees.append(fellow)
        self.assertEqual(self.amity.check_employee("Angela Mutava"), fellow)    

    def test_check_living_space(self):
        """Tests whether object returned is living space"""      
        space = LivingSpace("Jade", "living_space")
        self.amity.living_spaces.append(space)
        self.assertEqual(self.amity.check_living_space("Jade"), space)

    def test_check_old_employee_room(self):
        """Tests the previous employee room."""
        office = Office("accra", "office")
        self.amity.offices.append(office)
        self.amity.add_person("Angela Mutava", "fellow", "N")
        self.assertEqual(self.amity.check_old_employee_room("Angela Mutava"), office)

    def test_allocate_employee(self):
        """Tests random office returned"""
        office = Office("accra", "office")
        self.amity.offices.append(office)
        self.assertEqual(self.amity.allocate_employee(), office) 

    def test_accomodate_fellow(self):
        """Tests random living space returned"""
        space = LivingSpace("Jade", "living_space")
        self.amity.living_spaces.append(space)
        self.assertEqual(self.amity.accomodate_fellow(), space) 

    def tearDown(self):
        """To free variables for fresh use in other tests."""
        self.amity.employees = []
        self.amity.offices = []
        self.amity.living_spaces = []
        self.amity.allocated_employees = []
        self.amity.unallocated_employees = []
        self.amity.allocated_rooms = []
        self.amity.unaccomodated_fellows = []

if __name__ == '__main__':
    unittest.main()
