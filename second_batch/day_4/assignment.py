# ASSINMENT ON DICTIONARY

# 1. How do you create an empty dictionary?
# 2. What is the purpose of a dictionary in Python?
# 3. Can a dictionary store duplicate keys?
# 4. How do you access the value associated with a specific key in a dictionary?
# 5. What happens if you try to access a key that doesn't exist in a dictionary?
# 6. How do you add a new key-value pair to an existing dictionary?
# 7. How do you update the value associated with a specific key in a dictionary?
# 8. How do you remove a key-value pair from a dictionary?
# 9. How do you retrieve all keys from a dictionary?
# 10. How do you retrieve all values from a dictionary?
# 11. How do you iterate through the keys of a dictionary?
# 12. How do you iterate through the values of a dictionary?
# 13. How do you iterate through both keys and values of a dictionary simultaneously?
# 14. Can a dictionary have a list as a value?
# 15. How do you check if a key exists in a dictionary?
# 16. How do you find the number of key-value pairs in a dictionary?
# 17. How do you clear all the elements from a dictionary?
# 18. How can you create a copy of a dictionary?
# 19. How do you merge two dictionaries in Python 3.5+?
# 20. What is the built-in method to get a list of tuples representing key-value pairs from a dictionary?


# 1. To create an empty dictionary, you can use: `my_dict = {}` or `my_dict = dict()`.
# 2. The purpose of a dictionary in Python is to store and manage data in key-value pairs.
# 3. No, a dictionary cannot store duplicate keys. Each key must be unique.
# 4. You can access the value associated with a specific key using indexing: `value = my_dict[key]`.
# 5. If you try to access a key that doesn't exist in a dictionary, it will raise a `KeyError` exception.
# 6. To add a new key-value pair to an existing dictionary, you can assign a value to the new key: `my_dict[new_key] = value`.
# 7. To update the value associated with a specific key, you can reassign a new value to that key: `my_dict[key] = new_value`.
# 8. To remove a key-value pair from a dictionary, you can use the `del` statement: `del my_dict[key]`.
# 9. You can retrieve all keys from a dictionary using the `keys()` method: `keys_list = list(my_dict.keys())`.
# 10. You can retrieve all values from a dictionary using the `values()` method: `values_list = list(my_dict.values())`.
# 11. You can iterate through the keys of a dictionary using a `for` loop: `for key in my_dict:`.
# 12. You can iterate through the values of a dictionary using a `for` loop and the `values()` method: `for value in my_dict.values():`.
# 13. You can iterate through both keys and values using the `items()` method: `for key, value in my_dict.items():`.
# 14. Yes, a dictionary can have a list (or any other data type) as a value.
# 15. To check if a key exists in a dictionary, you can use the `in` keyword: `if key in my_dict:`.
# 16. You can find the number of key-value pairs in a dictionary using the `len()` function: `num_pairs = len(my_dict)`.
# 17. To clear all elements from a dictionary, you can use the `clear()` method: `my_dict.clear()`.
# 18. To create a copy of a dictionary, you can use the `copy()` method: `new_dict = my_dict.copy()`.
# 19. To merge two dictionaries in Python 3.5+, you can use dictionary unpacking: `merged_dict = {**dict1, **dict2}`.
# 20. The built-in method to get a list of tuples representing key-value pairs from a dictionary is the `items()` method: `items_list = list(my_dict.items())`.
