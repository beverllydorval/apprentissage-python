# -*- coding: utf-8 -*-


#Petits exercices 

#entiers 

x = 8
y = 10
z = x + y 

print(z)

#flottants 

a = 3
b = 2
c = a * b 
print (c)

#creation chaine de caracteres

str1 = "Bonjour, "
str2 = "Comment vas tu madame ? "
message = str1 + str2
print(message)

#longueur de la chaine de caracteres 

longueur = len(message)
print(longueur)

#creation d'une liste

ma_liste = [1, 2, 3, 4, 5]

#ajouter un element a la fin de la liste
ma_liste.append(6)

#supprimer un element de la liste
ma_liste.remove(3)

#recuperer un element de la liste
troisieme_element = ma_liste[0]

print(ma_liste)
print(troisieme_element)

#creer un tuple 

mon_tuple = ("pomme", "banane", "cerise")

#acceder à un element du tuple 
deuxieme_element = mon_tuple[1]

print(mon_tuple)
print(deuxieme_element)

#creer un dictionnaire 

mon_dictionnaire = {"nom": "Judith", "age": 30, "ville": "Paris"}

#acceder à une valeur du dictionnaire

age = mon_dictionnaire["age"]

#modifier une valeur du dictionnaire
mon_dictionnaire["ville"] = "Marseille"

#ajoutr une paire clé-valeur au dictionnaire 

mon_dictionnaire["profession"] = "Data scientist"

print(age)
print(mon_dictionnaire)
