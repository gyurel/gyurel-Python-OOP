from unittest import TestCase, main
from student.project.student import Student


class TestingStudent(TestCase):

    def test_student_initialization_with_passed_course_dict(self):
        student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})

        self.assertEqual('Name', student.name)
        self.assertEqual({'Python': ['Fundamentals', 'Advanced']}, student.courses)

    def test_student_initialization_without_passed_courses_dict(self):
        student = Student('Name')

        self.assertEqual('Name', student.name)
        self.assertEqual({}, student.courses)

    def test_if_enroll_method_returns_proper_str_and_adds_the_notes_when_the_course_already_exist_in_dict(self):
        student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})

        expected = student.courses['Python'] + [x for x in ['Web', 'Python DB']]

        self.assertEqual("Course already added. Notes have been updated.",
                         student.enroll('Python', ['Web', 'Python DB']))
        self.assertEqual(expected, student.courses['Python'])

    def test_if_enroll_method_returns_proper_str_and_the_course_and_notes_when_add_course_notes_Y_or_space(self):

        for note in ["Y", ""]:
            student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})
            new_course_name = 'JavaScript'
            notes = ['React Framework', 'Json']
            expected = ['React Framework', 'Json']

            self.assertEqual("Course and course notes have been added.", student.enroll(new_course_name, notes, note))
            self.assertEqual(expected, student.courses[new_course_name])

    def test_course_name_not_in_dict_and_add_course_notes_different_than_Y_or_space(self):
        student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})
        new_course_name = 'JavaScript'
        notes = ['React Framework', 'Json']
        expected = []

        self.assertEqual("Course has been added.", student.enroll(new_course_name, notes, 'A'))
        self.assertEqual(expected, student.courses[new_course_name])

    def test_add_notes_behaves_properly_when_adding_notes_to_existing_course(self):
        student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})
        course_name = 'Python'
        notes = 'Django'
        expected = student.courses['Python']
        expected.append(notes)

        self.assertEqual("Notes have been updated", student.add_notes(course_name, notes))
        self.assertEqual(expected, student.courses[course_name])

    def test_add_notes_raises_exeption_when_course_not_in_courses(self):
        student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})
        new_course_name = 'JavaScript'
        notes = ['React Framework', 'Json']
        expected = "Cannot add notes. Course not found."

        with self.assertRaises(Exception) as context:
            student.add_notes(new_course_name, notes)

        self.assertEqual(expected, str(context.exception))

    def test_if_leave_course_removes_existing_course_with_proper_string_returned(self):
        student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})
        course_name = 'Python'
        expected = "Course has been removed"

        self.assertEqual(expected, student.leave_course(course_name))
        self.assertEqual(True, course_name not in student.courses.keys())

    def test_if_leave_course_raises_exeption_if_course_not_in_courses(self):
        student = Student('Name', {'Python': ['Fundamentals', 'Advanced']})
        course_name = 'JavaScript'
        expected = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as context:
            student.leave_course(course_name)

        self.assertEqual(expected, str(context.exception))


if __name__ == '__main__':
    main()
