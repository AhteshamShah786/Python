# 47.	Write a program to merge two dictionaries and sort the resulting dictionary by key.

def merge_and_sort_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return dict(sorted(merged_dict.items()))

dict1 = {"b": 2, "a": 1}
dict2 = {"d": 4, "c": 3}

print(merge_and_sort_dicts(dict1, dict2))
