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
        self.amity.create_room("Krypton", "office")
        self.amity.add_person('Angela Mutava', 'Staff', 'N')
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Camelot"), "{} reallocated  to {}.".format(
                                    "Angela Mutava", "Camelot"))

        self.amity.create_room("Jade", "living_space")
        self.amity.create_room("Hamilton", "living_space")
        self.amity.add_person('Angela Mutava', 'fellow', 'Y')
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Hamilton"), "{} reallocated  to {}.".format(
                                    "Angela Mutava", "Hamilton"))


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


    # def test_allocate_employee(self):
    #     """ This method allocates employee to the office they request."""
    #     fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
    #     fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))
        
    #     self.assertEqual(self.amity.allocate_employee(
    #         fake_employee, fake_room), "Employee allocated successfully.")

    # def test_allocate_employee_to_the_same_room(self):
    #     """ This method allocates employee to the office they request."""
    #     fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
    #     fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))
    #     self.amity.allocate_employee(fake_employee, fake_room)
    #     self.assertEqual(self.amity.allocate_employee(
    #         fake_employee, fake_room), "You already have a space in the room.")

    # def test_allocate_employee_more_than_6_in_an_office(self):
    #     """ This method allocates employee to the office they request."""
    #     fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
    #     fake_employee1 = mock.Mock(side_effect=("Christina Sass", "Staff", "N"))
    #     fake_employee2 = mock.Mock(side_effect=("Jeremy Johnson", "Staff", "N"))
    #     fake_employee3 = mock.Mock(side_effect=("Shem Ogumbe", "Staff", "N"))
    #     fake_employee4 = mock.Mock(side_effect=("Mirabel Ekwenugo", "Staff", "N"))
    #     fake_employee5 = mock.Mock(side_effect=("Angela Mutava", "Fellow", "N"))
    #     fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))

        

    #     self.assertEqual(self.amity.allocate_employee(fake_employee, fake_room ),
    #                      "Room is full.Office cannot accomodate more than 6 employees.")

    # def test_reallocate_fellow(self):
    #     """ This method reallocates one person from one room to another."""
    #     fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
    #     fake_room = mock.Mock(side_effect=(["Hogwarts","Krypton"], 'Office'))
        
    #     self.assertEqual(self.amity.reallocate_employee(
    #         fake_employee, "krypton"), "Fellow reallocated successfully.")

    # def test_reallocate_fellow_unregistered(self):
    #     """ This method reallocates one person from one room to anot  her."""
    #     fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
    #     fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))
    #     self.assertEqual(self.amity.reallocate_employee(
    #         "Valeria Chemtai", "Krypton"), "Sorry the fellow is not added to the system.")

    # def test_reallocate_staff(self):
    #     """ This method reallocates one person from one room to another."""
    #     self.amity.add_person("Angela Mutava", "Staff", "N")
    #     self.amity.create_room(["Camelot", "Krypton"], "office")
    #     self.amity.allocate_employee("Angela Mutava", "Camelot")
    #     self.assertEqual(self.amity.reallocate_employee(
    #         "Angela Mutava", "Krypton"), "Staff reallocated successfully.")

    # def test_print_rooms(self):
    #     """ This method prints all the rooms."""
    #     self.amity.create_room(["Valhalla", "Camelot", "Cairo"], "Office")
    #     self.assertEqual(self.amity.print_rooms(),
    #                      ("Valhalla", "Camelot", "Cairo"))

    # def test_print_unallocated_rooms(self):
    #     """This method prints the rooms that have not been allocated employees yet."""
    #     self.amity.create_room(["Hogwarts", "Camelot"], "Office")
    #     self.amity.allocate_employee("Angela Mutava", "Camelot")
    #     self.assertEqual(self.amity.print_unallocated_room(), "Hogwarts")

    # def test_print_allocated_rooms(self):
    #     """This method prints the rooms that have  been allocated employees."""
    #     self.amity.create_room(["Hogwarts", "Camelot"], "Office")
    #     self.amity.allocate_employee("Angela Mutava", "Camelot")
    #     self.assertEqual(self.amity.print_unallocated_room(), "Camelot")

    # def test_load_people(self):
    #     """This method loads people from a database """
    #     self.assertEqual(self.amity.load_people("people.db"),
    #                      "Employees loaded from database successfully.")

    # def test_save_people(self):
    #     """This method loads people from a .txt file to the database"""
    #     self.assertEqual(self.amity.save_people("people.db"),
    #                      "Employees loaded to database successfully.")


if __name__ == '__main__':
    unittest.main()