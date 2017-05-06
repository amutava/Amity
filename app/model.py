from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Employees(Base):
	__tablename__ = 'employees'
	# Here we define columns for the table lyrics
    # Each column is also a normal Python instance attribute.
	id = Column(Integer, primary_key=True)
	employee_name = Column(String(200), nullable=False)
	employee type = Column(String(700), nullable=False)

	def __init__(self, employee_name, employee_type):
		self.employee_name = employee_name
		self.employee_type = employee

# Create an engine that stores data in the local directory's
# songs.db file.
engine = create_engine('sqlite:///songs.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)