import sqlite3
import random
from faker import Faker
from datetime import datetime

# Tworzenie bazy danych
conn = sqlite3.connect('school_database.db')
cur = conn.cursor()

# Tworzenie tabel
cur.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES Groups(group_id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Groups (
        group_id INTEGER PRIMARY KEY,
        group_name TEXT
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Lecturers (
        lecturer_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT,
        lecturer_id INTEGER,
        FOREIGN KEY (lecturer_id) REFERENCES Lecturers(lecturer_id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade REAL,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
    )
''')

# Tworzenie obiektu Faker
fake = Faker()

# Wypełnianie tabeli Lecturers
for _ in range(3, 6):
    first_name = fake.first_name_male()
    last_name = fake.last_name_male()
    cur.execute("INSERT INTO Lecturers (first_name, last_name) VALUES (?, ?)", (first_name, last_name))

# Lista przedmiotów
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Computer Science']

# Wypełnianie tabeli Subjects i przydzielanie nauczycieli
for subject_id, subject_name in enumerate(subjects, start=1):
    teacher_id = random.randint(1, 3)  # Losowy wybór nauczyciela
    cur.execute("INSERT INTO Subjects (subject_id, subject_name, lecturer_id) VALUES (?, ?, ?)",
                (subject_id, subject_name, teacher_id))

# Wypełnianie tabeli Students
number_of_students = random.randint(30, 50)
for _ in range(1, number_of_students + 1):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = random.randint(1, 3)
    cur.execute("INSERT INTO Students (first_name, last_name, group_id) VALUES (?, ?, ?)", (first_name, last_name, group_id))

# Wypełnianie tabeli Groups
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    cur.execute("INSERT INTO Groups (group_name) VALUES (?)", (group_name,))

# Wypełnianie tabeli Grades
def assign_grade(score):
    if score >= 91:
        return 5.0
    elif score >= 81:
        return 4.5
    elif score >= 71:
        return 4.0
    elif score >= 61:
        return 3.5
    elif score >= 51:
        return 3.0
    else:
        return 2.0

# def assign_modifier(score):
#     if score % 10 >= 7:
#         return '+'
#     elif score % 10 <= 3:
#         return '-'
#     else:
#         return ''

for student_id in range(1, number_of_students + 1):
    for _ in range(20):
        score = random.randint(0, 100)
        grade_letter = assign_grade(score)
        #modifier = assign_modifier(score)
        final_grade = grade_letter # modifier
        subject_id = random.randint(1, 8)  # Wybór z przedmiotów od 1 do 8
        start_date = datetime(2023, 10, 1)
        end_date = datetime(2024, 1, 31)
        date = fake.date_time_between(start_date=start_date, end_date=end_date)
        cur.execute("INSERT INTO Grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                    (student_id, subject_id, final_grade, date))

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()
