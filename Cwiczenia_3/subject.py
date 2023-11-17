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
        removed = False
        for i, (s, g) in enumerate(self.students):
            if s == student and g == grade:
                self.students.pop(i)
                removed = True
                print(f"Usunięto ocenę {grade} dla studenta {student}.")
                break
        if not removed:
            print(f"Brak oceny o numerze {grade} dla studenta {student}.")

    def __str__(self):
        student_info = "\n".join([f"    {s} {g}" for s, g in self.students])
        return f"{self.name}\n    Maksymalna liczba studentów: {self.max_students}\n    Aktualna liczba studentów: {len(self.students)}\n    Zapisani studenci:\n{student_info}"


list_of_subjects = [Subject("Matematyka", 2), Subject("Fizyka", 3)]
