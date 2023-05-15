# -*- coding: utf-8 -*-


#--Petits exercices--#


#entiers 

x = 8
y = 10
z = x + y 

#flottants 

a = 3
b = 2
c = a * b 

#creation chaine de caracteres

str1 = "Bonjour, "
str2 = "Comment vas tu madame ? "
message = str1 + str2

#longueur de la chaine de caracteres 

longueur = len(message)

#creation d'une liste

ma_liste = [1, 2, 3, 4, 5]

#ajouter un element a la fin de la liste
ma_liste.append(6)

#supprimer un element de la liste
ma_liste.remove(3)

#recuperer un element de la liste
troisieme_element = ma_liste[0]

#print(ma_liste)
#print(troisieme_element)

#creer un tuple 

mon_tuple = ("pomme", "banane", "cerise")

#acceder à un element du tuple 
deuxieme_element = mon_tuple[1]

#print(mon_tuple)
#print(deuxieme_element)

#creer un dictionnaire 

mon_dictionnaire = {"nom": "Judith", "age": 30, "ville": "Paris"}

#acceder à une valeur du dictionnaire

age = mon_dictionnaire["age"]

#modifier une valeur du dictionnaire
mon_dictionnaire["ville"] = "Marseille"

#ajouter une paire clé-valeur au dictionnaire 

mon_dictionnaire["profession"] = "Data scientist"

#print(age)
#print(mon_dictionnaire)

##--Les operateurs et les expressions--##

#-les operateurs arithmetiques-#

#Addition 

a = 5
b = 3
c = a + b

#Soustraction 

b = 5
c = 3
d = b - c

#Multiplication  

e = 5
f = 3
g = e * f

#Division 

h = 5
i = 3
j = h / i

#Modulo 

k = 8
l = 3
m = 8 % 3

#puissance 

n = 2
o = 3
p = n ** o


#-les operateurs de comparaison-#

#Comparaison d'égalité

r = 5
s = 3
t = (r == s)

#Comparaison de différence

u = 5
v = 3
w = ( u != v)

#Supériorité

x = 5
y = 3
z = ( x > y)

#Infériorité 

a = 5
b = 3
c = ( a < b)

#Supériorité ou égalité 

d = 5
e = 3
f = ( d >= f)

#Infériorité ou égalité 


g = 5
h = 3
i = ( g <= h)


#-les operateurs logiques-#

#Et (and)

a = True
b = False
c = a and b 

#Ou  (or)

df = False
eh = False
ff = df or eh 

# Non (not)

g = False
h = not g

#-Les expressions conditionnelles -# 
#Expression conditionnelle 

i = 5
j = 3
k = 10 if i > j else 2 


##--Les fonctions--##

#Definir une fontcion 

def somme(a, b):
    return a + b

#Appeler une fonction 

cc = somme(2, 3)

#Arguments de fonction 
def multiplication(a, b=2):
    return a * b

c = multiplication(1)
d = multiplication(2, 3)

#Variables locales et globales

#variable globale 
aa = 1 


def ma_fonction():
    b = 5 #variable locale 
    print (aa + b) #sortie 6

ma_fonction()

#Fonctions anonymes (lambda)

carre = lambda x: x**2
print(carre(3))


#Les boucles for et while

#for ii in range(5):
 #   print(ii)


#count = 0 
#while count < 5:
 #   print(count)
#count =+ 1

#Programmation Orientée Objet

# Création d'une classe Eleve
class Eleve :
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print("Je m'appelle", self.nom, "et j'ai", self.age, "ans.")

# Création d'un objet eleve.
Arthur = Eleve("Arthur", 25)
Arthur.se_presenter()













