from unittest import TestCase, mock
from unittest.mock import patch, Mock

from app.amity import Amity
from app.room import Room, Office, LivingSpace



class TestAmity(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_create_room(self):
        """ This method creates rooms of the given type."""
        self.assertEqual(self.amity.create_room(
            "Camelot", "office"), "Office {} created successfully.".format(
            "Camelot"))
        self.assertEqual(self.amity.create_room(
            "Jade", "living_space"), "LivingSpace {} created successfully.".format(
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
        """ This method tests that a person can be added successfully to the system."""
        self.amity.create_room('Camelot', "office")
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'Staff', 'N'), "{} a {} added successfully.".format(
                            "Catherine Mutava", "Staff"))

    def test_add_person_duplicate(self):
        """ This method tests duplicate additions to the system."""
        self.amity.add_person('Catherine Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'Staff', 'N'), "{} already in the system".format(
            "Catherine Mutava"))

    def test_invalid_employee_type(self):
        """This method tests that only staff and fellow."""
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'surbodinate', 'N'), "Invalid employee type.")

    def test_accomodate_staff(self):
        """This tests ensures that staff cannot be accomodated."""
        self.assertEqual(self.amity.add_person(
            'Catherine Mutava', 'Staff', 'Y'), "Sorry only fellows can be accomodated.")

    def test_reallocation(self):
        """This test an employee reallocation to a new room"""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Angela Mutava', 'Staff', 'N')
        self.amity.create_room("Krypton", "office")
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Krypton"), "{} reallocated  to {}.".format(
                                    "Angela Mutava", "Krypton"))

        self.amity.create_room("Jade", "living_space")
        self.amity.add_person('Angela Mutava', 'fellow', 'Y')
        self.amity.create_room("Hamilton", "living_space")
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Jade"), "{} reallocated  to {}.".format(
                                    "Angela Mutava", "Jade"))


    def test_reallocate_employee_not_registered(self):
        """This tests reallocation of an employee to a new room."""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Angela Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.reallocate_employee(
            "Catherine Mutava", "Hogwarts"), "{} is not in the system.".format(
                "Catherine Mutava"))

    def test_reallocate_employee_to_non_existing_room(self):
        """ This tests reallocation to a room that does not exist."""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Catherine Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.reallocate_employee(
            "Catherine Mutava", "Hogwarts"), "Amity has no room with the name {}".format("Hogwarts"))

    def test_reallocate_to_same_room(self):
        """Tests that an employee cannot be reallocated to the same room."""
        self.amity.create_room("Camelot", "office")
        self.amity.add_person('Catherine Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.reallocate_employee(
            "Catherine Mutava", "Camelot"), "{} cannot be reallocated to the same office.".format(
            "Catherine Mutava"))

        self.amity.create_room("Jade", "living_space")
        self.amity.add_person('Catherine Mutava', 'fellow', 'Y')
        self.assertEqual(self.amity.reallocate_employee(
            "Catherine Mutava", "Jade"), "{} cannot be reallocated to the same living space.".format(
            "Catherine Mutava"))

    def test_load_people(self):
        """This method tests loading people from a textfile """
        self.assertEqual(self.amity.load_people("employee.txt"),
                         "Read content from the file successfully.")

    def test_load_people_from_non_existing_file(self):
        """This method tests loading people form a file that doesn't exist."""
        self.assertEqual(self.amity.load_people("employees.txt"),
                         "Error: can\'t find file or read data.")    

    

if __name__ == '__main__':
    unittest.main()