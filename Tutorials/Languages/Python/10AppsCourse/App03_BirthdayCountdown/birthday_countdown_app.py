import platform
from datetime import date
from Common import app


def get_birthday():
    year = int(input("What year were you born in [YYYY]? "))
    month = int(input("What month were you born in [MM[? "))
    day = int(input("What day were you born in [DD]? "))

    return date(year, month, day)


def calculate_days(bday, todays_date):
    bday = date(year=todays_date.year, month=bday.month, day=bday.day)

    return (bday - todays_date).days


def print_birthday_info(bday, number_of_days):
    #  Windows would use '#' to specify no use of zero padding. Linux (Mac?) use '-'.
    if OS == "Windows":
        formatted_date = date.strftime(bday, "%#m/%#d/%Y")
    else:
        formatted_date = date.strftime(bday, "%-m/%-d/%Y")
    print("It looks like you were born on {}".format(formatted_date))

    if number_of_days > 0:
        message = "Looks like your birthday is in {} day(s)!\nHope you're looking forward to it!".format(number_of_days)
    elif number_of_days < 0:
        message = "You had your birthday {} day(s) ago this year. \nHope you had a good one!".format(-number_of_days)
    else:
        message = "Today is your birthday!\nHappy Birthday!"

    print(message)


""" Main """
OS = platform.system()
app.print_title("Birthday App")

birthday = get_birthday()
today = date.today()
days = calculate_days(birthday, today)

print_birthday_info(birthday, days)
