from db.database import (Course, Department, Employee, Student, Grade,
                         Online, Onsite, Instructor)
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
    [print(val) for val in session.query(Course).join(Onsite)]
    separator()

    print("!!!!! Display all schools related to first department !!!!")
    [print(val) for val in session.query(Course).join(Department).filter(Department.id == 1)]
    separator()

    print("!!!!! Display employee with id 10 !!!!!")
    print(session.query(Employee).get(10))
    separator()

    print("!!!!! Display all courses led by employee with id 1 !!!!")
    instructor = session.query(Employee).get(1)
    [print(val) for val in instructor.courses]
    separator()

    print("!!!!! Display all courses form department with id 2 !!!!")
    dep = session.query(Department).get(2)
    [print(val) for val in dep.courses]
    separator()

    print("!!!!! Display grades of student with id 1")
    grade = session.query(Course, Grade.exam1, Grade.exam2).filter(Grade.id_student == 1)
    [print(val) for val in grade]
    separator()

    print("!!!!!  Display grades of student with id 2 from course with id 3 !!!!!")
    grade = session.query(Grade).filter_by(id_student=2).filter_by(id_course=3)
    [print(val) for val in grade]
    separator()

    print("!!!!! Change name of employee with id 3 to Siabadaba  !!!!!")
    employee = session.query(Employee).get(3)
    employee.first_name = "Siabadaba"
    print(">>>> Check undeployed but modified records with \"session.dirty\"")
    print(session.dirty)
    print(">>>> Use session.rollback() to undo not commited changes and check it")
    session.rollback()
    print(session.dirty)
    separator()

    # print("!!!!! Add new student to database !!!!")
    # new_student = Student(first_name="John", last_name="Travolta", address="Oklahoma", pesel=123123)
    # session.add(new_student)
    # print(">>>> Check undeployed but newly added record with \"session.new\"")
    # print(session.new)
    # print(">>>> Commit data and check new table")
    # session.commit()
    # print(session.new)
    # separator()
    #
    # print("!!!!! Add new exams grades for course with id 1 for new students !!!!")
    # course = session.query(Course).get(1)
    # student = session.query(Student).filter_by(last_name="Travolta").first()
    # print({course.id}, {student.id})
    # grade_1 = Grade(id_course=course.id, id_student=student.id, exam1=1, exam2=1)
    # session.add(grade_1)
    # print(session.new)
    # session.commit()
    # print(">>>> Check Travolta grade table")
    # grade = session.query(Grade).filter_by(id_student=student.id).filter_by(id_course=course.id)
    # [print(val) for val in grade]
    # separator()

    # print("!!!!! Delete new student and all related grades, with cascade delete !!!!")
    # course = session.query(Course).get(1)
    # student = session.query(Student).filter_by(last_name="Travolta").first()
    # session.delete(student)
    # session.commit()
    # separator()
    #
    # print("!!!!! Delete course number 15, and check if all related grades")
    # print("and one to one onsite or online relations and instructors are deleted(not students !!!!!)")
    # course_15 = session.query(Course).get(15)
    # session.delete(course_15)
    # session.commit()
    # print("OK")
    # separator()

    # print("!!!!! Delete department with id 5, and check if id_department column are deleted !!!!!")
    # print("!!!!! but not courses and employees related with this departments !!!!!")
    # department_5 = session.query(Department).get(5)
    # session.delete(department_5)
    # session.commit()
    # print("OK")
    # separator()

    print("!!!!! Delete employee with id 10, and check if id_supervisor column are deleted !!!!!")
    print("!!!!! and instructor relation table but not courses related with this departments !!!!!")
    employee_10 = session.query(Employee).get(10)
    session.delete(employee_10)
    session.commit()
    print("OK")
    separator()

# todo add lazy=True, lazy load
# todo delete records, be aware of deleting also related data in tables
# todo remove error wth Decimals
# todo operator exists, has, like
# todo test switching to mysql tables
# todo check what will happen with id_supervisor id deleted employee
