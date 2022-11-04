class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_student_rating(self) -> float:
        if not self.grades:
            return 0
        marks = []
        for mark in self.grades.values():
            marks.extend(mark)
        return sum(marks) / len(marks)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
            \rФамилия: {self.surname}
            \rСредняя оценка за домашние задания: {round(self._average_student_rating(), 1)}
            \rКурсы в процессе изучения: {', '.join(self.courses_in_progress)}
            \rЗавершенные курсы: {', '.join(self.finished_courses)}
        """

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise Exception('wrong input')
        return self._average_student_rating() == other._average_student_rating()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise Exception('wrong input')
        return self._average_student_rating() < other._average_student_rating()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise Exception('wrong input')
        return self._average_student_rating() <= other._average_student_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_lecturer_rating(self) -> float:
        if not self.grades:
            return 0
        marks = []
        for mark in self.grades.values():
            marks.extend(mark)
        return sum(marks) / len(marks)

    def __str__(self):
        return f"""Имя: {self.name}
            \rФамилия: {self.surname}
            \rСредняя оценка за лекции: {round(self._average_lecturer_rating(), 1)}
        """

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('wrong input')
        return self._average_lecturer_rating() == other._average_lecturer_rating()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('wrong input')
        return self._average_lecturer_rating() < other._average_lecturer_rating()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('wrong input')
        return self._average_lecturer_rating() <= other._average_lecturer_rating()


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
        return f"""Имя: {self.name}
            \rФамилия: {self.surname}
        """


def average_rating_by_course(persons_list, course):
    if not isinstance(persons_list, list):
        return "wrong input - not a list"
    ratings = []
    for person in persons_list:
        ratings.extend(person.grades.get(course, []))
    if not ratings:
        return "no marks on this course"
    return round (sum(ratings) / len(ratings), 2)




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

print(average_rating_by_course(students_list, 'Python'))
print(average_rating_by_course(lecturers_list, 'Dancing with a tambourine'))
