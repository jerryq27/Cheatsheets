from App04_PersonalJournal import journal
from Common import app


def run_event_loop():
    print("What do you want to do?")

    journal_name = "Default"
    journal_data = journal.load(journal_name)  # [] or list() can also be used.

    user_input = "null"
    while user_input != "X" and user_input:  # Same as saying user_input != '', since empty collections are false.
        user_input = input("[L]ist entries, [A]dd an entry, E[x]it: ").upper().strip()

        if user_input == "L":
            list_entries(journal_data)
        elif user_input == "A":
            entry = input("Enter your journal entry: ")
            journal.add_entry(entry, journal_data)
        elif user_input != "X" and user_input:
            print("'{}' isn't a valid command.".format(user_input))

    journal.save(journal_name, journal_data)


def list_entries(data):
    size = len(data)

    message = None
    if size > 1:
        message = "Your {} journal entries:".format(size)
    elif size == 1:
        message = "Your {} journal entry:".format(size)
    elif size == 0:
        message = "There are no entries."
    print(message)

    entries = reversed(data)  # To display the newest entry first.
    for i, entry in enumerate(entries):  # 'enumerate' pairs each item in a collection to their index as tuples.
        print(i + 1, entry, sep=". ")


# Python convention. Checks to make sure this script is the entry point of the program,
# instead of an import. Otherwise, this code would run if we imported this module.
# If this was an import, __name__ would be the module name.
if __name__ == "__main__":
    app.print_title("Personal Journal App")
    run_event_loop()