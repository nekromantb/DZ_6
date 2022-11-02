def average_rating(dictionary) -> float:
    sum_marks = 0
    marks_quantity = 0
    for course in dictionary:
        for mark in dictionary[course]:
            sum_marks += mark
            marks_quantity += 1
    return sum_marks / marks_quantity


def compare_grades(dictionary_self, dictionary_other) -> int:
    self_ave_grade = average_rating(dictionary_self)
    other_ave_grade = average_rating(dictionary_other)
    if self_ave_grade > other_ave_grade:
        return 1
    elif self_ave_grade == other_ave_grade:
        return 0
    else:
        return -1


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) \
                and course in lecturer.courses_attached:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за домашние задания: {round(average_rating(self.grades), 1)}")
        if self.courses_in_progress is None:
            print(f"Курсы в процессе изучения: ", *self.courses_in_progress)
        if self.finished_courses is None:
            print(f"Завершенные курсы: ", *self.finished_courses)
        return ""

    def __cmp__(self, other):
        if isinstance(other, Student):
            return compare_grades(self.grades, other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades_from_students = {}

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за лекции: {round(average_rating(self.grades_from_students), 1)}")
        return ""

    def __cmp__(self, other):
        if isinstance(other, Lecturer):
            return compare_grades(self.grades_from_students, other.grades_from_students)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        return ""


def average_students_rating_by_course(students, course):
    average_ratings_student = 0
    sum_students = 0
    if students is not None:
        for student in students:
            if student.grades.get(course) is not None:
                sum_rating = 0
                quantity_ratings = 0
                for rate in student.grades.get(course):
                    sum_rating += rate
                    quantity_ratings += 1
                average_ratings_student += sum_rating / quantity_ratings
                sum_students += 1
        if sum_students != 0:
            return average_ratings_student / sum_students
    return -1


def average_lecturer_rating_by_course(lecturers, course):
    sum_rating = 0
    quantity_ratings = 0
    average_ratings_lecturer = 0
    sum_lecturers = 0
    for lecturer in lecturers:
        for rate in lecturer.grades_from_students.get(course):
            sum_rating += rate
            quantity_ratings += 1
        if quantity_ratings != 0:
            average_ratings_lecturer += sum_rating / quantity_ratings
            sum_lecturers += 1
    if sum_lecturers != 0:
        return average_ratings_lecturer / sum_lecturers
    return -1


students_list = []
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
students_list += [best_student]
ave_student = Student('Ahalay', 'Mahalay', 'What_is_gender?')
ave_student.courses_in_progress += ['Artistic milking']
ave_student.finished_courses += ['Dancing with a tambourine']
students_list += [ave_student]

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Artistic milking']
ave_reviewer = Reviewer('Roger', 'Rabbit')
ave_reviewer.courses_attached += ['Dancing with a tambourine']

lecturers_list = []
cool_lecturer = Lecturer('Filius', 'Flitwick')
cool_lecturer.courses_attached += ['Dancing with a tambourine']
lecturers_list += [cool_lecturer]
cool_lecturer_2 = Lecturer('Genie', 'From the lamp')
cool_lecturer_2.courses_attached += ['Python']
cool_lecturer_2.courses_attached += ['Artistic milking']
cool_lecturer_2.courses_attached += ['Dancing with a tambourine']
lecturers_list += [cool_lecturer_2]

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(ave_student, 'Artistic milking', 1)
cool_reviewer.rate_hw(ave_student, 'Artistic milking', 6)
ave_reviewer.rate_hw(ave_student, 'Dancing with a tambourine', 8)
ave_reviewer.rate_hw(ave_student, 'Dancing with a tambourine', 9)

ave_student.rate_lecturer(cool_lecturer, 'Dancing with a tambourine', 10)
ave_student.rate_lecturer(cool_lecturer, 'Dancing with a tambourine', 9)
ave_student.rate_lecturer(cool_lecturer_2, 'Dancing with a tambourine', 7)
ave_student.rate_lecturer(cool_lecturer_2, 'Dancing with a tambourine', 7)
ave_student.rate_lecturer(cool_lecturer_2, 'Artistic milking', 11)
best_student.rate_lecturer(cool_lecturer_2, 'Python', 4)
best_student.rate_lecturer(cool_lecturer_2, 'Python', 5)

print(best_student)
print(ave_student)
print(cool_lecturer)
print(cool_lecturer_2)
print(cool_reviewer)
print(ave_reviewer)

print(average_students_rating_by_course(students_list, 'Python'))
print(average_lecturer_rating_by_course(lecturers_list, 'Dancing with a tambourine'))