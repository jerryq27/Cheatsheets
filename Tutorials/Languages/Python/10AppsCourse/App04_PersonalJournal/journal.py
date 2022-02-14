"""
Module level documentation for the Journal.
"""

import os


def load(name):
    """
    This method loads data from the journal file
    and returns it as a list.

    :param name: The journal's basename.
    :return: The journal's data.
    """
    file_name = get_file_path(name)
    print("... loading from '{}' ...".format(file_name))

    lines = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as input_file:
            for line in input_file.readlines():
                lines.append(line.rstrip())  # right strip.

    size = len(lines)
    message = None
    if size > 1:
        message = "... loaded {} entries ...".format(size)
    elif size == 1:
        message = "... loaded {} entry ...".format(size)
    elif size == 0:
        message = "... No entries to load ..."
    print(message)

    return lines


def save(name, journal_data):
    file_name = get_file_path(name)
    print("... saving to {} ...".format(file_name))

    with open(file_name, 'w') as journal_file:
        for line in journal_data:
            journal_file.write(line + '\n')

    print("... save complete ...")


def get_file_path(name):
    return os.path.join("res", name + ".jrl")


def add_entry(entry, journal_data):
    journal_data.append(entry)
