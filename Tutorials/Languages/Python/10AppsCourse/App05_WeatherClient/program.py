import requests  # Get the HTML.
import bs4  # Parses the HTML.
import collections  # Allows the use of named tuples so we don't need to wokr with indexes.
from Common import app

WeatherReport = collections.namedtuple(
    "WeatherReport",
    "cond, temp, scale, loc"
)


def get_html_from_web(zip_code):
    url = "http://www.wunderground.com/weather-forecast/{}".format(zip_code)
    response = requests.get(url)
    # print(response.status_code)  # This is the code returned by the site (200 is good, 404 or 500, not good).
    return response.text  # Returns the html code from the response.


def parse_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")

    location = soup.find(class_="region-content-header").find("h1").get_text()
    condition = soup.find(class_="condition-icon").find("p").get_text()
    temp = soup.find(class_="test-true").find(class_="wu-value").get_text()
    scale = soup.find(class_="test-true").find(class_="wu-label").get_text()

    location = cleanup_text(location)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # Tuples are defined with commas, not '()'. Also val1, val2, val3 = tuple will unpack a tuple into 3 variables.
    # return condition, temp, scale, location  # You can return multiple values of any type as a tuple.
    return WeatherReport(cond=condition, temp=temp, scale=scale, loc=location)


def cleanup_text(text: str):  # A way to tell Python what kind of data we're expecting, helps people and PyCharm.
    if not text:
        return text

    return text.strip()


if __name__ == "__main__":
    app.print_title("Weather Client App")
    zip_code = input("Enter your zip code (e.g. 97201): ")
    html = get_html_from_web(zip_code)
    report = parse_html(html)
    print("The weather in {} is {} {} and {}.".format(
        # report[3],
        # report[0],
        # report[1],
        # report[2]
        # Better way using named tuples.
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))
