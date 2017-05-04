from unittest import TestCase, mock
from unittest.mock import patch, Mock

from app.amity import Amity



class TestAmity(TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_add_person(self):
        """ This method tests that a person can be added successfully to the system."""
        self.assertEqual(self.amity.add_person('Catherine Mutava', 'Staff', 'N'), "Staff added successfully.")

    def test_add_person_duplicate(self):
        """ This method tests that a person can be added successfully to the system."""
        fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
        with mock.patch('builtins.input', fake_employee):
            add_employee = self.amity.add_person("Catherine Mutava", "Staff", "N")
        self.assertIs(fake_employee, add_employee, "Employee already in the system") 

    def test_create_room_duplicates(self):
        """ This method creates rooms of the given type."""
        fake_rooms = mock.Mock(side_effect=['Camelot', 'Valhalla', 'Krypton'])
        with mock.patch('builtins.input', fake_rooms):
            add_rooms = self.amity.create_room(['Camelot', 'Valhalla', 'Krypton'], "office")
        self.assertEqual(add_rooms, ['Camelot', 'Valhalla', 'Krypton'])

    def test_create_room(self):
        """ This method creates rooms of the given type"""
        fake_room = mock.Mock(side_effect=("Valhalla", "Office"))
        with mock.patch('builtins.input', fake_room):
            self.assertEqual(self.amity.create_room("Valhala", "Office"),
                         "Sorry system does not allow duplicate rooms.")

    def test_allocate_employee(self):
        """ This method allocates employee to the office they request."""
        fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
        fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))
        
        self.assertEqual(self.amity.allocate_employee(
            fake_employee, fake_room), "Employee allocated successfully.")

    def test_allocate_employee_to_the_same_room(self):
        """ This method allocates employee to the office they request."""
        fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
        fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))
        self.amity.allocate_employee(fake_employee, fake_room)
        self.assertEqual(self.amity.allocate_employee(
            fake_employee, fake_room), "You already have a space in the room.")

    def test_allocate_employee_more_than_6_in_an_office(self):
        """ This method allocates employee to the office they request."""
        fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
        fake_employee1 = mock.Mock(side_effect=("Christina Sass", "Staff", "N"))
        fake_employee2 = mock.Mock(side_effect=("Jeremy Johnson", "Staff", "N"))
        fake_employee3 = mock.Mock(side_effect=("Shem Ogumbe", "Staff", "N"))
        fake_employee4 = mock.Mock(side_effect=("Mirabel Ekwenugo", "Staff", "N"))
        fake_employee5 = mock.Mock(side_effect=("Angela Mutava", "Fellow", "N"))
        fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))

        

        self.assertEqual(self.amity.allocate_employee(fake_employee, fake_room ),
                         "Room is full.Office cannot accomodate more than 6 employees.")

    def test_reallocate_fellow(self):
        """ This method reallocates one person from one room to another."""
        fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
        fake_room = mock.Mock(side_effect=(["Hogwarts","Krypton"], 'Office'))
        
        self.assertEqual(self.amity.reallocate_employee(
            fake_employee, "krypton"), "Fellow reallocated successfully.")

    def test_reallocate_fellow_unregistered(self):
        """ This method reallocates one person from one room to anot  her."""
        fake_employee = mock.Mock(side_effect=('Catherine Mutava', 'Staff', 'N'))
        fake_room = mock.Mock(side_effect=(["Hogwarts"], 'Office'))
        self.assertEqual(self.amity.reallocate_employee(
            "Valeria Chemtai", "Krypton"), "Sorry the fellow is not added to the system.")

    def test_reallocate_staff(self):
        """ This method reallocates one person from one room to another."""
        self.amity.add_person("Angela Mutava", "Staff", "N")
        self.amity.create_room(["Camelot", "Krypton"], "office")
        self.amity.allocate_employee("Angela Mutava", "Camelot")
        self.assertEqual(self.amity.reallocate_employee(
            "Angela Mutava", "Krypton"), "Staff reallocated successfully.")

    def test_print_rooms(self):
        """ This method prints all the rooms."""
        self.amity.create_room(["Valhalla", "Camelot", "Cairo"], "Office")
        self.assertEqual(self.amity.print_rooms(),
                         ("Valhalla", "Camelot", "Cairo"))

    def test_print_unallocated_rooms(self):
        """This method prints the rooms that have not been allocated employees yet."""
        self.amity.create_room(["Hogwarts", "Camelot"], "Office")
        self.amity.allocate_employee("Angela Mutava", "Camelot")
        self.assertEqual(self.amity.print_unallocated_room(), "Hogwarts")

    def test_print_allocated_rooms(self):
        """This method prints the rooms that have  been allocated employees."""
        self.amity.create_room(["Hogwarts", "Camelot"], "Office")
        self.amity.allocate_employee("Angela Mutava", "Camelot")
        self.assertEqual(self.amity.print_unallocated_room(), "Camelot")

    def test_load_people(self):
        """This method loads people from a database """
        self.assertEqual(self.amity.load_people("people.db"),
                         "Employees loaded from database successfully.")

    def test_save_people(self):
        """This method loads people from a .txt file to the database"""
        self.assertEqual(self.amity.save_people("people.db"),
                         "Employees loaded to database successfully.")


if __name__ == '__main__':
    unittest.main()