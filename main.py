
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def _lt_(self,lecturer):
        return self.average_grade < lecturer.average_grade


    def __str__(self):
        some_student = f' Имя: {self.name}\n Фамилмя: {self.surname}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n ' \
                       f'завершенные курсы: {" ".join(self.finished_courses)}\n Средняя оценка за ДЗ: {self.grades}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = {}
        self.courses_attached= []

    def __str__(self):
        some_lecturer = f' Имя лектора: {self.name}\n Фамилмя лектора: {self.surname}\n Средняя оценка за лекции: {self.grades}\n'
        return some_lecturer


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self):
        some_reviewer=f' Имя контролера:{self.name}\n Фамилмя контролера:{self.surname}\n'
        return some_reviewer


some_reviewer = Reviewer('Some', 'Buddy')


some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress = ['Python','Git']
some_student.finished_courses = ['Введение в программирование']
some_student = Student('Tom', 'Cruz', 'male')
some_student.courses_in_progress = ['Python','Git']
some_student.finished_courses = ['Введение в программирование']
some_student = Student('Jerry', 'mouse', 'male')
some_student.courses_in_progress = ['Python','Git']
some_student.finished_courses = ['Введение в программирование']


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached = ['Python']
some_lecturer = Lecturer('Any', 'Buddy')
some_lecturer.courses_attached = ['Python']
some_lecturer = Lecturer('How', 'Buddy')
some_lecturer.courses_attached = ['Python']


some_student.rate_lecturer(some_lecturer,'Python', 9.6)
some_student.rate_lecturer(some_lecturer,'Python', 9.3)
some_student.rate_lecturer(some_lecturer,'Python', 9.8)
# Jerry_mouse.rate_lecturer={Some_Buddy:('Python', 9.6), Any_Buddy:('Python', 9.3), How_Buddy:('Python', 9.8) }
some_reviewer.rate_student=[some_student,'Python', 9.3, some_student,'Python', 9.5, some_student,'Python', 9.2]
# some_reviewer.rate_student(Tom_Cruz,'Python', 9.5)
# some_reviewer.rate_student(Jerry_mouse,'Python', 9.2)


def lecturer_average_grade(lecturer, course, grade):
    lecturer.averaage_grade = 0
    for lecturer in some_student.rate_lecturer:
        lecturer.average_grade[course] += [grade]
    return lecturer.averaage_grade / len(some_student.rate_lecturer)


def average_student_grade(student,grade):
    student.average_grades=0
    for student in some_reviewer.rate_student:
        student.average_grades += [grade]
    return student.average_grades / len(some_reviewer.rate_student)




print(some_reviewer)
print(some_lecturer)
print(some_student)
# print(f'ср оц студ {list(average_student_grade)}')
# print(f'ср оц лектора {list(average_student_grade)}')
# print(Student.grade < Lecturer.grade)


