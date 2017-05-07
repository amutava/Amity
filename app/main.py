
"""
Usage:
    amity create_room (living|office) <room_name>...
    amity add_person <name> (fellow|staff) [<wants_accomodation>]
    amity reallocate_person <name> <new_room_name>
    amity load_people <filename>
    amity save_people
    amity print_allocated_rooms
    amity print_unallocated_rooms
    amity print_allocations [-o <filename>]
    amity print_unallocated [-o <filename>]
    amity print_room_occupants <room_name>
    amity (-i | --interactive)
    amity (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import cmd
from docopt import docopt, DocoptExit
from amity import *
from pyfiglet import figlet_format
from termcolor import cprint
from clint.textui import colored
import os


def docopt_cmd(func):
    """
    Decorator definition for the app.
    """

    def fn(self, arg):

        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            msg = "Invalid Command."

            print(msg)
            print(e)
            return

        except SystemExit:
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

amity = Amity()


class Amity(cmd.Cmd):
    # intro = cprint(figlet_format("Amity", font="big"), "cyan", attrs=['bold'])
    print (colored.cyan('                   O8', bold=12))
    print (colored.cyan('                  @@@@C', bold=12))
    print (colored.cyan('                @@@@@@@@c', bold=12))
    print (colored.cyan('      @@@@@@@@O8@@8  8@@8o@@@@@@@@c', bold=12))
    print (colored.cyan('      @@@@@@@@            C@@@@@@@c', bold=12))
    print (colored.cyan('      8@@8                    8@@@                     O@@                                                     ', bold=12))
    print (colored.cyan('      O@@@                    @@@8                     @@@O                                                    ', bold=12))
    print (colored.cyan('      C                          C                    @@@@@8                                                   ', bold=12))
    print (colored.cyan('   o@@@@                        o@@@o                @@@ o@@8      C@@C@@@       @@@@8   @@@   @@@@                     ', bold=12))
    print (colored.cyan(' c@@@@@C                         @@@@@O             8@@c  @@@      C@@@ @@     @@ @@@C   @@@   @@@@                       ', bold=12))
    print (colored.cyan('c@@@@@c                           8@@@@o           o@@O    @@@     C@@8  @@  @@   O@@C   @@@   @@@@                      ', bold=12))
    print (colored.cyan('   @@@@@o                       8@@@@c            o@@8oooooo@@@    C@@C    @@@    o@@O   @@@   @@@@@@@@@   @@@    @@@    ', bold=12))
    print (colored.cyan('     O@o                         @@o             c@@@@@@@@@@@@@8   C@@C           o@@O   @@@   @@@@@@@@@   @@@    @@@    ', bold=12))
    print (colored.cyan('      O@@O                    O8@O               @@@         8@@o  C@@C           o@@O   @@@   @@@@        @@@    @@@    ', bold=12))
    print (colored.cyan('      8@@@                    8@@@              8@@o          O@@o C@@C           o@@O   @@@   @@@@@@@@@   @@@@@@@@@@     ', bold=12))
    print (colored.cyan('      @@@@O88O            c@8O8@@@             oOOo            OOO cOOo           cOOo   @@@   @@@@@@@@@   @@@@@@@@@@     ', bold=12))
    print (colored.cyan('      @@@@@@@@CcO@o  c@@c 8@@@@@@@c                                                                               @@@       ', bold=12))
    print (colored.cyan('      cocc     @@@@8o@@@@c    ccoc                                                                                @@@      ', bold=12))
    print (colored.cyan('                 8@@@@@C                                                                                   @@@@@@@@@@      ', bold=12))
    print (colored.cyan('                  o@@o                                                                                     @@@@@@@@@@       ' , bold=12))
    


    print ("                                                        **********User Guide************    ")
    print ("                                                        Command    Description     Parameter")
    
    print ("type --help-- to view commands")
    prompt = "<--Amity-->"

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_names> <room_type>"""
        room_names = arg["<room_names>"]
        room_type = arg["<room_type>"]
        for rooms in room_names:
            amity.create_room(rooms, room_type)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <name> <employee_type> <need_accomodation>"""  
        
        

    @docopt_cmd
    def do_reallocate_employee(self, arg):
        """Usage: reallocate_employee <>"""
        

    @docopt_cmd
    def do_print_room_occupants(self):
        """Usage: print_room_occupants"""
        
        

    @docopt_cmd
    def do_print_allocated_rooms(self):
        """Usage: print_allocated_rooms"""
        

    @docopt_cmd
    def do_print_unallocated_rooms(self):
        """Usage: print_unallocated_rooms"""
        

    @docopt_cmd
    def do_load_people(self):
        """Usage: load_people"""
        

    @docopt_cmd
    def do_save_people(self, arg):
        """Usage: save_people"""            
        

    
    def do_quit(self, arg):
        """Exits the application
        """
        print ("Welcome again!")
        exit()
if __name__ == '__main__':
    Amity().cmdloop()
