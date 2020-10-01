from datetime import datetime, date
from db.database import Course, Department, Employee, Student, Grade, Online, Onsite, Supervisor, Instructor


def bootstrap_courses(session):
    courses = [
        ("Basic mechanics", 10000, 150, date(2020, 1, 1), date(2020, 5, 29), 1),
        ("Safety in aviation", 10000, 50, date(2020, 2, 1), date(2020, 4, 29), 1),
        ("Flight theory", 15000, 200, date(2020, 2, 1), date(2020, 3, 29), 1),
        ("Aerodynamics", 5000, 100, date(2020, 2, 1), date(2020, 3, 29), 1),
        ("Jets basics", 23000, 300, date(2020, 4, 1), date(2020, 7, 29), 2),
        ("Bombers basics", 42000, 200, date(2020, 4, 1), date(2020, 8, 29), 2),
        ("Parachuting", 25000, 150, date(2020, 7, 1), date(2020, 8, 29), 2),
        ("Passenger planes", 40000, 200, date(2019, 4, 1), date(2019, 6, 29), 3),
        ("Cargo planes", 40000, 200, date(2019, 5, 1), date(2019, 7, 29), 3),
        ("Special planes", 20000, 150, date(2019, 6, 1), date(2019, 8, 29), 3),
        ("Helicopters", 38000, 200, date(2018, 5, 1), date(2018, 6, 29), 4),
        ("Drones", 11000, 200, date(2018, 6, 1), date(2018, 8, 29), 4),
        ("Cargo copters", 33000, 350, date(2018, 7, 1), date(2018, 9, 29), 4),
        ("Touristic licence", 22000, 100, date(2020, 2, 1), date(2020, 3, 29), 5),
        ("Seaplanes", 35000, 250, date(2019, 6, 1), date(2019, 8, 29), 5),
    ]
    session.add_all([
        Course(name=name, price=price, ects=ects, start_date=start, end_date=end, id_department=dep)
        for name, price, ects, start, end, dep in courses
    ])
    session.commit()


def bootstrap_departments(session):
    departments = [
        ("Education", 650000, "ul. Sienkiewicza 20a, Wygwizdowo"),
        ("Civil Protection", 100000, "ul. Sienkiewicza 20b, Wygwizdowo"),
        ("Big planes", 750000.50, "ul. Sienkiewicza 20c, Wygwizdowo"),
        ("Helicopter", 450000.50, "ul. Sienkiewicza 20d, Wygwizdowo"),
        ("Small planes", 450000, "ul. Sienkiewicza 20e, Wygwizdowo")
    ]
    session.add_all([
        Department(name=name,
                   budget=budget,
                   address=address)
        for name, budget, address in departments
    ])
    session.commit()


def bootstrap_employees(session):
    employees = [
        ("Marek", "Marecki", datetime(2013, 1, 14, 11, 10, 10), 89010112365, 888555321, "ul. długa 983, Łapiguz"),
        ("Piotr", "Pioterski", datetime(2015, 2, 26, 9, 10, 10), 8812023286, 888555322, "ul. sroga 9, Zło"),
        ("Konrad", "Konradzki", datetime(2017, 3, 8, 10, 22, 10), 85050527793, 888555323, "ul. zimna 3, Mróz"),
        ("Adam", "Adamowicz", datetime(2020, 4, 2, 10, 12, 10), 94070428745, 888555324, "ul. rzecza 8, Łapiguz"),
        ("Stefan", "Stefański", datetime(2015, 5, 23, 11, 10, 10), 93110112365, 834555321, "ul. końska 83, Zwoleń"),
        ("Agata", "Marek", datetime(2017, 6, 3, 13, 11, 10), 99030112575, 883555321, "ul. krowia 93, Muńsk"),
        ("Liliana", "Kwiatowska", datetime(2017, 7, 1, 10, 10, 10), 90022312365, 888574234, "ul. zdrowa 98, Aspirynów"),
        ("Olga", "Torba", datetime(2018, 8, 21, 10, 4, 10), 9110290112345, 888587378, "ul. mrowia 11, Termitów"),
        ("Zdzisław", "Pupa", datetime(2019, 9, 22, 7, 42, 10), 72052112124, 888547024, "ul. paskudna 2a, Smrodów"),
        ("Zbigniew", "Jeżyna", datetime(2012, 10, 9, 12, 10, 10), 79070412347, 888549532, "ul. none 0, Szczecin")
    ]
    session.add_all([
        Employee(first_name=first, last_name=last, start_date=start, pesel=pesel, phone_number=phone, address=address)
        for first, last, start, pesel, phone, address in employees
    ])
    session.commit()


