from db.database import (Course, Department, Employee, Student, Grade,
                         Online, Onsite, Supervisor, Instructor)
from db.session import session
from datetime import datetime, date


def separator():
    print('-' * 30)
    print()


if __name__ == '__main__':

    print('!!!!! Display all students data (repr) !!!!!!')
    for student in session.query(Student):
        print(student)
    separator()

    print('!!!!! Display courses data: id, name and sort by price from he most expensive !!!!!')
    for curse in session.query(Course.id, Course.name, Course.price).order_by(Course.price.desc()):
        print(curse)
    separator()

    print('!!!!! Display departments with budget higher than 500 000 !!!!!')
    for dep in session.query(Department).filter(Department.budget > 500000):
        print(dep)
    separator()

    print("!!!!! Display employees hired in 2018 !!!!!")
    for emp in session.query(Employee.start_date).filter(Employee.start_date > date(2018, 1, 1)):
        print(emp)

# todo display tables
# todo add data into tables
# todo display merged, sorted ordered tables
# todo check relations between tables
# todo delete records, be aware of deleting also related data in tables
