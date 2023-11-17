class Subject:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add(self, student, grade):
        if len(self.students) < self.max_students:
            self.students.append((student, grade))
        else:
            print(f"Brak miejsc na przedmiocie {self.name}.")

    def remove(self, student, grade):
        found = False
        for i, (s, g) in enumerate(self.students):
            if s == student and g == grade:
                self.students.pop(i)
                found = True
                print(f"Usunięto ocenę {grade} dla studenta {student}.")
                break
        if not found:
            print(f"Brak oceny o numerze {grade} dla studenta {student}.")

    def __str__(self):
        student_info = "\n".join([f"    {s} {g}" for s, g in self.students])
        return f"{self.name}\n    Maksymalna liczba studentów: {self.max_students}\n    Aktualna liczba studentów: {len(self.students)}\n    Zapisani studenci:\n{student_info}"


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject.name] = grade

    def __str__(self):
        grade_info = "\n".join([f"    {subject} {self.grades[subject]}" for subject in self.grades])
        return f"{self.name}\n{grade_info}"


list_of_subjects = [Subject("Matematyka", 2), Subject("Fizyka", 3)]
list_of_students = [Student("Jan Kowalski"), Student("Anna Kowalska"), Student("Joanna Bielecka")]
while True:
    user_input = input("> ")
    if user_input == "grades":
        for subject in list_of_subjects:
            print(subject)
    elif user_input == "print(list_of_subjects)":
        subject_names = [subject.name for subject in list_of_subjects]
        print(subject_names)
    elif user_input == "print(list_of_students)":
        student_names = [student.name for student in list_of_students]
        print(student_names)
    elif "print(list_of_subjects[" in user_input and user_input.endswith("])"):
        try:
            index = int(user_input.split("[")[1].split("]")[0])
            if index >= 0 and index < len(list_of_subjects):
                print(list_of_subjects[index])
            else:
                print(" " * 11 + "Niepoprawny indeks przedmiotu")
        except ValueError:
            print(" " * 11 + "Niepoprawny indeks przedmiotu")
    elif "student = list_of_students" in user_input and "subject = list_of_subjects" in user_input:
        try:
            exec(user_input)
        except Exception as e:
            print(f"Nieznane polecenie: {str(e)}")
    elif "print(list_of_students[" in user_input and user_input.endswith("])"):
        try:
            index = int(user_input.split("[")[1].split("]")[0])
            if index >= 0 and index < len(list_of_students):
                print(list_of_students[index])
            else:
                print(" " * 11 + "Niepoprawny indeks studenta")
        except ValueError:
            print(" " * 11 + "Niepoprawny indeks studenta")
    elif "+=" in user_input:
        parts = user_input.split("+=")
        student_name = parts[0].strip()
        subject_name = parts[1].strip()
        grade = float(parts[2].strip())
        student = next((s for s in list_of_students if s.name == student_name), None)
        subject = next((s for s in list_of_subjects if s.name == subject_name), None)
        if student is not None and subject is not None:
            subject.add(student, grade)
        else:
            print(" " * 11 + "Niepoprawna komenda")
    elif "+=" in user_input:
        # Implementacja dodawania oceny
        parts = user_input.split("+=")
        student_name = parts[0].strip()
        subject_name = parts[1].strip()
        grade = float(parts[2].strip())
        for student in list_of_students:
            if student.name == student_name:
                for subject in list_of_subjects:
                    if subject.name == subject_name:
                        subject.add(student, grade)
    elif "-=" in user_input:
        # Implementacja usuwania oceny
        parts = user_input.split("-=")
        student_name = parts[0].strip()
        subject_name = parts[1].strip()
        grade = float(parts[2].strip())
        for student in list_of_students:
            if student.name == student_name:
                for subject in list_of_subjects:
                    if subject.name == subject_name:
                        subject.remove(student, grade)
    elif "+" in user_input:
        print(" " * 11 + "Niepoprawny format komendy")
    else:
        print(" " * 11 + "Nieznana komenda")
