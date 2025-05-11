# Creons la liste beatles
beatles = []

# Ajoutons John Lennon, Paul McCartney et George Harrison
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

# Affichons la liste pour verifier
print(beatles)

# Invitons l'utilisateur a ajouter les membres : Stu Sutcliffe et Pete Beast
for i in range(2):
    # Au premier tour on lui demande d'ajouter Stu Sutcliffe
    if i == 0 :
        member = input("Ajouter Stu Sutcliffe : ")
        beatles.append(member)
    # Et au deuxieme on lui demande d'ajouter Pete Beast
    else:
        member = input("Ajouter Pete Beast : ")
        beatles.append(member)

# Affichons la liste pour verifier
print(beatles)

# Utilisons del pour supprimer Stu Stcliffe et Pete Beast
# Puisque Stcliffe et Pete sont a la 4e et 5e position. De ce fait les indexes 3 et 4
del beatles[3]

# Apres avoir del Stcliffe, la liste est revenu a 4 elements, Pete occupe la position 4 donc l'indexe 3
del beatles[3]

# Affichons la liste pour verifier
print(beatles)

# Utilisons insert pour ajouter Ringo Starr au debut de la liste
beatles.insert(0, 'Ringo Start') 

# Affichons la liste pour verifier
print(beatles)