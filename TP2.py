"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
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


bibliotheque2= {ligne["cote_rangement"]:ligne for ligne in nouvelle_collection}
for i in bibliotheque2:
    bibliotheque2[i].pop("cote_rangement")
    #biblio2.key()
    #for kye,data in dict2 if key in dict2=key in dict1 (update)



    







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






