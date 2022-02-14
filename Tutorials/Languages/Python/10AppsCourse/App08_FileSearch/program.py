import os
import collections

from Common import app

SearchResult = collections.namedtuple("SearchResult", "file, line, text")


def get_folder():
    input_folder = input("What folder do you want to search? ")
    if not input_folder or not input_folder.strip():
        return None
    if not os.path.isdir(input_folder):
        return None

    return os.path.abspath(input_folder)


def get_search_text():
    return input("What are you searching for [single phrases only]? ").strip().lower()


def search_folders(search_folder, search_text):
    # all_matches = []
    print("Would search '{}' for '{}'.".format(search_folder, search_text))
    items = os.listdir(search_folder)
    for item in items:
        full_path = os.path.join(search_folder, item)
        if os.path.isdir(full_path):
            # We use recursion to solve directories we find in the specified directory.
            # matches = search_folders(full_path, search_text)
            # all_matches.extend(matches)
            # for m in matches:
            #     yield m
            # ###### OR ###### #
            yield from search_folders(full_path, search_text)
        else:
            # matches = search_file(full_path, search_text)
            # all_matches.extend(matches)  # When adding a single item uses append, adding a collection uses extends.
            # for m in matches:
            #     yield m
            yield from search_file(full_path, search_text)
    # return all_matches


def search_file(full_file_path, search_text):
    # matched_lines = []
    with open(full_file_path, 'r', encoding="utf-8") as input_file:
        for i, line in enumerate(input_file):
            if line.lower().find(search_text) >= 0:  # find() returns a -1 if the string doesn't contain a substring.
                match = SearchResult(file=full_file_path, line=i + 1, text=line.strip())
                # matched_lines.append(match)
                yield match
    # return matched_lines


if __name__ == '__main__':
    app.print_title("File Search App")
    folder = get_folder()
    if not folder:
        print("Folder does not exist.")
    text = get_search_text()
    if not text:
        print("We can't search for nothing!")

    results = search_folders(folder, text)
    for r in results:
        print(r)