def bootstrap_students(session):
    students = [
        ("John", "Smith", "Long st. 654, Manchester", 89381458745, 112688412),
        ("Brad", "Marble", "Blank st. 4, Berlin", 89381898955, 115821412),
        ("Paul", "Candle", "Dirty st. 64, Kiev", 89381898742, 115238412),
        ("Jessica", "Sweet", "Snowy st. 5, NY", 89381898713, 115832412),
        ("Nick", "Curtain", "Windy st. 2, Orlando", 89381478745, 115888972),
        ("Pamela", "Salt", "Chopin st. 8, Bydgoszcz", 89388498745, 115888842),
        ("Nicolas", "Paper", "Lewinski st. 21, Gotham", 89381893445, 115888454),
        ("Georgia", "Horror", "Obama st. 7, Disneyland", 89381876745, 115888252),
        ("Bill", "Blacksmith", "Kaczyński st. 9, Watershed", 89121898745, 115834412),
        ("Phil", "Toe", "Park st. 1, Blackwater", 89381893445, 245883412),
    ]
    session.add_all([
        Student(first_name=first, last_name=last, address=address, pesel=pesel, phone_number=phone)
        for first, last, address, pesel, phone in students
    ])
    session.commit()


def bootstrap_grades(session):
    values = [
        (1, 1, 5, 5), (2, 1, 5, 5), (3, 1, 5, 5), (4, 1, 5, 5), (5, 1, 5, 5),
        (6, 1, 5, 5), (7, 1, 5, 5), (8, 1, 5, 5), (9, 1, 5, 5), (10, 1, 5, 5),
        (11, 1, 5, 5), (12, 1, 5, 5), (13, 1, 5, 5), (14, 1, 5, 5), (15, 1, 5, 5),

        (1, 2, 4, 5), (2, 2, 4, 5), (3, 2, 4, 5), (4, 2, 4, 5), (5, 2, 4, 5),
        (6, 2, 4, 5), (7, 2, 4, 5), (8, 2, 4, 5), (9, 2, 4, 5), (10, 2, 4, 5),
        (11, 2, 5, 5), (12, 2, 4, 5), (13, 2, 4, 5), (14, 2, 4, 5), (15, 2, 4, 5),

        (1, 3, 4, 5), (2, 3, 4, 4), (3, 3, 4, 4), (4, 3, 4, 4), (5, 3, 4, 4),
        (6, 3, 4, 4), (7, 3, 4, 4), (8, 3, 4, 4), (9, 3, 4, 4), (10, 3, 4, 4),
        (11, 3, 4, 5), (12, 3, 4, 4), (13, 3, 4, 5), (14, 3, 4, 4), (15, 3, 4, 4),

        (1, 4, 4, 3), (2, 4, 4, 3), (3, 4, 4, 3), (4, 4, 4, 3), (5, 4, 4, 3),
        (6, 4, 4, 3), (7, 4, 4, 3), (8, 4, 4, 3), (9, 4, 4, 3), (10, 4, 4, 4),
        (11, 4, 4, 3), (12, 4, 4, 3), (13, 4, 4, 3), (14, 4, 4, 3), (15, 4, 4, 4),

        (1, 5, 3, 3), (2, 5, 3, 3), (3, 5, 3, 3), (4, 5, 4, 3), (5, 5, 3, 3),
        (6, 5, 3, 3), (7, 5, 3, 4), (8, 5, 3, 3), (9, 5, 3, 3), (10, 5, 3, 3),
        (11, 5, 3, 3), (12, 5, 3, 4), (13, 5, 3, 3), (14, 5, 4, 3), (15, 5, 3, 3),

        (1, 6, 4, 5), (2, 6, 4, 5), (3, 6, 4, 5), (4, 6, 4, 3), (5, 6, 4, 3),
        (6, 6, 4, 5), (7, 6, 4, 5), (8, 6, 4, 5), (9, 6, 4, 3), (10, 6, 4, 3),
        (11, 6, 4, 5), (12, 6, 4, 5), (13, 6, 4, 5), (14, 6, 4, 4), (15, 6, 4, 5),

        (1, 7, 4, 5), (2, 7, 4, 5), (3, 7, 4, 5), (4, 7, 4, 2), (5, 7, 4, 5),
        (6, 7, 4, 5), (7, 7, 4, 5), (8, 7, 4, 5), (9, 7, 4, 3), (10, 7, 4, 5),
        (11, 7, 4, 5), (12, 7, 4, 5), (13, 7, 4, 5), (14, 7, 2, 3), (15, 7, 4, 5),

        (1, 8, 4, 3), (2, 8, 4, 3), (3, 8, 4, 5), (4, 8, 4, 3), (5, 8, 4, 5),
        (6, 8, 3, 3), (7, 8, 4, 3), (8, 8, 4, 5), (9, 8, 4, 3), (10, 8, 4, 3),
        (11, 8, 4, 5), (12, 8, 3, 5), (13, 8, 4, 3), (14, 8, 4, 4), (15, 8, 3, 5),

        (1, 9, 3, 5), (2, 9, 4, 5), (3, 9, 4, 5), (4, 9, 4, 5), (5, 9, 4, 5),
        (6, 9, 4, 5), (7, 9, 4, 5), (8, 9, 4, 5), (9, 9, 4, 5), (10, 9, 4, 5),
        (11, 9, 4, 5), (12, 9, 4, 5), (13, 9, 4, 5), (14, 9, 4, 5), (15, 9, 4, 5),

        (1, 10, 4, 5), (2, 10, 4, 5), (3, 10, 4, 5), (4, 10, 4, 5), (5, 10, 4, 5),
        (6, 10, 4, 2), (7, 10, 4, 5), (8, 10, 4, 5), (9, 10, 4, 5), (10, 10, 4, 5),
        (11, 10, 4, 4), (12, 10, 4, 5), (13, 10, 4, 5), (14, 10, 4, 5), (15, 10, 4, 5),

    ]

    session.add_all([
        Grade(id_course=course, id_student=student, exam1=grade1, exam2=grade2)
        for course, student, grade1, grade2 in values
    ])
    session.commit()


