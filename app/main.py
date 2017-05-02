"""
A brief description of what the application does.
"""
import cmd
from docopt import docopt, DocoptExit
from app.amity import *
from pyfiglet import figlet_format
from termcolor import cprint

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

class Amity(cmd.Cmd):
	intro = cprint(figlet_format("Amity", font="big"), "yellow", attrs=['bold'])
	print "**********User Guide************"
	print "    Command    Description     Parameter"
	
	print "type --help-- to view commands"
	prompt = "<--Amity-->"

	@docopt_cmd
	def do_x(self, arg):
		"""Usage: find <query> """
		query = arg["<query>"]
		#song_find(query)
		

	@docopt_cmd
	def do_y(self, arg):
		"""Usage: view <track_id>"""	
		track_id = arg["<track_id>"]
		

	@docopt_cmd
	def do_z(self, arg):
		"""Usage: clear
		"""
		

	@docopt_cmd
	def	do_A(self, arg):
		"""Usage: save <track_id>"""
		track_id = arg["<track_id>"]
		

	@docopt_cmd
	def do_B(self, arg):
		"""Usage: clear_song <track_id>"""
		track_id = arg["<track_id>"]
		

	
	def do_quit(self, arg):
		"""Exits the application
	    """
		print "Welcome again!"
		exit()
if __name__ == '__main__':
	LyricsFinder().cmdloop()