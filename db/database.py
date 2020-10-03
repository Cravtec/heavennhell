from sqlalchemy import (Column, Integer, Sequence,
                        String, ForeignKey, Table,
                        Numeric, SmallInteger, Date,
                        DateTime)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Grade(Base):
    __tablename__ = "grades"

    id_course = Column(Integer, ForeignKey("courses.id"), primary_key=True)
    id_student = Column(Integer, ForeignKey("students.id"), primary_key=True)
    exam1 = Column(Integer)
    exam2 = Column(Integer)

    # many to many relationship
    course = relationship("Course", back_populates="students")
    student = relationship("Student", back_populates="courses")


class Instructor(Base):
    __tablename__ = "instructors"
    id_course = Column(Integer, ForeignKey("courses.id"), primary_key=True)
    id_employee = Column(Integer, ForeignKey("employees.id"), primary_key=True)
    start_date = Column(Date)

    # many to many relationship
    course = relationship("Course", back_populates="employees")
    employee = relationship("Employee", back_populates="courses")


# old supervisor association table. I do not know how to put data in
# supervisor = Table("supervisors", Base.metadata,
#                    Column("id_employee", ForeignKey("employees.id")),
#                    Column("id_department", ForeignKey("departments.id")),
#                    Column("start_date", DateTime))


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, Sequence('courses_id_seq'), primary_key=True)
    name = Column(String(30))
    price = Column(Numeric(7, 2))
    ects = Column(SmallInteger)
    start_date = Column(Date)
    end_date = Column(Date)

    # one department to many courses relationship
    id_department = Column(Integer, ForeignKey("departments.id"))
    departments = relationship("Department", back_populates="courses")

    # one to one relationships
    online = relationship("Online", uselist=False, back_populates="course")
    onsite = relationship("Onsite", uselist=False, back_populates="course")

    # many to many relationship with [students] table and [grades] association table
    students = relationship("Grade", back_populates="course")

    # many to many relationship with [employees] table and [instructor] association table
    employees = relationship("Instructor", back_populates="course")

    def __repr__(self):
        return f"Course id: {self.id} name: {self.name} ects: {self.ects}"


class Online(Base):
    __tablename__ = "online"

    id_course = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    url = Column(String)

    # one to one relationship, back_populates attribute must be the same name as parent
    course = relationship("Course", back_populates="online")


class Onsite(Base):
    __tablename__ = "onsite"

    id_course = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    address = Column(String(50))

    # one to one relationship, back_populates attribute must be the same name as parent
    course = relationship("Course", back_populates="onsite")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, Sequence('students_id_seq'), primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    address = Column(String)
    pesel = Column(Integer)
    phone_number = Column(Integer)

    # many to many relationship with [courses] table and [grades] association table
    courses = relationship("Grade", back_populates="student")

    def __repr__(self):
        return f"Student id: {self.id}, name: {self.first_name} {self.last_name}"


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, Sequence('employees_id_seq'), primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    start_date = Column(DateTime)
    pesel = Column(Integer)
    phone_number = Column(Integer)
    address = Column(String)

    # many to many relationship with [courses] table and [instructor] association table
    courses = relationship("Instructor", back_populates="employee")

    # one to one relationship with [departments] table
    departments = relationship("Department", back_populates="employee")

    def __repr__(self):
        return f"Employee id:{self.id}, name: {self.first_name} {self.last_name}"


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    budget = Column(Numeric(7, 2))
    address = Column(String)

    # one to one relationship with employees
    id_supervisor = Column(Integer, ForeignKey('employees.id'))
    employee = relationship("Employee", uselist=False, back_populates="departments")

    # one department to many courses relationship
    courses = relationship("Course", back_populates="departments")

    def __repr__(self):
        return f"Department id: {self.id}, name: {self.name}"
