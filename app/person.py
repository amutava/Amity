class Person(object):

	def __init__(self, name=None, employee_type= None, need_accomodation=None):
		self.name = name
		self.employee_type = employee_type
		self.need_accomodation = need_accomodation
		self.all_employees = []

class Fellow(Person):
   pass

class Staff(Person):
	pass