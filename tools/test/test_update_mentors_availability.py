import unittest

from src.update_mentors_availability import *


class TestUpdateMentorsAutomation(unittest.TestCase):

    def setUp(self):
        self.data = load_yaml("../../_data/mentors.yml")

    def test_load_file(self):
        self.assertEqual(89, len(self.data))

    def test_find_existing_item(self):
        mentor_name = "Rajani Rao"
        mentor = find_mentor_by_name(mentor_name, self.data)
        self.assertIsNotNone(mentor)
        self.assertEqual(mentor['name'], mentor_name)

    def test_find_non_existing_item(self):
        non_existing_item = find_mentor_by_name("Adriana Maria", self.data)
        self.assertIsNone(non_existing_item)

    def test_found_mentors_by_name(self):
        found_mentors = find_mentors_by_names(["Rajani Rao", "Eleonora Belova"], self.data)
        self.assertEqual(2, len(found_mentors))
