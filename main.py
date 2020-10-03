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
    [print(dep) for dep in session.query(Department).filter(Department.budget > 500000)]
    separator()

    print("!!!!! Display employees hired in 2017 !!!!!")
    [print(emp) for emp in session.query(Employee).filter(Employee.start_date) if emp.start_date.year == 2017]
    separator()

    print("!!!!! Display employees hired over 2017 !!!!!")
    [print(emp) for emp in session.query(Employee).filter(Employee.start_date) if emp.start_date.year > 2017]
    separator()

    print("!!!!! Display all onsite courses !!!!")

    print("!!!!! Display all schools related to first department !!!!")

    print("!!!!! Add new student !!!!")

    print("!!!!! Add new exams grades for this student !!!!")

    print("!!!!! Delete student and all related grades !!!!")

    print("!!!!! Show all students with failed exams !!!!")

    print("!!!!! Count average grades from students and sort then from best to worst. !!!!")
    print("!!!!! Display also students who not passed all exams !!!!")

    print("!!!!! Display all onsite courses !!!!")







# todo display tables
# todo add data into tables
# todo display merged, sorted ordered tables
# todo check relations between tables
# todo delete records, be aware of deleting also related data in tables
# todo test switching to mysql tables
