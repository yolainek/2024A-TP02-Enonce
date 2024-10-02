"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Yolaine Ntabugi Karemere (2379172), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

csvfile= open("collection_bibliotheque.csv", newline="")
collection_bibliotheque= csv.DictReader(csvfile)

bibliotheque={ligne["cote_rangement"]:ligne for ligne in collection_bibliotheque}
for i in bibliotheque:
    bibliotheque[i].pop("cote_rangement")
print(f' \n Bibliotheque initiale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

csvfile= open("nouvelle_collection.csv", newline="")
nouvelle_collection= csv.DictReader(csvfile)

for ligne in nouvelle_collection:
    if ligne["cote_rangement"] in bibliotheque:
        print(f"Le livre {ligne["cote_rangement"]} ---- {ligne["titre"]} par {ligne["auteur"]} ---- est déjà présent dans la bibliothèque")
    else: 
        bibliotheque.update({"titre":ligne["titre"], "auteur": ligne["auteur"], "date_publication": ligne["date_publication"]})
        print(f"Le livre {ligne["cote_rangement"]} ---- {ligne["titre"]} par {ligne["auteur"]} ---- a été ajouté avec succès")

    

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

keys_to_change=[]
for cote_rangement in bibliotheque:
    if cote_rangement[0]== "S"and bibliotheque[cote_rangement]["auteur"] == "William Shakespeare":
        new_key = cote_rangement.replace("S","WS")
        keys_to_change.append((cote_rangement, new_key))

for old_key, new_key in keys_to_change:
    bibliotheque[new_key] = bibliotheque.pop(old_key)

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')




########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

csvfile= open("emprunts.csv", newline="")
emprunts= csv.DictReader(csvfile)

for cote_rangement in bibliotheque:
    bibliotheque[cote_rangement]["emprunts"] = "disponible"
    
for ligne in emprunts:
    for cote_rangement in bibliotheque:
        if ligne["cote_rangement"] in bibliotheque:
            bibliotheque[ligne["cote_rangement"]]["emprunts"]= "emprunté"
    





########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






