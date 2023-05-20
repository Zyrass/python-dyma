# Commentaires
print("Bonjour le monde")

# types de variables possible (POKER)
nom = "Guillon"
prenom = "Alain"
age = 38
solde = 1000.0

# Affiche un message
print(f"{nom} {prenom} a {age} ans et il démarre le jeu avec un solde de {solde} euros")

points = 153
print(f"points: {points} est du type { type(points)}") 

prix = 69.99
print(f"prix: {prix} est du type { type(prix)}")

message_bienvenue = "Bonjour, bienvenue sur ce programme"
print(f"message_bienvenue: {message_bienvenue} est du type { type(message_bienvenue)}")

vrai = True
print(f"vrai: {vrai} est du type { type(vrai)}")
faux = False
print(f"faux: {faux} est du type { type(faux)}")

notes = {3, 20, 20, 19, 16, -2.2}
print(f"Notes: {notes} est du type { type(notes)}")

personne = {
    "nom": "Morin",
    "prenom": "Camille",
    "age": 25
}
print(f"Personne: {personne} est du type { type(personne)}")
print(f"{personne['prenom']} {personne['nom']} a {personne['age']} ans.")

informaticienne = None
print(f"Informaticienne: {informaticienne} est du type { type(informaticienne)}")

a = 1       # int
b = 2.5     # float
c = a + b

print(f"c = {c} (a + b)")
# Réponse : a + b = 3.5
print(f"type : {type(c)}")

d = 1       # int
e = "2"     # str
# f = d + e

# print(f"f = {f} (d + e)")
# Réponse : c = 3.5 (a + b)
# print(f"type : {type(f)}")
# Réponse : type : <class 'float'>

g = 1       # int
h = "2"     # str
i = g + int(h) # <-- casting

print(f"i = {i} (g + h)")
# Réponse : i = 3 (g + h)
print(f"Type: {type(i)}")
# Réponse : Type: <class 'int'>

nombre_a = 69
nombre_b = 69

print(nombre_a == nombre_b)             
print(nombre_a is nombre_b)             
print(f"Nombre A = {id(nombre_a)}")     
print(f"Nombre B = {id(nombre_b)}")     

set_a = {1,2,3,4,5,6,7,8,9}
set_b = {1,2,3,4,5,6,7,8,9}

print(set_a == set_b)             
print(set_a is set_b)             
print(f"Set A = {id(set_a)}")     
print(f"Set B = {id(set_b)}")     

nombre_c = 69
nombre_d = nombre_c

print(nombre_c == nombre_d)             
print(nombre_c is nombre_d)             
print(f"Nombre C = {id(nombre_c)}")     
print(f"Nombre D = {id(nombre_d)}")     