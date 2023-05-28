# -*- coding: utf-8 -*-
""""
import requests
import json
import aiohttp
import asyncio
"""

""""

# GET -- Dans cet exemple, nous utilisons la methode GET pour obtenir la liste des utilisateurs.

url = "https://reqres.in/api/users?page=2"

# Reponse
response = requests.get(url)
if response.status_code == 200:
    users = response.json()
    # Formate la sortie JSON avec indentation
    formatted_output = json.dumps(users, indent=4) 
    print(formatted_output)
else:
    print("Oops ! Une erreur s'est produite.")
    
# POST -- Dans cet exemple, on utilise la methode POST afin d'envoyer les donnees d'un nouvel utilisateur 

url = "https://reqres.in/api/users"
data = {
    "name": "+++Camille",
    "email": "camille@example.com"
}
response = requests.post(url, json=data)

# Reponse
if response.status_code == 201:
    # Utilisateur cree (un seul utilisateur)
    user = response.json() 
    print("Utilisateur cree avec succes")
else:
    print("Oups ! Une erreur s'est produite lors de la creation de l'utilisateur")
'''


url = "https://reqres.in/api/users"
data = {
"name": "+++ Camille",
"email": "camille@example.com"
}
response = requests.post(url, json=data)
if response.status_code == 201:
    user = response.json()
    print(user) 
else:
    print("Oups ! Une erreur s'est produite lors de la creation de l'utilisateur")

'''

# PUT -- ici, nous utilisons la methode PUT afin de mettre a jour les informations d’un utilisateur existant, identifie par l’id “1”

url = "https://reqres.in/api/users/2"
data = {
    "name": "Camille Dupre",
    "email": "camille@example.com"
}
response = requests.put(url, json=data)

# Reponse
if response.status_code == 200:
    print("Utilisateur mis a jour avec succes")
else:
    print("Ooops ! Une erreur s'est produite lors de la mise a jour de l'utilisateur")


# DELETE -- Ici, nous utilisons la methode DELETE afin de supprimer un utilisateur existant, identifie par l'id "2"

url = "https://reqres.in/api/users/2"
response = requests.delete(url)

# Reponse

if response.status_code == 204:
    print("Utilisateur supprime avec succes")
else:
    print("Ooops ! Une erreur s'est produite lors de la suppression de l'utilisateur")
# Ici, nous supprimons l'utilisateur identifie par l'ID 2.


# HEAD -- Ici nous faisons une requête HEAD a l'URL "https://google.com"

url = "https://google.com"
resp = requests.head(url)
print(resp.headers)


# OPTIONS -- Ici nous faisons une requête OPTIONS a l'URL "https://google.com"
url = "https://google.com"

resp = requests.options(url)
print(resp.status_code)
"""

"""""
async def make_request():
    async with aiohttp.ClientSession() as session:
        url = "https://reqres.in/api/users/2"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(data)
            else:
                print("Ooops ! Une erreur s'est produite lors de la requête")

asyncio.run(make_request())
"""
def dis_bonjour():
    print("Bonjour !")

# Appel de la fonction
dis_bonjour()

