import unittest

from src.update_mentors_availability import *

TEST_AVAILABILITY = [5, 6]
TEST_MENTOR_1 = "Rajani Rao"
TEST_MENTOR_2 = "Eleonora Belova"
TEST_MENTOR_3 = "Adriana Zencke Zimmermann"
TEST_MENTORS = [TEST_MENTOR_1, TEST_MENTOR_2]


class TestUpdateMentorsAutomation(unittest.TestCase):

    def setUp(self):
        self.data = load_yaml("../../_data/mentors.yml")

    def test_load_file(self):
        self.assertEqual(89, len(self.data))

    def test_find_existing_item(self):
        mentor = find_mentor_by_name(TEST_MENTOR_1, self.data)
        self.assertIsNotNone(mentor)
        self.assertEqual(mentor['name'], TEST_MENTOR_1)

    def test_find_non_existing_item(self):
        non_existing_item = find_mentor_by_name("Adriana Maria", self.data)
        self.assertIsNone(non_existing_item)

    def test_found_mentors_by_name(self):
        found_mentors = find_mentors_by_names([TEST_MENTOR_1, TEST_MENTOR_2], self.data)
        self.assertEqual(2, len(found_mentors))

    def test_update_mentors_availability(self):
        mentors = update_availability(TEST_MENTORS, TEST_AVAILABILITY, self.data)

        mentor = find_mentor_by_name(TEST_MENTOR_1, mentors)
        self.assertEqual(TEST_AVAILABILITY, mentor.get('availability'))

        mentor = find_mentor_by_name(TEST_MENTOR_2, mentors)
        self.assertEqual(TEST_AVAILABILITY, mentor.get('availability'))

    def test_update_single_mentor_availability_correctly(self):
        mentors = update_availability([TEST_MENTOR_2], TEST_AVAILABILITY, self.data)

        mentor = find_mentor_by_name(TEST_MENTOR_2, mentors)
        self.assertEqual(TEST_AVAILABILITY, mentor.get('availability'))

    def test_update_mentors_availability_without_changes(self):
        mentors = update_availability(TEST_MENTORS, TEST_AVAILABILITY, self.data)

        mentor = find_mentor_by_name(TEST_MENTOR_3, mentors)
        self.assertNotEqual(TEST_AVAILABILITY, mentor.get('availability'))
