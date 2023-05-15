# -*- coding: utf-8 -*-

# On commence par importer numpy en lui donnant l'alias "np" 
import numpy as np

#Creer un tableau NumPy a une dimension

arr_1 = np.array([1, 2, 3, 4, 5])

#Créer un tableau NumPy à deux dimensions
arr_2 = np.array ([[1, 2, 3 ], [4, 5, 6], [7, 8, 9]])


#Créer tableau numPy vide avec 5 éléments 

arr3 = np.empty(5)

print(arr3)

#Créer un tableau numPy de zéros 

arr4 = np.zeros(5)

print(arr4)

#Créer un tableau numPy de 1 

arr5 = np.ones(10)

print(arr5)

#Créer tableau numPy avec des valeurs aléatoires

arr6 =np.random.rand(5)

print(arr6)

#--Indexer et manipuler un tableau NumPy--#


#Etape 1 : créer un tableau numPy unidimensionnel 

arr = np.array ([1, 2, 3, 4, 5])

#Etape 2 : accéder à un élément du teable en utilisant son index 

print(arr[0])
print(arr[2])

#Etape 2bis :  accéder à un élément du teable en utilisant un index négatif (permet d'accéder à des éléments à partir de la fin du tableau)

print(arr[-1])
print(arr[-4])

#Pareil, mais pour un tableau multidimensionnel 

#Etape 1 : Créer un tableau numPy à deux dimensions : 

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Accéder à un élément du tableau. 

#Process : on commence par spécifier l'indice de la dimension, puis le deuxième

#Exemple : correspond au dernier tableau, et au dernier élément du tableau
print(arr[2, 2])
#Exemple: fait référence au premier tableau, et à son premier élément
print(arr[0, 0])


## Accéder à une ligne ou une colonne d'un tablau numPy multidimensionnel 

#Etape 1 : création d'un tableau numPy à 2 dimensions 

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2)

#On accède à une colonne du tableau 
print(arr[:, 1]) #Permet d'afficher la deuxième colonne 
print(arr[:, 0]) #Permet d'afficher la première colonne 
print(arr[:, 2]) #Permet d'afficher la troisième colonne 

#Accéder à plusieurs colonnes du tableau 
print(arr[:, [0, 2]]) #affiche la première et la troisième colonne
print(arr[:, [1, 2]]) #affiche la seconde et la troisième colonne

#Accéder à une ligne du tableau 
print(arr[1, :]) #affiche la seconde ligne du tableau
print(arr[0, :]) #affiche la première ligne du tableau

#Convertir une ligne en tableau unidimensionnel 

row = arr[1, :]
row_arr = row.reshape(1, -1)
print(row_arr)


#-Indexation par booléens avec NumPy-# 


#Tableau Numpy a un dimension 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Creer un masque booléen 
mask = arr % 2 == 0 # on selectionne les elements pairs

#Selectionner les elements du tableau qui corresondent au masqu boolen 
result = arr[mask]

print(result)