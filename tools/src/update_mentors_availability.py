import yaml


def load_yaml(file_path):
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


if __name__ == "__main__":
    yaml_file_path = '../../_data/mentors.yml'
    data = load_yaml(yaml_file_path)
    print(len(data))
