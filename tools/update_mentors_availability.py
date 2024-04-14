from typing import List
import sys
import yaml
import logging

MENTOR_FILE = '../_data/mentors.yml'


def load_yaml(file_path=MENTOR_FILE):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def update_yaml(file_path, new_data):
    with open(file_path, 'w') as file:
        yaml.dump(new_data, file)


def find_mentor_by_name(name, mentors):
    for mentor in mentors:
        if mentor.get('name') == name:
            return mentor
    return None


def find_mentors_by_names(names, mentors):
    found_mentors = []
    for mentor in mentors:
        if mentor.get('name') in names:
            found_mentors.append(mentor)

    return found_mentors


def update_availability(names: List[str], availability, mentors):
    """Process a list of mentors names and update their availability."""

    for mentor in mentors:
        if mentor.get('name') in names:
            mentor['availability'] = availability

    return mentors


def update_mentors_data(names: List[str], availability):
    """Process a list of mentors names and update their availability."""

    mentors = load_yaml(MENTOR_FILE)

    for mentor in mentors:
        mentor_name = mentor.get('name')
        if mentor_name in names:
            logging.info(f'Updating mentor: {mentor_name}, availability={availability}')

            mentor['availability'] = availability

    update_yaml(MENTOR_FILE, mentors)


def validate_sys_list():
    if not isinstance(sys.argv[1], list):
        raise TypeError("Mentors Names needs to be a list")
    if not isinstance(sys.argv[3], list):
        raise TypeError("Mentors availability needs to be a list")


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if len(sys.argv) != 4:
        logging.error("Usage: python SCRIPT_NAME MENTORS_FULL_NAMES PARAMS_TO_UPDATE NEW_VALUES")
        return

    validate_sys_list()

    mentors_names: List[str] = sys.argv[1]
    attributes = sys.argv[2]
    updated_values = sys.argv[3]

    update_mentors_data(mentors_names, updated_values)


if __name__ == "__main__":
    main()
