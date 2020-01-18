import requests
import collections

from App10_MovieSearch import movie_service
from Common import app


def main():
    app.print_title("Movie Search App")
    search_loop()


def search_loop():
    search = None
    while search != 'x':
        try:
            search = input("Movie text to search for (x to exit): ").lower().strip()
            if search != 'x':
                results = movie_service.find_movies(search)
                print("Found {} result(s).".format(len(results)))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
        except ValueError:
            print("Error: Search text is required.")
        except requests.exceptions.ConnectionError as cerr:
            print("Error: No network.")
        except Exception as e:
            print("Something went wrong, details: {}".format(type(e)))  # Using type() can help identify an exception.

    print("Exiting..")


if __name__ == "__main__":
    main()
