import argparse

class Course:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, student, grade):
        self.grades[student] = grade

    def remove_grade(self, student, number):
        if student in self.grades and number in self.grades[student]:
            del self.grades[student][number]

    def __str__(self):
        return self.name

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class GradeBook:
    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course):
        self.courses[course] = Course(course)

    def add_student(self, student):
        self.students[student] = Student(student)

    def add_grade(self, student_name, course_name, grade):
        student = self.students.get(student_name)
        course = self.courses.get(course_name)
        if student and course:
            course.add_grade(student, grade)
        else:
            print("Niepoprawna komenda")

    def remove_grade(self, student_name, course_name, number):
        student = self.students.get(student_name)
        course = self.courses.get(course_name)
        if student and course:
            course.remove_grade(student, number)
        else:
            print("Niepoprawna komenda")

    def show_grades(self):
        print("----------+----------+-------+")
        print("Przedmiot | Studenci | Oceny |")
        print("----------+----------+-------+")
        for course in self.courses.values():
            course_name = course.name
            for student, grades in course.grades.items():
                student_name = student.name
                grade_str = " ".join([str(grade) for grade in grades.values()])
                print(f"{course_name: <12} {student_name: <12} {grade_str}")

    def show_courses(self):
        for course in self.courses.keys():
            print(course)

def main():
    grade_book = GradeBook()
    while True:
        try:
            command = input("> ")
            if command == "Ctrl+D":
                break
            if command == "grades":
                grade_book.show_grades()
            elif command == "pokaż_przedmioty":
                grade_book.show_courses()
            else:
                parts = command.split("+=")
                if len(parts) == 2:
                    student_course = parts[0].strip().split("|")
                    student_name = student_course[0].strip()
                    course_name = student_course[1].strip()
                    grades = parts[1].split("|")
                    for grade in grades:
                        grade_parts = grade.split("(")
                        if len(grade_parts) == 2:
                            grade_name = grade_parts[0].strip()
                            grade_value = grade_parts[1].replace(")", "").split(",")
                            if len(grade_value) == 2:
                                grade_value = (float(grade_value[0]), float(grade_value[1]))
                                grade_book.add_student(student_name)
                                grade_book.add_course(course_name)
                                grade_book.add_grade(student_name, course_name, grade_value)
                            else:
                                print("Niepoprawny format komendy")
                        else:
                            print("Niepoprawny format komendy")
                else:
                    parts = command.split("-=")
                    if len(parts) == 2:
                        student_course = parts[0].strip().split("|")
                        student_name = student_course[0].strip()
                        course_name = student_course[1].strip()
                        grades = parts[1].split("|")
                        for grade in grades:
                            grade_name = grade.strip()
                            grade_book.remove_grade(student_name, course_name, grade_name)
                    else:
                        print("Niepoprawny format komendy")
        except EOFError:
            break

if __name__ == "__main__":
    main()
