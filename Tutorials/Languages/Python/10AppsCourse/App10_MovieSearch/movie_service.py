import collections
import requests

MovieResult = collections.namedtuple(
    "MovieResult",
    "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")


def find_movies(text):
    if not text:
        raise ValueError("Search text is required.")  # 'throw' exception.

    url = "http://movie_service.talkpython.fm/api/search/{}".format(text)
    resp = requests.get(url)
    resp.raise_for_status()  # Would throw an exception if the response is not a successful status code.
    movie_data = resp.json().get("hits")

    # Old way of mapping a dictionary to a named tuple.
    # movies = []
    # for data in movie_data:
    #     movie = MovieResult(
    #         imdb_code=data.get("imdb_code"),
    #         title=data.get("title"),
    #         duration=data.get("duration"),
    #         director=data.get("director"),
    #         year=data.get("year"),
    #         rating=data.get("rating"),
    #         imdb_score=data.get("imdb_score"),
    #         keywords=data.get("keywords"),
    #         genres=data.get("genres")
    #     )
    #     movies.append(movie)

    # New way.
    # New way with **kwargs, usually used in method parameters to say that aany other arguments passed in is accepted.
    # Those extra arguments will be passed in as a dictionary.
    # movies = []
    # for data in movie_data:
    #     movie = MovieResult(**data)  # Since the keys match up, we are passing in a dictionary. KEYS HAVE TO MATCH UP.
    #     movies.append(movie)

    # Using list comprehension.
    movies = [
        MovieResult(**data)
        for data in movie_data
    ]

    movies.sort(key=lambda m: -m.year)  # To reverse the sort, simply place a negative sign.
    return movies
