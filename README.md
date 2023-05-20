# Python DYMA

**Apprentissage de python avec la plateforme de dyma.**
Python est un interpréteur, il en existe énormément tel que :

```dif
+ CPYTHON (_le plus connu_)
+ PYPY
+ JAPY
```

CONVENTION RECOMMANDEE A UTILISEE EN PYTHON, LE **SNAKE_CASE**

## Menu

1. Installation
    1. Instalation sur Windows
    2. Installation sur Mac
    3. Installation sur Linux
2. Quelques commandes
3. Les bases de Python
    1. Exécution d'un premier fichier
    2. Les variables
    3. Les types natifs

---

### 1 - Installation

> Tu vas pouvoir installer Python sur chacun des systèmes d'exploitation en sachant que sur certains, il est installé par défaut.

#### 1.1 - Installation sur Windows

**L'interpréteur Python inclut le langage python**
On récupère python à cette adresse: [https://www.python.org/downloads/]

**/!\ IMPORTANT**
Lors de l'installation il faut bien cocher l'ajout de l'exécutable dans le **PATH** de windows.

#### 1.2 - Installation sur Mac

**L'interpréteur Python inclut le langage python**
On récupère python à cette adresse: [https://www.python.org/downloads/]

```sh
# une commande + TABULATION pour voir les versions installés
python # tab 2x
```

#### 1.3 - Installation sur Linux

> Python est déjà installé par défaut

```sh
# une commande + TABULATION pour voir les versions installés
python # tab 2x
```

Ouvrir le terminal **CTRL + T**.
Saisir dans le terminal:
**Les commandes sont issuent de ce dépot très connu:** [https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa]

```sh
# installer la dernière version de Python

# 1 - Ajout du ppa + mise à jour
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# 2 - Installation de Python 3.11
sudo apt install python3.11

# Enfin pour lancer l'interpréteur 3.11 il suffit de faire
python3.11
```

---

### 2 - Quelques commandes

```python
# Connapitre la version utilisé (pour windows)
python --version
# Connaitre la version utilisé (pour linux)
python3 --version

# Quitter l'interpréteur
exit()

# Ecrire un commentaire
# Tout les commentaires commence par un "#" tout simplement

# Récupérer le type d'une variable
print( type(nom_de_la_variable_à_évaluer) )
```

---

### 3 - Les bases de Python

#### 3.1 - Exécution d'un premier fichier

```sh
# création d'un fichier bases.py pour apprendre la syntaxe de base de python
touch bases.py
```

Dans le fichier fraîchement créé on saisira:

```python
# Afficher bonjour
print("Bonjour le monde")
```

Dans le terminal on affichera le contenu du script avec cette commande:

```sh
# Exécute le fichier bases.py (pour windows)
python bases.py
# ou
py bases.py

# Exécute le fichier bases.py (pour Linux)
python3 bases.py
```

#### 3.2 - Les variables

```python
# types de variables possible (POKER)
nom = "Guillon"
prenom = "Alain"
age = 38
solde = 1000.0

# Utilisation d'un f-string
print(f"{nom} {prenom} a {age} ans et il démarre le jeu avec un solde de {solde} euros")
# Résultat:
#   Guillon Alain a 38 ans et il démarre le jeu avec un solde de 1000.0 euros
```

#### 3.3 - Les types natifs

```python
# Nombres entiers           -   int
# Nombre décimaux           -   float
# Chaînes de caractères     -   str
# Booléens                  -   bool    (True et False et non true et false)
# listes                    -   list    (équivalent tableaux dans d'autres langages)
# tuple                     -   tuple   (Ne peut pas être modifié)
# Ensembles                 -   set     (Une seule valeur dans une séquence)
# Dictionnaires             -   dict    (Ressemble à un objet JS "clé" "valeur")
# Absence de valeur         -   None
```

```python
# Nombres entiers           -   int
points = 153
print(f"points: {points} est du type { type(points)}")
# Résultat : points: 153 est du type <class 'int'>
```

```python
# Nombre décimaux           -   float
prix = 69.99
print(f"prix: {prix} est du type { type(prix)}")
# Résultat : prix: 69.99 est du type <class 'float'>
```

```python
# Chaînes de caractères     -   str
message_bienvenue = "Bonjour, bienvenue sur ce programme"
print(f"message_bienvenue: {message_bienvenue} est du type { type(message_bienvenue)}")
# résultat : message_bienvenue: Bonjour, bienvenue sur ce programme est du type <class 'str'>
```

```python
# Booléens                  -   bool    (True et False et non true et false)
vrai = True
print(f"vrai: {vrai} est du type { type(vrai)}")
# Résultat : vrai: True est du type <class 'bool'>
faux = False
print(f"faux: {faux} est du type { type(faux)}")
# Résultat : faux: False est du type <class 'bool'>
```

```python
# listes                    -   list    (équivalent tableaux dans d'autres langages)
personne_modifiable = [25, "Camille", "Morin"]
```

```python
# tuple                     -   tuple   (Ne peut pas être modifié)
personne_non_modifiable = (25, "Camille", "Morin")
```

```python
# Ensembles                 -   set     (Une seule valeur dans une séquence)
notes = {3, 20, 20, 19, 16, -2.2}
print(f"Notes: {notes} est du type { type(notes)}")
# Résultat : Notes: {16, 3, 19, 20, -2.2} est du type <class 'set'>
```

```python
# Dictionnaires             -   dict    (Ressemble à un objet JS "clé" "valeur")
personne = {
    "nom": "Morin",
    "prenom": "Camille",
    "age": 25
}
print(f"Personne: {personne} est du type { type(personne)}")
# Résultat : Personne: {'nom': 'Morin', 'prenom': 'Camille', 'age': 25} est du type <class 'dict'>
print(f"{personne['prenom']} {personne['nom']} a {personne['age']} ans.")
# Résultat : Camille Morin a 25 ans.
```

```python
# Absence de valeur         -   None
informaticienne = None
print(f"Informaticienne: {informaticienne} est du type { type(informaticienne)}")
# Résultat : Informaticienne: None est du type <class 'NoneType'>
```
