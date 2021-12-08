from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student_report_card = StudentReportCard('Nakov', 1)

    def test_student_report_card_initialization_with_valid_arguments(self):
        expected_name = 'Nakov'
        expected_year = 1
        grades_by_subject = {}

        self.assertEqual(expected_name, self.student_report_card.student_name)
        self.assertEqual(expected_year, self.student_report_card.school_year)
        self.assertEqual(grades_by_subject, self.student_report_card.grades_by_subject)

    def test_studen_report_card_init_raises_value_error_with_empty_string_name(self):
        name = ''

        with self.assertRaises(ValueError) as context:
            self.student_report_card.student_name = name

        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_student_report_card_init_raises_value_error_with_invalid_year(self):
        year1 = 0
        year2 = 13

        with self.assertRaises(ValueError) as context:
            self.student_report_card.school_year = year1

        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.student_report_card.school_year = year2

        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_add_grade_adds_the_passed_grade_when_subject_not_in_dictionary(self):
        subject = 'Mathematics'
        grade = 6
        expected = [6]

        self.student_report_card.add_grade(subject, grade)

        self.assertEqual(expected, self.student_report_card.grades_by_subject[subject])

    def test_add_grade_adds_a_grade_when_subject_allready_in_dictionary(self):
        subject = 'Mathematics'
        grade = 6
        expected = [6, 6]
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade)

        self.assertEqual(expected, self.student_report_card.grades_by_subject[subject])

    def test_average_grade_by_subject_returns_proper_string(self):
        subject1 = 'Mathematics'
        subject2 = 'Physics'
        grade = 6
        expected = f"{subject1}: {grade:.2f}\n{subject2}: {grade:.2f}"

        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade)

        self.student_report_card.add_grade(subject2, grade)
        self.student_report_card.add_grade(subject2, grade)
        self.student_report_card.add_grade(subject2, grade)

        self.assertEqual(expected, self.student_report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        subject1 = 'Mathematics'
        subject2 = 'Physics'
        grade = 6
        expected = f"Average Grade: {grade:.2f}"

        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade)

        self.student_report_card.add_grade(subject2, grade)
        self.student_report_card.add_grade(subject2, grade)
        self.student_report_card.add_grade(subject2, grade)

        self.assertEqual(expected, self.student_report_card.average_grade_for_all_subjects())

    def test__repr__if_returns_proper_string(self):
        expected_name = 'Nakov'
        expected_year = 1
        subject1 = 'Mathematics'
        subject2 = 'Physics'
        grade = 6
        expected = f"Name: {expected_name}\n" \
                   f"Year: {expected_year}\n" \
                   f"----------\n" \
                   f"{subject1}: {6:.2f}\n" \
                   f"{subject2}: {6:.2f}\n"\
                   f"----------\n" \
                   f"Average Grade: {6:.2f}"

        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade)

        self.student_report_card.add_grade(subject2, grade)
        self.student_report_card.add_grade(subject2, grade)
        self.student_report_card.add_grade(subject2, grade)

        self.assertEqual(expected, repr(self.student_report_card))


if __name__ == '__main__':
    main()
