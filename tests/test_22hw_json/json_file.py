import itertools
import json
from pprint import pprint

'''
These are solutions for 3 points in HW 22-json.docx
'''

with open("students.json") as file:
    stock = json.load(file)

'''Solution 1'''
# def group_by_two_fields(field1: str, field2: str, list_of_dicts: list[dict[str, str]]):
#     result = {}
#     for element in list_of_dicts:
#         key = (element.get(field1), element.get(field2))
#         if key in result:
#             result[key].append(element)
#         else:
#             result[key] = [element]
#     return result
# pprint(group_by_two_fields('Class', 'Club', stock))

'''Solution 2'''
def group_two(class_: str, club: str = None):
    result = {}
    classes = set(element[class_] for element in stock)
    clubs = set(element[club] for element in stock)
    for class_, club in itertools.product(classes, clubs):
        for student in stock:
            if student["Class"] == class_ and student["Club"] == club:
                result.update({student["Name"]: {"Class": class_, "Club": club}})
    print(result)
    for elt in result:
        print(elt)


if __name__ == "__main__":
    group_two("Class", "Club")
