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
    if ligne["cote_rangement"]==ligne["cote_rangement"] in bibliotheque:
        print(f"Le livre {ligne["cote_rangement"]} ---- {ligne["titre"]} par {ligne["auteur"]} ---- est déjà présent dans la bibliothèque")
    else: 
        bibliotheque.update({"titre":ligne["titre"], "auteur": ligne["auteur"], "date_publication": ligne["date_publication"]})
        print(f"Le livre {ligne["cote_rangement"]} ---- {ligne["titre"]} par {ligne["auteur"]} ---- a été ajouté avec succès")

    

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






