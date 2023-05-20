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