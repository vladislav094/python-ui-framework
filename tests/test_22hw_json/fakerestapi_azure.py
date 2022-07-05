import random
from datetime import date, datetime

import requests

check_swagger = requests.get("https://fakerestapi.azurewebsites.net/index.html")
print(f"Status request 'check_swagger': {check_swagger}")


"""Get list with all authors"""
get_authors_list = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors")
print(f"Status request 'get_author_list': {get_authors_list}")

"""You can use this print how optional opportunity to view all list of author in console"""
# list_author = print(*get_authors_list.text.split('},'), sep='\n')


"""Get random ID author for request get_author"""
random_id_author = random.randint(1, 500)


"""Get author with ID from variable random_id_author"""
get_author = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Authors/{random_id_author}")
print(f"Author's data with ID {random_id_author}: {get_author.text}")

"""Data new book for adding in list other books"""
data_book = {
    "id": random.randint(9, 100),
    "title": "string",
    "description": "string",
    "pageCount": random.randint(300, 500),
    "excerpt": "string",
    "publishDate": f"{str(date.today())}T{str(datetime.time(datetime.now()))}",
}

"""Request for adding new book with data from variable data_book"""
add_new_book = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Books", json=data_book)
print(f"Status request 'add_new_book': {add_new_book}")
print(add_new_book.text)

"""Data new user for adding in list other users"""
userName = "Wilfredo Pareto"
data_user = {"id": random.randint(1, 100), "userName": userName, "password": str(random.randint(123456, 999999))}

"""Request for create new user"""
add_new_user = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Users", json=data_user)
print(f"Status request 'add_new_user': {add_new_user}")
print(add_new_user.text)


id_book_for_update = 10
"""Data book with ID from variable id_book_for_update for update this book"""
data_book_for_update = {
    "id": id_book_for_update,
    "title": "string",
    "description": "string",
    "pageCount": random.randint(300, 500),
    "excerpt": "string",
    "publishDate": f"{str(date.today())}T{str(datetime.time(datetime.now()))}",
}

"""Request for view book with ID from variable id_book_for_update"""
get_book = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Books/{id_book_for_update}")
print(f"Data book with ID {id_book_for_update} before update: {get_book.text}")


"""Request for update data from variable data_book_for_update for book with ID from variable id_book_for_update"""
update_book = requests.put(
    f"https://fakerestapi.azurewebsites.net/api/v1/Books/{id_book_for_update}", json=data_book_for_update
)
print(f"Status request 'update_book': {update_book}")
print(f"Data book with ID {id_book_for_update} after update: {update_book.text}")

"""ID user for next actions"""
id_user = 4

"""Get user with ID from variable id_user"""
get_user = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Users/{id_user}")
print(f"Status request 'get_user': {get_user}")
print(f"Data user with ID {id_user} before deletion this user: {get_user.text}")

"""Delete user with id from variable id_user"""
delete_user = requests.delete(f"https://fakerestapi.azurewebsites.net/api/v1/Users/{id_user}")
print(f"Status request 'delete_user': {delete_user}")

delete_user_text = delete_user.text
if len(delete_user_text) == 0:
    delete_user_text = "The user with the specified ID was not found"

print(f"Data user with ID {id_user} after deletion: {delete_user_text}")
