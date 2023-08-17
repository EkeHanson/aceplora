# A Dictionary is a changeable unordered collection of unique key:value  pairs
countries = {
    "Nigeria": "Abuja",
    "USA": "Washington DC",
    "Ghana": "Accra",
    "India": "New Dheli",
    "China": "Beijing",
    "Russia": "Moscow",
}
countries["Japan"] = "Tokyo"
countries.update({"USA": "Los Angeles"})
countries.pop("Russia")
# countries.clear()
# print(countries["USA"])
# print(countries["Nigeria"])

for key, value in countries.items():
    # print(value)
    # print(key)
    print(key, ":", value)
    # print(countries.items())
    # print(countries.keys())
    # print(countries.values())


# class work
# Create a dictionary name students with names = Hermione, Harry, Ron aand Draco
# Their corresponding houses are                Griffyndor, Griffyndor, Griffyndor and Slytherin
name = {
    "email": "ekenehanson@gmail.com",
    "age": 12,
    "is_human": True,
    "height": 23.45,
    "has_bad_credit": False,
}
