import os
import csv
import statistics

from App09_RealEstateDataMiner.data_types import Purchase
from Common import app


def get_data_file():
    base_folder = os.path.abspath(os.path.dirname(__file__))  # Need to call abspath() after a call to dirname().
    return os.path.join(base_folder, "data", "real-estate-data.csv")


def load_data(filename):
    with open(filename, 'r', encoding="utf-8") as input_file:
        # DictReader reads in the csv as a dictionary with the header as the keys.
        reader = csv.DictReader(input_file)
        purchases = []
        for line in reader:
            p = Purchase.create_from_dict(line)
            purchases.append(p)

        # Old way.
        # header = input_file.readline()
        # reader = csv.reader(input_file)
        # for line in reader:
        #     print(line)
    return purchases


def get_price(p):
    return p.price


def query_data(data):
    # data.sort(key=get_price)
    # Using a lambda is cleaner.
    # Basically an inline method.
    # Structure: lambda [args]: [return val]
    data.sort(key=lambda p: p.price)
    highest = data[-1]
    lowest = data[0]
    print("The most expensive house is: ${:,} with {} beds and {} baths.".format(
        highest.price, highest.beds, highest.baths
    ))
    print("The most least expensive house is: ${:,} with {} beds and {} baths.".format(
        lowest.price, lowest.beds, lowest.baths
    ))

    # Find the mean.

    # Old way.
    # purchases = []
    # for purchase in data:
    #     purchases.append(purchase.price)
    # statistics.mean(purchases)

    # Easier approach
    purchases = [
        # You can write an expression here to generate a list. This is a List Comprehension.
        p.price  # 2. First line is the items we want. If there is multiple, use ().
        for p in data  # 2. The source of data.
        # 3. Test
    ]
    print("The average price of the houses is ${:,}".format(statistics.mean(purchases)))

    # Find the mean of two bedroom homes.
    purchases = [
        (p.price)
        for p in data
        if p.beds == 2  # Test condition.
    ]
    print("The average price of 2-bedroom houses is ${:,}".format(statistics.mean(purchases)))

    # Generator methods, the next step from List Comprehensions.
    pass


if __name__ == "__main__":
    app.print_title("Real Estate App")
    filename = get_data_file()
    data = load_data(filename)
    query_data(data)

