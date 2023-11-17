import sys

def read_grades(filename):
    grades = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                student_name = parts[0]
                student_grades = {}
                for item in parts[1:]:
                    subject, scores = item.split('(')
                    scores = scores.rstrip(')').split(',')
                    student_grades[subject] = [float(score) for score in scores]
                grades[student_name] = student_grades
    except FileNotFoundError:
        grades = {}
    return grades

def save_grades(filename, grades):
    with open(filename, 'w') as file:
        for student_name, student_grades in grades.items():
            grades_str = '|'.join([f"{subject}({','.join(map(str, scores))})" for subject, scores in student_grades.items()])
            file.write(f"{student_name}|{grades_str}\n")

def display_grades(grades):
    if not grades:
        print("Brak ocen w bazie danych.")
    else:
        max_subject_len = max(len(subject) for student_grades in grades.values() for subject in student_grades.keys())
        max_student_len = max(len(student) for student in grades.keys())
        
        print(f"{'Przedmiot':<{max_subject_len}} | {'Studenci':<{max_student_len}} | Oceny")
        print('-' * (max_subject_len + max_student_len + 20))
        
        for subject, student_grades in sorted(grades.items()):
            for student, scores in student_grades.items():
                print(f"{subject:<{max_subject_len}} | {student:<{max_student_len}} | {', '.join(map(str, scores))}")
                
def add_grades(grades, command):
    parts = command.split('+=')
    student_name = parts[0]
    grade_info = parts[1].split('|')
    
    if student_name not in grades:
        grades[student_name] = {}
    
    for item in grade_info:
        subject, scores = item.split('(')
        scores = scores.rstrip(')').split(',')
        
        if subject not in grades[student_name]:
            grades[student_name][subject] = []
        
        grades[student_name][subject].extend([float(score) for score in scores])

def remove_grades(grades, command):
    parts = command.split('-=')
    student_name = parts[0]
    grade_info = parts[1].split('|')
    
    if student_name in grades:
        for item in grade_info:
            subject, num = item.split('(')
            num = int(num.rstrip(')'))
            
            if subject in grades[student_name] and 1 <= num <= len(grades[student_name][subject]):
                del grades[student_name][subject][num - 1]
                if not grades[student_name][subject]:
                    del grades[student_name][subject]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: usos.py [file]")
        sys.exit(1)
    
    filename = sys.argv[1]
    grades = read_grades(filename)
    
    while True:
        try:
            command = input("> ")
            if command == "grades":
                display_grades(grades)
            elif '+=' in command:
                add_grades(grades, command)
                save_grades(filename, grades)
            elif '-=' in command:
                remove_grades(grades, command)
                save_grades(filename, grades)
            else:
                print("Nieznane polecenie")
        except (EOFError, KeyboardInterrupt):
            break

