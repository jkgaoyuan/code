from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import sessionmaker
engine = create_engine(
    'mysql+pymysql://gaoyuan:gaoyuan@192.168.1.58/tedu1903?charset=utf8',
    encoding='utf8',
    echo=True
)


Session = sessionmaker(bind=engine)

base = declarative_base()

class Departments(base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)
class Employees(base):

    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))
class salay(base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)
if __name__ == '__main__':
    base.metadata.create_all(engine)
