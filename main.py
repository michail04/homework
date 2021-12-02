

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'нет такого курса'

    def lecturer_average_grades(self, lecturer):
        sum_grades = sum(map(sum, some_lecturer.grades.values()))
        for key, values in sorted(some_lecturer.grades.items()):
            lecturer.average_grades.append(sum_grades / len(values))
        return lecturer.average_grades

    def _lt_(self, lecturer):
        return self.average_grades < lecturer.average_grades

    def __str__(self):
        some_student = f' Имя: {self.name}\n Фамилмя: {self.surname}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n завершенные курсы: {" ".join(self.finished_courses)}\n ' \
                       f'Средняя оценка за ДЗ: {some_student_1.grades}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = {}

    def __str__(self):
        some_lecturer_list = f' Имя лектора: {self.name}\n Фамилмя лектора: {self.surname}\n Средняя оценка за лекции: {self.grades}\n'
        return some_lecturer_list


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

    def student_average_grades(self, student):
        sum_grades = sum(map(sum, some_student.grades.values()))
        for key, values in sorted(some_student.grades.items()):
            student.average_grades.append(sum_grades / len(values))
        return student.aveage_grades

    def __str__(self):
        some_reviewer = f' Имя контролера: {self.name}\n Фамилмя контролера: {self.surname}\n'
        return some_reviewer


some_reviewer = Reviewer('Some', 'Buddy')

some_student_1 = Student('Jerry', 'mouse', 'male')
some_student_1.courses_in_progress = ['Python', 'Git']
some_student_1.finished_courses = ['Введение в программирование']
some_student_2 = Student('Tom', 'Cruz', 'male')
some_student_2.courses_in_progress = ['Python', 'Git']
some_student_2.finished_courses = ['Введение в программирование']
some_student_3 = Student('Ruoy', 'Eman', 'male')
some_student_3.courses_in_progress = ['Python', 'Git']
some_student_3.finished_courses = ['Введение в программирование']

some_lecturer_1 = Lecturer('How', 'Buddy')
some_lecturer_1.courses_attached = ['Python']
some_lecturer_2 = Lecturer('Any', 'Buddy')
some_lecturer_2.courses_attached = ['Python']
some_lecturer_3 = Lecturer('Some', 'Buddy')
some_lecturer_3.courses_attached = ['Python']

# student_average_grades = {some_student_1: ['Python', 9.3], some_student_2: ['Python', 9.5], some_student_3: ['Python', 9.2]}
# lecturer_average_grades = {some_lecturer_1: ['Python', 9.6], some_lecturer_2: ['Python', 9.3], some_lecturer_3: ['Python', 9.8]}

some_student_3.rate_lecturer(some_lecturer_1, 'Python', 9.0)
some_student_3.rate_lecturer(some_lecturer_2, 'Python', 9.3)
some_student_3.rate_lecturer(some_lecturer_3, 'Python', 9.6)
some_lecturer_list = [[some_lecturer_1, 'Python', 9.0], [some_lecturer_2, 'Python', 9.3], [some_lecturer_3, 'Python', 9.6]]

some_reviewer.rate_student(some_student_1, 'Python', 9.8)
some_reviewer.rate_student(some_student_2, 'Python', 6.3)
some_reviewer.rate_student(some_student_3, 'Python', 7.6)
some_student_list = [some_student_1, some_student_2, some_student_3]



print(f'{some_reviewer} \n{some_lecturer_3} \n{some_student_3}')
