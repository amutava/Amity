from sqlachemy import create_engine
from sqlalchemy import Column, Integer, String
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
    need_accomodation = Column(String(40), nullable=True)

    def __init__(self, employee_name, employee_type, need_accomodation):
        self.employee_name = employee_name
        self.employee_type = employee_type
        self.need_accomodation = need_accomodation


class Offices(Base):
    __tablename__ = 'offices'
    office_id = Column(Integer, primary_key=True)
    room_name = Column(String(60))
    room_capacity = Column(String(20))
    room_occupants = Column(String(600))  


    def __repr__(self):
        return 'Office %s' % (self.name)


class LivingSpaces(Base):
    __tablename__ = 'livingspaces'
    living_space_id = Column(Integer(), primary_key=True)
    room_name = Column(String(60))
    room_capacity = Column(String(20))
    room_occupants = Column(String(600))

    def __repr__(self):
        return 'Livingspace %s' % (self.name)


Base.metadata.create_all(engine)
