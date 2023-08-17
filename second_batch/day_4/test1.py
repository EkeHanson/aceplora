# Lists, Tuples, and Sets Quiz:**

# 1. What is the key difference between a list and a tuple in Python?
# Answer:
# 2. Which of the following data structures is mutable: list, tuple, or set?
# 3. How do you create an empty list in Python?
# 4. Can a list contain elements of different data types?
# 5. What is the primary purpose of using a tuple?
# 6. How do you access the second element in a list or tuple?

numbers = [1, 2, 3, 4, 5, 6]
first = numbers[1]
# 7. Which data structure is used to store a collection of unique and unordered elements?
# ANSWER:  Sets are used to store a collection of unique and unordered elements.

# 8. How do you add an element to the end of a list?

# 9. What is the difference between `append()` and `extend()` methods in lists?

# ANSWER: The `append()` method adds an element to the end of a list,
#  while the `extend()` method adds all elements of an iterable to the end of the list.

# list, tuple, set and dictionary

numbers = [1, 2, 3, 4, 5, 6]
last = [7, 8, 9]
numbers.extend(last)

# print(divmod(40, 19))
# set_numbers = set(numbers)
# print(type(set_numbers))
# for i in numbers:
#     print(i, end="")

# 10. How do you remove an element from a set?
# 11. In a set, are the elements ordered?
# 12. What Python function is used to convert a list into a set?
# 13. Can a tuple be modified after it is created? Why or why not?
# 14. How do you check if an element exists in a set?
# dishes = {"Bowl", "Plate", "Cup", "Jug"}
# if "Bowl" in dishes:
#     print("Bowl is present")

# 15. What is the purpose of using a list comprehension?
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# square = [i * i for i in numbers]
# for i in square:
#     print(i)
# 16. Is a list comprehension applicable to sets?
# 17. How do you find the length of a tuple?
# fishes = ("Croacker", "Tilapia")
# print(len(fishes))

# 18. Can a list have nested lists as elements?
# for i in range(1, 13):
#     for j in range(1, 13):
#         print(str(i), "*", str(j), "=", str(i * j))


# numbers = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# 19. What happens if you try to add a duplicate element to a set?
# fishes = {"Croacker", "Tilapia", "Tilapia"}

# for fish in fishes:
#     print(fish)

# 20. How do you concatenate two lists?

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# square = [i * i for i in numbers]

# main_list = numbers + square
# for i in main_list:
#     print(i)

# 1. The key difference between a list and a tuple is that lists are mutable (can be changed after creation), while tuples are immutable (cannot be changed after creation).
# 2. Lists and sets are mutable data structures.
# 3. You can create an empty list using `my_list = []`.
# 4. Yes, a list can contain elements of different data types.
# 5. Tuples are often used to group related data together and are generally immutable.
# 6. You can access the second element in a list or tuple using indexing: `my_list[1]` or `my_tuple[1]`.
# 7. Sets are used to store a collection of unique and unordered elements.
# 8. You can add an element to the end of a list using the `append()` method.
# 9. The `append()` method adds an element to the end of a list, while the `extend()` method adds all elements of an iterable to the end of the list.
# 10. You can remove an element from a set using the `remove()` or `discard()` method.
# 11. No, the elements in a set are not ordered.
# 12. The `set()` function can be used to convert a list into a set.
# 13. No, a tuple cannot be modified after it is created. Tuples are immutable.
# 14. You can check if an element exists in a set using the `in` keyword.
# 15. List comprehensions provide a concise way to create lists by applying an expression to each item in an iterable.
# 16. Yes, list comprehensions can be adapted to create sets.
# 17. You can find the length of a tuple using the `len()` function.
# 18. Yes, a list can have nested lists as elements.
# 19. If you try to add a duplicate element to a set, it will not be added, and the set will remain unchanged.
# 20. You can concatenate two lists using the `+` operator: `new_list = list1 + list2`.
