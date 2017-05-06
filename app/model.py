from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base




engine = create_engine('sqlite:///amity_db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Employees(Base):
	__tablename__ = 'employees'
	id = Column(Integer, primary_key=True)
	employee_name = Column(String(200), nullable=False)
	employee_type = Column(String(700), nullable=False)
	office_name = Column(String(60), nullable=False)
	living_space = Column(String(60), nullable=False) 

	def __init__(self, employee_name, employee_type):
		self.employee_name = employee_name
		self.employee_type = employee

class Office(Base):
    __tablename__ = 'offices'
    office_id = Column(Integer, primary_key=True)
    name = Column(String(60), ForeignKey('employees.office_name'))
    employee = relationship('Employees', backref=backref('offices'))

    def __repr__(self):
        return 'Office %s' % (self.name)


class LivingSpace(Base):
    __tablename__ = 'livingspaces'
    living_space_id = Column(Integer(), primary_key=True)
    name = Column(String(60), ForeignKey('employees.living_space'))
    person = relationship('Employees', backref=backref('livingspaces'))

    def __repr__(self):
        return 'Livingspace %s' % (self.name)		




Base.metadata.create_all(engine)