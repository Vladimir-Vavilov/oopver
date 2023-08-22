class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        self.stu_grade = {}
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lec_grades = {}

    def __lt__(self, other):
        self.lec_grades = {}

    def rate_grade(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grades]
            else:
                lecturer.lec_grades[course] = [grades]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python', 'Git']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Git']
best_lecturer.lec_grades['Git'] = [10, 10, 10, 10, 10]


cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']

sr_grade_lec = len(best_lecturer.lec_grades)/len(best_lecturer.lec_grades)
sr_grade_stu = len(best_student.grades)/len(best_student.grades)
cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 10)
print(f'Имя:{cool_Reviewer.name} \nФамилия:{cool_Reviewer.surname}')
print(f'Имя:{best_lecturer.name} \nФамилия:{best_lecturer.surname}')
print(f'Средняя оценка за лекции:{sr_grade_lec}')
print(f'Имя: {best_student.name} \nФамилия:{best_student.surname}')
print(f'Средняя оценка за домашние задания: {sr_grade_stu}')
print(f'Курсы в процессе изучения: {best_student.courses_in_progress}')
print(f'Завершенные курсы: {best_student.finished_courses}')

# print(cool_Reviewer.courses_attached)
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
