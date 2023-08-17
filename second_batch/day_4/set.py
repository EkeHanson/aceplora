# SET: This is collection that is unordered and unindex.
# It does allow duplicate values
# Sets are declared with curly brackets

utensils = {"Fork", "Spoon", "Knife", "Spoon",  "Jug"}

# utensils.add("Napkin")
# utensils.remove("Knife")
# utensils.clear() #
dishes = {"Bowl","Plate","Cup", "Jug"}

utensils.update(dishes)

# dinner_table = utensils.union(dishes)

# difference = utensils.difference(dishes)

# intersection = utensils.intersection(dishes)


for i in utensils:
    print(i)