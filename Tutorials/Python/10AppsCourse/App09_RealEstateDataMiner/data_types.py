
class Purchase:

    def __init__(self, street, city, zipcode, state, beds, baths, sq_ft, home_type, sale_data, price, lat, lon):
        self.lon = lon
        self.lat = lat
        self.price = price
        self.sale_data = sale_data
        self.home_type = home_type
        self.sq_ft = sq_ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zipcode = zipcode
        self.city = city
        self.street = street

    @staticmethod  # Marks a method as a static method.
    def create_from_dict(lookup):
        return Purchase(
            lookup["street"],
            lookup["city"],
            lookup["zip"],
            lookup["state"],
            int(lookup["beds"]),
            int(lookup["baths"]),
            int(lookup["sq__ft"]),
            lookup["type"],
            lookup["sale_date"],
            float(lookup["price"]),
            float(lookup["latitude"]),
            float(lookup["longitude"])
        )