def bootstrap_online(session):
    values = [
        (1, "https://www.heavenhell.com/curses/one"),
        (3, "https://www.heavenhell.com/curses/three"),
        (5, "https://www.heavenhell.com/curses/five"),
        (7, "https://www.heavenhell.com/curses/seven"),
        (9, "https://www.heavenhell.com/curses/nine"),
        (11, "https://www.heavenhell.com/curses/eleven"),
        (13, "https://www.heavenhell.com/curses/thirteen"),
        (15, "https://www.heavenhell.com/curses/fifteen"),
    ]

    session.add_all([
        Online(id_course=course, url=url)
        for course, url in values
    ])
    session.commit()


def bootstrap_onsite(session):
    values = [
        (2, "Wygwizdowo 29"),
        (4, "Wygwizdowo 15"),
        (6, "Wygwizdowo 17"),
        (8, "Wygwizdowo 23"),
        (10, "Wygwizdowo 14"),
        (12, "Wygwizdowo 13"),
        (14, "Wygwizdowo 1"),
    ]

    session.add_all([
        Onsite(id_course=course, address=address)
        for course, address in values
    ])
    session.commit()


def bootstrap_supervisors(session):
    values = [
        (10, 1, date(2012, 10, 9)),
        (10, 2, date(2012, 10, 9)),
        (10, 3, date(2012, 10, 9)),
        (10, 4, date(2012, 10, 9)),
        (10, 5, date(2012, 10, 9))
    ]
    session.add_all([
        Supervisor(id_employee=emp, id_department=dep, start_date=start)
        for emp, dep, start in values
    ])
    session.commit()


def bootstrap_instructors(session):
    values = [
        (1, 1, date(2018, 1, 26)),
        (2, 2, date(2018, 12, 19)),
        (3, 1, date(2018, 4, 11)),
        (4, 2, date(2018, 7, 29)),
        (5, 3, date(2018, 8, 19)),
        (6, 6, date(2018, 8, 12)),
        (7, 4, date(2020, 2, 9)),
        (8, 7, date(2018, 12, 3)),
        (9, 5, date(2018, 11, 9)),
        (10, 5, date(2018, 10, 29)),
        (11, 8, date(2018, 6, 3)),
        (12, 9, date(2019, 4, 14)),
        (13, 7, date(2018, 6, 25)),
        (14, 4, date(2020, 5, 26)),
        (15, 8, date(2018, 7, 18)),
    ]
    session.add_all([
        Instructor(id_course=course, id_employee=emp, start_date=start)
        for course, emp, start in values
    ])
    session.commit()


def bootstrap_db(session):
    bootstrap_students(session)
    bootstrap_employees(session)
    bootstrap_departments(session)
    bootstrap_courses(session)
    bootstrap_grades(session)
    bootstrap_online(session)
    bootstrap_onsite(session)
    bootstrap_supervisors(session)
    bootstrap_instructors(session)
