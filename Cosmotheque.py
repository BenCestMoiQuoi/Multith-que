#       -*- coding:Utf8 -*-
########################################
#   Programme python
#   Nom : Cosmotheque.py
#   Auteur :    LE GUEN Antonin
#               LE MERCIER Aurore
#               ROCHE Corentin
#   Version : 7
#   Date : 28/11/2022
#########################################
#########################################
#
#   Programme qui fait l'ensemble de l'application :
#       Lecture/écriture dans un fichier csv
#       Lecture/écriture dans un fichier txt
#       Interface graphique et interaction avec l'utilisateur
#       Et qui permet à l'utilisateur de stocké l'ensemble de
#           sa Cosmotheque (Livre, Film, Série, Jeux, Musique, ...)
#           annotté de note et de bien d'autre caractéristique.
#       D'autres fonction sont faite pour le bon déroulement de l'utilisation.
#
#########################################
#########################################
#
# Listes des fonctions dans ce programme :
#       Recherche_all
#       Recherche_Categorie
#       Recherche_Mot_Cles
#       Top10_categorie
#       tri_liste
#       trouver_selection
#       if_login
#       creat_login
#       suppr_note_perso
#       recup_note_perso
#       recup_ligne_csv
#       ouvrir_nperso
#       ouvrir_pdf
#       vider_entre
#       vider
#       message_erreur
#       mdp
#       verif_nombre
#       index
#       creat
#       creer_modif_Film
#       creer_modif_Serie
#       creer_modif_Livre
#       creer_modif_Morceau
#       creer_modif_Jeux_video
#       creer_modif_Jeux_societe
#       creer_modif_Plante
#       ajout_theque
#       modif_theque
#       suppr_theque
#       ajout_csv
#       modif_csv
#       suppr_csv
#       retour
#       validation
#       ajouter
#       changement
#       fen
#
#########################################
#
# Importation des modules :
#       Classes
#
#       tkinter
#       tkinter.messagebox
#       tkinter.ttk
#       os.startfile
#       tkcalendar.DateEntry
#       functools.partial
#       datetime.date
#

from Classes import *

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from os import startfile

from tkcalendar import DateEntry

from functools import partial

#import datetime.date

#########################################
#
# Caractérisation des variables usuels dans ce programme :

Nom_Projet = "Cosmothèque"
User = ""
Liste_Categorie = ['------', 'Film', 'Série', 'Livre', 'Morceau', 'Jeux vidéo', 'Jeux de société', 'Plantes']
Liste_Etat = ["", "A lire", "A acheter", "En cours de lecture", "Lu"]
Liste_Narration = ["", "Je", "Tu", "Il/Elle", "Omnisciente", "Multiple"]
Chemain_Data = "Data\\"
Chemain_pdf = "PDF\\"
Nom_CSV = "Cosmotheque.csv"
Nom_login = "login.txt"
Nom_note_perso = "Note_Perso.txt"


###########################################################
######################## Fonctions ########################
###########################################################

def Recherche_all():
    """
############### Fonction Recherche_Mot_Cles ################
#
#   Prend en argument : Rien
#   Retourne : Une liste
#   Cette fonction permet de trouver une liste trier de
#       l'ensemble des objets de la Cosmotheque de l'utilisateur.
#
###########################################################
    """
    global Cosmotheque
    Retour = []
    for i in Cosmotheque.theque:
        if i.classe != "Plantes" and i.nombre != 0:
            for j in i.theque:
                Retour.append([j.id, i.classe, j.titre, j.createur, j.annee])
        elif i.classe == "Plantes" and i.nombre != 0:
            for j in i.theque:
                Retour.append([j.id, i.classe, j.nom, j.espece])
    return tri_liste(Retour)

def Recherche_Categorie(listeCombo_cat):
    """
############### Fonction Recherche_Mot_Cles ################
#
#   Prend en argument : listeCombo_cat  Tkinter.ComboListe
#   Retourne : Une liste
#   Cette fonction permet de trouver une liste trier selon 
#       la catégorie choisie par l'utilisateur 
#       depuis la Cosmotheque de ce dernier.
#
############################################################
    """
    global Cosmotheque
    Retour = []
    classe = listeCombo_cat.get()
    id_classe = index(classe, Liste_Categorie)
    if Cosmotheque.theque[id_classe].nombre == 0:
        return Retour
    for i in Cosmotheque.theque[id_classe].theque:
        if classe != "Plantes":
            Retour.append([i.id, classe, i.titre, i.createur, i.annee])
        else:
            Retour.append([i.id, classe, i.nom, i.espece])
    return tri_liste(Retour)

def Recherche_Mot_Cles(entre):
    """
############### Fonction Recherche_Mot_Cles ################
#
#   Prend en argument : entre une liste composé d'un Entry et d'un ComboListe
#   Retourne : Une liste
#   Cette fonction permet de trouver une liste trier selon 
#       la catégorie et les mots_clés choisie par l'utilisateur 
#       depuis la Cosmotheque de ce dernier.
#
############################################################
    """
    Retour = []
    mot_cle = entre[0].get()
    classe = entre[1].get()
    id_classe = index(classe, Liste_Categorie)
    if classe == "------":
        pre_Retour = Recherche_all()
    else:
        pre_Retour = Recherche_Categorie(entre[1])
    if pre_Retour == []:
        return Retour
    for i in pre_Retour:
        if mot_cle in i[2]:
            Retour.append(i)
    return Retour


def Top10_Categorie(listeCombo_cat):
    """
############### Fonction Top10_Categorie ################
#
#   Prend en argument : listeCombo_cat   Tkinter.Comboliste
#   Retourne : Une liste
#   Cette fonction permet de trouver une liste trier selon 
#       la catégorie choisie par l'utilisateur et d'en faire un 
#       top 10.
#
##########################################################
    """
    global Cosmotheque
    pre_Retour = Recherche_Categorie(listeCombo_cat)
    classe = listeCombo_cat.get()
    id_classe = index(classe, Liste_Categorie)
    Note = []

    for i in Cosmotheque.theque[id_classe].theque:
        for j in pre_Retour:
            if i.id == j[0] and i.note != "":
                Note.append([i.note, i.id])
                j.append(i.note)
    Note = tri_liste(Note)
    Retour = []
    i = 1
    while i <= len(Note):
        for j in pre_Retour:
            if Note[-i][1] == j[0]:
                Retour.append(j)
        i += 1
    if len(Retour) <= 10:
        return Retour
    else:
        return Retour[0:10]





def tri_liste(liste):
    """
############### Fonction tri_liste ################
#
#   Prend en argument : liste   Une liste
#   Retourne : Une liste
#   Cette fonction permet de trier une liste selon la facon
#       du tri par bulles. Chaque élément doivent être une liste
#       dont l'entier à trier et en position 0.
#
###################################################
    """
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j][0] > liste[j+1][0]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste


def trouver_selection(id, classe):
    """
############### Fonction trouver_selection ################
#
#   Prend en argument : id   Un entier
#                       classe  Un entier
#   Retourne : Une liste
#   Cette fonction permet de trouver les caractéristiques
#       de l'objet sélectionné à modifier.
#
###########################################################
    """
    global Cosmotheque
    id_classe = index(classe, Liste_Categorie)
    for i in Cosmotheque.theque[id_classe].theque:
        if i.id == id:
            if classe == "Film":
                acteurs = ""
                for x in i.acteurs:
                    if acteurs != "":
                        acteurs += ";"
                    acteurs += str(x)
                return [id_classe, id, i.titre, i.annee, i.createur, i.genre, acteurs, i.recompense, i.note, i.prix, i.dat_visio, i.note_perso]
            elif classe == "Série":
                acteurs = ""
                for x in i.acteurs:
                    if acteurs != "":
                        acteurs += ";"
                    acteurs += str(x)
                return [id_classe, id, i.titre, i.annee, i.createur, i.genre, acteurs, i.recompense, i.note, i.plateforme, i.dat_visio, i.der_episode_vu, i.note_perso]
            elif classe == "Livre":
                return [id_classe, id, i.titre, i.annee, i.createur, i.genre, i.recompense, i.etat, i.note, i.prix, i.tome, i.narration, i.note_perso]
            elif classe == "Morceau":
                return [id_classe, id, i.titre, i.annee, i.createur, i.genre, i.recompense, i.prix, i.note]
            elif classe == "Jeux vidéo":
                return [id_classe, id, i.titre, i.annee, i.createur, i.genre, i.recompense, i.note, i.prix, i.console, i.nbh, i.nbjM, i.nbjm, i.note_perso]
            elif classe == "Jeux de société":
                return [id_classe, id, i.titre, i.annee, i.createur, i.genre, i.recompense, i.note, i.prix, i.support, i.nbjm, i.nbjM, i.note_perso]
            elif classe == "Plantes":
                return [id_classe, id, i.nom, i.espece, i.caracteristique, i.luminosite, i.eau, i.pot, i.cache_pot, i.ou_elle_est, i.date, i.note]


def if_login(user, mdp = ""):
    """
############### Fonction if_login ################
#
#   Prend en argument : user    Un string
#                       mdp     un string
#   Retourne : Booléen
#   Cette fonction permet de vérifier dans le fichier de login
#       si le user et le mdp donnés sont bien renseigné et renvoi
#       la variable True, sinon renvoi la variable False.
#
##################################################
    """
    t = Chemain_Data + Nom_login
    f = open(t, 'r')
    lines = f.readlines()
    for i in lines:
        i = i.split(';')
        if i[0] == user and i[1] == mdp:
            return True
        elif i[0] == user and mdp == "":
            return False
    if mdp != "":
        return False
    else:
        return True


def creat_login(user, mdp):
    """
############### Fonction creat_login ################
#
#   Prend en argument : user    Un string
#                       mdp     un string
#   Retourne : Rien
#   Cette fonction permet de rajouter dans le fichier de connexion
#       le mot de passe et le user du nouvel utilisateur
#
#####################################################
    """
    t = Chemain_Data + Nom_login
    f = open(t, 'a')
    f.write(user + ";" + mdp + ';\n')
    f.close()


def suppr_note_perso():
    """
############### Fonction suppr_note_perso ################
#
#   Prend en argument : Rien
#   Retourne : Rien
#   Cette fonction permet de supprimer l'ensemble des caractères
#       dans le fichier note_perso.txt
#
##########################################################
    """
    t = Chemain_Data + Nom_note_perso
    f = open(t, "w")
    # Remplace l'ensemble des caractères par ""
    f.write("")
    f.close()


def recup_note_perso():
    """
############### Fonction recup_note_perso ################
#
#   Prend en argument : Rien
#   Retourne : note_perso   Un string
#   Cette fonction permet de récupérer en une chaine de caractères
#       l'ensemble des lignes du laissé dans le fichier note_perso.txt
#       par l'utilisateur lors de la modification ou la création 
#       d'un object
#
##########################################################
    """
    t = Chemain_Data + Nom_note_perso
    f = open(t, "r")
    lines = f.readlines()
    note_perso = ""
    for i in lines:
        i = i.replace(";", ".,")
        note_perso += str(i)
    return note_perso


def recup_ligne_csv(user = ""):
    """
############### Fonction recup_ligne_csv ################
#
#   Prend en argument : user
#   Retourne : Rien
#   Cette fonction permet de récupérer l'ensemble des lignes du
#       fichier csv pour l'utilisateur donné.
#       Si une ligne ne correspond pas correctement à un type d'objet,
#       elle sera écartée par le bloc (Try/Except)
#
#########################################################
    """
    global Cosmotheque
    Cosmotheque.user = user
    t = Chemain_Data + Nom_CSV
    # Ouverture en lecture du fichier Csv
    f = open(t, 'r')
    objets = []
    for i in f:
        i = i.split(";")
        # Pour chaque classe dans le fichier, on l'étudie pour le rajouter dans la COsmotheque
        # Si une valeur n'est pas correcte, l'objet est écarté
        try:
            id = int(i[0])
            utilisateur = i[1]
            if utilisateur != user and user != "":
                int("Permet de changer de ligne, car c'est impossible de transformer cette phrase en un entier.")
            classe = int(i[2])

            if classe == 1: # Film
                titre = i[3]
                annee = i[4]
                if annee != "":
                    annee = int(annee)
                realisateur = i[5]
                genre = i[6]
                acteurs = i[7].split("!")
                recompense = i[8]
                note = i[9]
                if note != "":
                    note = int(note)
                prix = i[10]
                if prix != "":
                    prix = float(prix)
                date_visio = i[11]
                note_perso = i[12].replace("\\n", "\n").replace('.,', ";")
                plus = Film(id, titre, annee, realisateur, genre, acteurs, recompense, note, date_visio, note_perso, prix)

            elif classe == 2: # Série
                titre = i[3]
                annee = i[4]
                if annee != "":
                    annee = int(annee)
                realisateur = i[5]
                genre = i[6]
                acteurs = i[7].split("!")
                recompense = i[8]
                note = i[9]
                if note != "":
                    note = int(note)
                plateforme = i[10]
                date_visio = i[11]
                dev = i[12]
                note_perso = i[13].replace("\\n", '\n').replace(".,", ";")
                plus = Serie(id, titre, annee, realisateur, genre, acteurs, recompense, note, plateforme, date_visio, dev, note_perso)
            
            elif classe == 3: # Livres
                titre = i[3]
                annee = i[4]
                if annee != "":
                    annee = int(annee)
                auteur = i[5]
                genre = i[6]
                recompense = i[7]
                etat = i[8]
                note = i[9]
                if note != "":
                    note = int(note)
                prix = i[10]
                if prix != "":
                    prix = float(prix)
                tome = i[11]
                if tome != "":
                    tome = int(tome)
                narration = i[12]
                note_perso = i[13].replace("\\n", '\n').replace(".,", ";")
                plus = Livres(id, titre, annee, auteur, genre, recompense, etat, note, prix, tome, narration, note_perso)
            
            elif classe == 4: # Morceau
                titre = i[3]
                annee = i[4]
                if annee != "":
                    annee = int(annee)
                artiste = i[5]
                genre = i[6]
                recompense = i[7]
                prix = i[8]
                if prix != "":
                    prix = float(prix)
                note = i[9]
                if note != "":
                    note = int(note)
                plus = Morceau(id, titre, annee, artiste, genre, recompense, prix, note)
            
            elif classe == 5: # Jeux vidéo
                titre = i[3]
                annee = i[4]
                if annee != "":
                    annee = int(annee)
                studio = i[5]
                genre = i[6]
                recompense = i[7]
                note = i[8]
                if note != "":
                    note = int(note)
                prix = i[9]
                if prix != "":
                    prix = float(prix)
                console = i[10]
                nbh = i[11]
                if nbh != "":
                    nbh = int(nbh)
                nbjM = i[12]
                if nbjM != "":
                    nbjM = int(nbjM)
                nbjm = i[13]
                if nbjm != "":
                    nbjm = int(nbjm)
                note_perso = i[14].replace("\\n", '\n').replace(".,", ";")
                plus = Jeux_Videos(id, titre, annee, studio, genre, recompense, note, prix, console, nbh, nbjM, nbjm, note_perso)
            
            elif classe == 6: # Jeux de Société
                titre = i[3]
                annee = i[4]
                if annee != "":
                    annee = int(annee)
                marque = i[5]
                genre = i[6]
                recompense = i[7]
                note = i[8]
                if note != "":
                    note = int(note)
                prix = i[9]
                if prix != "":
                    prix = float(prix)
                support = i[10]
                nbjM = i[11]
                if nbjM != "":
                    nbjM = int(nbjM)
                nbjm = i[12]
                if nbjm != "":
                    nbjm = int(nbjm)
                note_perso = i[13].replace("\\n", '\n').replace(".,", ";")
                plus = Jeux_Societe(id, titre, annee, marque, genre, recompense, note, prix, support, nbjM, nbjm, note_perso)
            
            elif classe == 7: # Plantes
                nom = i[3]
                espece = i[4]
                caract = i[5]
                luminosite = i[6]
                eau = i[7]
                pot = i[8]
                cache_pot = i[9]
                ou_elle_est = i[10]
                date = i[11]
                note = i[12]
                if note != "":
                    note = int(note)
                plus = Plantes(id, nom, espece, caract, luminosite, eau, pot, cache_pot, ou_elle_est, date, note)
            # Ajout de l'objet dans la bonne classe de la Cosmotheque
            Cosmotheque.theque[classe].theque.append(plus)
            # Recalcul le nombre d'objet dans la COsmotheque
            Cosmotheque.nb_objet_collection()
        except:
            # Ligne qui permet de pouvoir écarter les mauvaises lignes
            int(123)


def ouvrir_nperso(nb, nperso):
    """
############### Fonction ouvrir_nperso ################
#
#   Prend en argument : nb  un entier
#                       nperso  un string
#   Retourne : Rien
#   Cette fonction permet d'ouvrir le fichier texte des notes perso
#       pour que l'utilisateur puisse noter facilement.
#       Le modifie avant si l'utilisateur modifie un objet.
#
#######################################################
    """
    t = Chemain_Data + Nom_note_perso
    if nb == 5: # Si modification d'un objet
        # Ouverture du fichier note_perso
        f = open(t, 'w')
        # Ecriture dans le fichier
        f.write(nperso)
        f.close()
    # Ouverture du fichier pour l'utilisateur
    f = startfile(t)
    message_erreur(5) # Message de rappel de sauvegarde


def ouvrir_pdf(nom, tome):
    """
############### Fonction ouvrir_pdf ################
#
#   Prend en argument : nom     Un string
#                       tome    Un string
#   Retourne : Rien
#   Cette fonction permet d'ouvrir le fichier pdf du 
#       livre si il est dans le dossier PDF.
#       Nom du fichier : titre_tome.pdf dans le dossier PDF
#
#################################################### 
    """
    chemain = Chemain_pdf+nom
    if tome != "":
        chemain += "_"+tome
    chemain += ".pdf"
    try:
        startfile(chemain)
    except:
        message_erreur(6)


def vider_entre(E):
    """
############### Fonction vider_entre ################
#
#   Prend en argument : E   Un tableau
#   Retourne : Rien
#   Cette fonction permet de vider les objets tkinter.Entry
#       du tableau E, des caractère mis précédement.
#
#####################################################
    """
    for i in E:
        vider(i)


def vider(case):
    """
################ Fonction vider ################
#
#   Prend en argument : case    Un objet tkinter d'entrée
#   Retourne : Rien
#   Cette fonction permet de vider les objets tkinter.Entry
#       des caractère mis précédement.
#
################################################
    """
    # Réinitialisation d'un Entry ou d'un DateEntry
    if str(type(case)) == "<class 'tkinter.Entry'>" or str(type(case)) == "<class 'tkcalendar.dateentry.DateEntry'>":
        case.delete(0, 'end')
    # Réinitialisation de la combobox
    elif str(type(case)) == "<class 'tkinter.ttk.Combobox'>" :
        case.current(0)


def message_erreur(id, erreur = ""):
    """
################ Fonction message_erreur ################
#
#   Prend en argument : id  Un entier
#                       erreur un string ou une liste
#   Retourne : Rien
#   Cette fonction permet d'annoncé par un message une erreur
#       qui change en fonction de l'id et de la variable erreur.
#
#########################################################
    """
    if id == 1: # Message suite de connexion
        messagebox.showinfo(title="Nom ou mot de passe incorecte(s)",message = "Veuillez réessayer !")
    elif id == 2: # Message suite création de compte
        if erreur == "":
            messagebox.showinfo(title="Espace créé", message="Espace créé, bienvenue !")
        elif erreur == 1:
            messagebox.showinfo(title="Erreur", message="Nom déjà utilisé !")
        elif erreur == 2:
            messagebox.showinfo(title="Erreur", message="N'utilisez pas de ';' dans votre nom ou votre mot de passe.")
        elif erreur == 3:
            messagebox.showinfo(title="Erreur", message="Saisie incorrecte. Veuillez recommencer !")
    elif id == 3: # Message erreur suite création objet
        t = "Saisie incorecte. \n"
        if len(erreur) == 1:
            t += "L'erreur est sur : " + erreur[0]
        else:
            t += "Les erreurs sont les suivantes : \n"
            for i in erreur:
                t += "\t- " + i + "\n"
            t += "Veuillez recommencez !"
        messagebox.showinfo(title="Erreur", message=t)
    elif id == 4: # Message réussite suite à création, modif ou suppr
        if erreur == 1:
            messagebox.showinfo(title="Réussite", message="Objet bien créé !")
        elif erreur == 2:
            messagebox.showinfo(title="Réussite", message="Objet bien modifié !")
        elif erreur == 3:
            messagebox.showinfo(title="Réussite", message="Objet bien supprimé !")
    elif id == 5: # Message rappel sauvegarde note_perso.txt
        t = "Noubliez pas : \n\td'écrire vos notes persos dans le fichier, \n\td'enregistrer le fichier txt, \n\tet de continuer la création de l'objet."
        messagebox.showinfo(title="Important !", message=t)
    elif id == 6: # Message d'erreur non ouverture de pdf
        t = "Le livre n'a pas réussi à être ouvert, vérifiez qu'il est bien dans le dossier 'PDF' et qu'il est bien orthographié dans le dossier et dans la cosmotheque !"
        messagebox.showinfo(title="Erreur", message=t)


def mdp(e):
    """
################ Fonction mdp ################
#
#   Prend en argument : E   Un tableau de Entry
#   Retourne : un string
#   Cette fonction permet se connecter à la Cosmotheque
#       en se connectant avec user et mdp. On vérifie l'identitée
#       depuis un fichier txt. Renvoie le user si c'est bon
#       ou "" si la connection n'est pas valide
#
##############################################
    """
    user = e[0].get()
    mdp = e[1].get()
    # Effectue la connexion
    if if_login(user, mdp):
        # Récupère l'ensemble de la cosmotheque de l'utilisateur 
        recup_ligne_csv(user)
        return user
    vider_entre(e)
    message_erreur(1)
    return ""


def verif_nombre(i, condition = 0):
    """
################ Fonction verif_nombre ################
#
#   Prend en argument : i  Une chaine de caractère
#                       condition Un entier
#   Retourne : i (modifié si respect les conditions)
#   Cette fonction permet de retourné un entier ou un flottant
#       depuis une chaine de caractère en fonction du nombre
#       donné dans la variable condition.
#
#######################################################
    """
    if i == "":
        return i
    if condition == 0: # Vérification d'un float
        try:
            i = float(i)
            return i
        except:
            return False
    if condition == 1: # Vérification d'un entier
        try:
            i = int(i)
            return i
        except:
            return False
    if condition == 2: # Vérification d'un entier et nb entre 0 et 5
        try:
            i = int(i)
            if i >= 0 and i <= 5:
                return i
            else:
                return False
        except:
            return False
    if condition == 3: # Vérification d'un entier sup ou égal à 0
        try:
            i = int(i)
            if i >= 0:
                return i
            else:
                return False
        except:
            return False


def index(st, liste):
    """
################ Fonction index ################
#
#   Prend en argument : st  Une chaine de caractère
#                       liste   Une liste de chaine de caractère
#   Retourne : Un entier
#   Cette fonction permet retrouver et de retourner l'index
#       de la chaine de caractère dans la liste. Renvoi 0
#       si la chaine n'est pas présente
#
################################################
    """
    for i in range(len(liste)):
        if st == liste[i]:
            return i
    return 0


def creat(e):
    """
################ Fonction creat ################
#
#   Prend en argument : e   Une liste de 4 objets tkinter.Entry
#   Retourne : Un string
#   Cette fonction permet de créer un utilisateur (si y'en a pas un déjà avec
#       le même user et de se connecter. Ne renvoie rien si la création n'est
#       pas possible, et affiche un message d'erreur.
#
################################################
    """
    # Récupération des atributs
    user = e[0].get()
    mdp = e[1].get()
    cmdp = e[2].get()
    robot = e[3].get()
    a = True
    # Analyse des identifiants
    if ';' in user or ';' in mdp:
        a = False
    if robot and len(user)!=0 and len(mdp)!=0 and cmdp == mdp:
        if if_login(user) and a: # Regard dans le fichier txt si le user est déjà utilisé
            creat_login(user, mdp) # Création d'une ligne dans le txt avec les identifiants
            message_erreur(2) # MessageBox de réussite de création
            return user
        elif a:
            message_erreur(2, 1) # MessageBox erreur User déjà utilisé
        else:
            message_erreur(2, 2) # MessageBox erreur utilisation d'un ;
    else:
        message_erreur(2, 3) # MessageBox erreur mdp = "" ou Confirmation_mdp != mdp
    vider_entre(E)
    return ""


def creer_modif_Film(e, quoi, id=""):
    """
################ Fonction creer_modif_Film ################
#
#   Prend en argument : e   Une liste de 9 objets tkinter.Entry
#                       quoi Un entier (0 pour la modif, 1 pour la créa)
#                       id  Un entier contienant l'id de l'objet à modifier
#   Retourne : Rien
#   Cette fonction permet de créer ou de modifier un objet
#       Film à partir des infos données par l'utilisateur
#       sur l'interface. (Si quoi = 0 --> Modif et si quoi = 1 --> Créa)
#
###########################################################
    """
    id_classe = 1
    # Récupération et analyse des atributs
    erreur = []
    titre = e[0].get()
    if titre == "":
        erreur.append("Titre")
    realisateur = e[1].get()
    annee = verif_nombre(e[2].get(), 1)
    if annee == False:
        erreur.append("Année")
        vider(e[2])
    genre = e[3].get()
    recompense = e[4].get()
    prix = verif_nombre(e[5].get(), 0)
    if prix == False:
        erreur.append("Prix d'achat")
        vider(e[5])
    note = verif_nombre(e[6].get(), 2)
    if note == False:
        erreur.append("Note")
        vider(e[6])
    acteurs = e[7].get().split(';')
    date_der_vu = e[8].get()
    if date_der_vu == "":
        date_der_vu = datetime.date(1900, 1, 1)
    note_perso = recup_note_perso()
      #
    if note_perso == False:
        erreur.append("Note(s) Personnelle(s)")
    if len(erreur) == 0:
        if quoi == 0:
            # Modification à la theque Plante
            modif_theque(id, id_classe, [titre, annee, realisateur, genre, acteurs, recompense, note, prix, date_der_vu, note_perso])
        elif quoi == 1:
            # Ajout à la theque Plante
            vider_entre(e)
            ajout_theque(id_classe, [titre, annee, realisateur, genre, acteurs, recompense, note, prix, date_der_vu, note_perso])
        suppr_note_perso()
    else:
        message_erreur(3, erreur) # MessageBox d'erreur avec la liste des erreurs


def creer_modif_Serie(e, quoi, id=""):
    """
################ Fonction creer_modif_Serie ################
#
#   Prend en argument : e   Une liste de 11 objets tkinter.Entry
#                       quoi Un entier (0 pour la modif, 1 pour la créa)
#                       id  Un entier contienant l'id de l'objet à modifier
#   Retourne : Rien
#   Cette fonction permet de créer ou modifier un objet Série à partir des infos
#       données par l'utilisateur sur l'interface.
#
############################################################
    """
    id_classe = 2
    # Récupération et analyse des atributs
    erreur = []
    titre = e[0].get()
    if titre == "":
        erreur.append("Titre")
    realisateur = e[1].get()
    annee = verif_nombre(e[2].get(), 1)
    if annee == False:
        erreur.append("Année")
        vider(e[2])
    genre = e[3].get()
    recompense = e[4].get()
    note = verif_nombre(e[5].get(), 2)
    if note == False:
        erreur.append("Note")
        vider(e[5])
    acteurs = e[6].get().split(';')
    date_der_vu = e[7].get()
    if date_der_vu == "":
        date_der_vu = datetime.date(1900, 1, 1)
    plateforme = e[8].get()
    dernier_episo = e[9].get()
    note_perso = recup_note_perso()

    if len(erreur) == 0:
        if quoi == 0:
            # Modification à la theque Plante
            modif_theque(id, id_classe, [titre, annee, realisateur, genre, acteurs, recompense, note, plateforme, date_der_vu, dernier_episo, note_perso])
        elif quoi == 1:
            # Ajout à la theque Plante
            vider_entre(e)
            ajout_theque(id_classe, [titre, annee, realisateur, genre, acteurs, recompense, note, plateforme, date_der_vu, dernier_episo, note_perso])
        suppr_note_perso()
    else:
        message_erreur(3, erreur) # MessageBox d'erreur avec la liste des erreurs


def creer_modif_Livre(e, quoi, id=""):
    """
################ Fonction creer_modif_Livre ################
#
#   Prend en argument : e   Une liste de 11 objets tkinter.Entry
#                       quoi Un entier (0 pour la modif, 1 pour la créa)
#                       id  Un entier contienant l'id de l'objet à modifier
#   Retourne : Rien
#   Cette fonction permet de créer ou modifier un objet Livre à partir des infos
#       données par l'utilisateur sur l'interface.
#
############################################################
    """
    id_classe = 3
    # Récupération et analyse des atributs
    erreur = []
    titre = e[0].get()
    if titre == "":
        erreur.append("Titre")
    auteur = e[1].get()
    annee = verif_nombre(e[2].get(), 1)
    if annee == False:
        erreur.append("Année")
        vider(e[2])
    genre = e[3].get()
    recompense = e[4].get()
    prix = verif_nombre(e[5].get(), 0)
    if prix == False:
        erreur.append("Prix d'achat")
        vider(e[5])
    etat = e[6].get()
    note = verif_nombre(e[7].get(), 2)
    if note == False:
        erreur.append("Note")
        vider(e[7])
    narration = e[8].get()
    tome = e[9].get()
    note_perso = recup_note_perso()
    if len(erreur) == 0:
        if quoi == 0:
            # Modification à la theque Plante
            modif_theque(id, id_classe, [titre, annee, auteur, genre, recompense, etat, note, prix, tome, narration, note_perso])
        elif quoi == 1:
            # Ajout à la theque Plante
            vider_entre(e)
            ajout_theque(id_classe, [titre, annee, auteur, genre, recompense, etat, note, prix, tome, narration, note_perso])
        suppr_note_perso()
    else:
        message_erreur(3, erreur) # MessageBox d'erreur avec la liste des erreurs


def creer_modif_Morceau(e, quoi, id=""):
    """
################ Fonction creer_modif_Morceau ################
#
#   Prend en argument : e   Une liste de 7 objets tkinter.Entry
#                       quoi Un entier (0 pour la modif, 1 pour la créa)
#                       id  Un entier contienant l'id de l'objet à modifier
#   Retourne : Rien
#   Cette fonction permet de créer ou modifier un objet Morceau à partir des infos
#       données par l'utilisateur sur l'interface.
#
##############################################################
    """
    id_classe = 4
    # Récupération et analyse des atributs
    erreur = []
    titre = e[0].get()
    if titre == "":
        erreur.append("Titre")
    artiste = e[1].get()
    annee = verif_nombre(e[2].get(), 1)
    if annee == False:
        erreur.append("Année")
        vider(e[2])
    genre = e[3].get()
    recompense = e[4].get()
    prix = verif_nombre(e[5].get(), 0)
    if prix == False:
        erreur.append("Prix d'achat")
        vider(e[5])
    note = verif_nombre(e[6].get(), 2)
    if note == False:
        erreur.append("Note")
        vider(e[6])
    if len(erreur) == 0:
        if quoi == 0:
            # Modification à la theque Plante
            modif_theque(id, id_classe, [titre, annee, artiste, genre, recompense, prix, note])
        elif quoi == 1:
            # Ajout à la theque Plante
            vider_entre(e)
            ajout_theque(id_classe, [titre, annee, artiste, genre, recompense, prix, note])
    else:
        message_erreur(3, erreur) # MessageBox d'erreur avec la liste des erreurs


def creer_modif_Jeu_Video(e, quoi, id=""):
    """
################ Fonction creer_modif_Jeu_Video ################
#
#   Prend en argument : e   Une liste de 11 objets tkinter.Entry
#                       quoi Un entier (0 pour la modif, 1 pour la créa)
#                       id  Un entier contienant l'id de l'objet à modifier
#   Retourne : Rien
#   Cette fonction permet de créer ou modifier un objet Jeu Vidéo à partir des infos
#       données par l'utilisateur sur l'interface.
#
################################################################
    """
    id_classe = 5
    # Récupération et analyse des atributs
    erreur = []
    titre = e[0].get()
    if titre == "":
        erreur.append("Titre")
    studio = e[1].get()
    annee = verif_nombre(e[2].get(), 1)
    if annee == False:
        erreur.append("Année")
        vider(e[2])
    genre = e[3].get()
    recompense = e[4].get()
    prix = verif_nombre(e[5].get(), 0)
    if prix == False:
        erreur.append("Prix d'achat")
        vider(e[5])
    note = verif_nombre(e[6].get(), 2)
    if note == False:
        erreur.append("Note")
        vider(e[6])
    console = e[7].get()
    nombre_heure_jouer = verif_nombre(e[8].get(), 3)
    if nombre_heure_jouer == False:
        erreur.append("Nombre d'heure de jeu")
        vider(e[8])
    nombre_joueur_Max = verif_nombre(e[9].get(), 3)
    if nombre_joueur_Max == False:
        erreur.append("Nombre de joueurs Maximal")
        vider(e[9])
    nombre_joueur_min = verif_nombre(e[10].get(), 3)
    if nombre_joueur_min == False:
        erreur.append("Nombre de joueurs minimal")
        vider(e[10])
    if nombre_joueur_Max != "" and nombre_joueur_min != "" and nombre_joueur_Max != False and nombre_joueur_min != False:
        if nombre_joueur_min > nombre_joueur_Max:
            erreur.append("Nombre de joueurs Maxi/mini")
            vider_entre([e[9], e[10]])
    note_perso = recup_note_perso()
    if len(erreur) == 0:
        if quoi == 0:
            # Modification à la theque Plante
            modif_theque(id, id_classe, [titre, annee, studio, genre, recompense, note, prix, console, nombre_heure_jouer, nombre_joueur_Max, nombre_joueur_min, note_perso])
        elif quoi == 1:
            # Ajout à la theque Plante
            vider_entre(e)
            ajout_theque(id_classe, [titre, annee, studio, genre, recompense, note, prix, console, nombre_heure_jouer, nombre_joueur_Max, nombre_joueur_min, note_perso])
        suppr_note_perso()
    else:
        message_erreur(3, erreur) # MessageBox d'erreur avec la liste des erreurs


def creer_modif_Jeu_Societe(e, quoi, id=""):
    """
################ Fonction creer_modif_Jeu_Societe ################
#
#   Prend en argument : e   Une liste de 11 objets tkinter.Entry
#                       quoi Un entier (0 pour la modif, 1 pour la créa)
#                       id  Un entier contienant l'id de l'objet à modifier
#   Retourne : Rien
#   Cette fonction permet de créer ou de modifier un objet Jeu de Société à partir des infos
#       données par l'utilisateur sur l'interface.
#
##################################################################
    """
    id_classe = 6
    # Récupération et analyse des atributs
    erreur = []
    titre = e[0].get()
    if titre == "":
        erreur.append("Titre")
    marque = e[1].get()
    annee = verif_nombre(e[2].get(), 1)
    if annee == False:
        erreur.append("Année")
        vider(e[2])
    genre = e[3].get()
    recompense = e[4].get()
    prix = verif_nombre(e[5].get(), 0)
    if prix == False:
        erreur.append("Prix d'achat")
        vider(e[5])
    note = verif_nombre(e[6].get(), 2)
    if note == False:
        erreur.append("Note")
        vider(e[6])
    nombre_joueur_Max = verif_nombre(e[7].get(), 3)
    if nombre_joueur_Max == False:
        erreur.append("Nombre de joueurs Maximal")
        vider(e[7])
    nombre_joueur_min = verif_nombre(e[8].get(), 3)
    if nombre_joueur_min == False:
        erreur.append("Nombre de joueurs minimal")
        vider(e[8])
    if nombre_joueur_Max != "" and nombre_joueur_min != "" and nombre_joueur_Max != False and nombre_joueur_min != False:
        if nombre_joueur_min > nombre_joueur_Max:
            erreur.append("Nombre de joueurs Maxi/mini")
            vider_entre([e[7], e[8]])
    support = e[9].get()
    note_perso = recup_note_perso()

    if len(erreur) == 0:
        if quoi == 0:
            # Modification à la theque Plante
            modif_theque(id, id_classe, [titre, annee, marque, genre, recompense, note, prix, support, nombre_joueur_Max, nombre_joueur_min, note_perso])
        elif quoi == 1:
            # Ajout à la theque Plante
            vider_entre(e)
            ajout_theque(id_classe, [titre, annee, marque, genre, recompense, note, prix, support, nombre_joueur_Max, nombre_joueur_min, note_perso])
        suppr_note_perso()
    else:
        message_erreur(3, erreur) # MessageBox d'erreur avec la liste des erreurs


def creer_modif_Plante(e, quoi, id=""):
    """
################ Fonction creer_modif_Plante ################
#
#   Prend en argument : e   Une liste de 11 objets tkinter.Entry
#                       quoi Un entier (0 pour la modif, 1 pour la créa)
#                       id  Un entier contienant l'id de l'objet à modifier
#   Retourne : Rien
#   Cette fonction permet de créer ou de modifier un objet Plante à partir des infos
#       données par l'utilisateur sur l'interface.
#
#############################################################
    """
    id_classe = 7
    # Récupération et analyse des atributs
    erreur = []
    nom = e[0].get()
    if nom == "":
        erreur.append("Nom")
    espece = e[1].get()
    caracteristique = e[2].get()
    luminosite = e[3].get()
    eau = e[4].get()
    pot = e[5].get()
    cache_pot = e[6].get()
    ou_elle_est = e[7].get()
    date = e[8].get()
    if date == "":
        date = datetime.date(1900, 1, 1)
    note = verif_nombre(e[9].get(), 2)
    if note == False:
        erreur.append("Note")
        vider(e[9])
    if len(erreur) == 0:
        if quoi == 0:
            # Modification à la theque Plante
            modif_theque(id, id_classe, [nom, espece, caracteristique, luminosite, eau, pot, cache_pot, ou_elle_est, date, note])
        elif quoi == 1:
            # Ajout à la theque Plante
            vider_entre(e)
            ajout_theque(id_classe, [nom, espece, caracteristique, luminosite, eau, pot, cache_pot, ou_elle_est, date, note])
    else:
        message_erreur(3, erreur) # MessageBox d'erreur avec la liste des erreurs


def ajout_theque(id_classe, arguments):
    """
################ Fonction ajout_theque ################
#
#   Prend en argument : id_classe   Un entier
#                       arguments   Une liste qui contient
#                           l'ensemble des paramêtre de chaque classe
#   Retourne : Rien
#   Cette fonction permet de créer un objet de la classe
#       passé en paramêtre, de l'ajouter à la theque de la
#       bonne classe et de l'ajouter au fichier csv.
#
#######################################################
    """
    global Cosmotheque
    nom_classe = Liste_Categorie[id_classe]
    Cosmotheque.nb_objet += 1
    id = Cosmotheque.nb_objet
    # Création d'un objet en fonction de la classe passé en argument
    if id_classe == 1:
        [titre, annee, realisateur, genre, acteurs, recompense, note, prix, date_der_vu, note_perso] = arguments
        plus = Film(id, titre, annee, realisateur, genre, acteurs, recompense, note, date_der_vu, note_perso, prix)
    elif id_classe == 2:
        [titre, annee, realisateur, genre, acteurs, recompense, note, plateforme, date_der_vu, der_episode_vu, note_perso] = arguments
        plus = Serie(id, titre, annee, realisateur, genre, acteurs, recompense, note, plateforme, date_der_vu, der_episode_vu, note_perso)
    elif id_classe == 3:
        [titre, annee, auteur, recompense, genre, etat, note, prix, tome, narration, note_perso] = arguments
        plus = Livres(id, titre, annee, auteur, genre, recompense, etat, note, prix, tome, narration, note_perso)
    elif id_classe == 4:
        [titre, annee, artiste, genre, recompense, prix, note] = arguments
        plus = Morceau(id, titre, annee, artiste, genre, recompense, prix, note)
    elif id_classe == 5:
        [titre, annee, studio, genre, recompense, note, prix, console, nombre_heure_jouer, nombre_joueur_Max, nombre_joueur_min, note_perso] = arguments
        plus = Jeux_Videos(id, titre, annee, studio, genre, recompense, note, prix, console, nombre_heure_jouer, nombre_joueur_Max, nombre_joueur_min, note_perso)
    elif id_classe == 6:
        [titre, annee, marque, genre, recompense, note, prix, support, nombre_joueur_Max, nombre_joueur_min, note_perso] = arguments
        plus = Jeux_Societe(id, titre, annee, marque, genre, recompense, note, prix, support, nombre_joueur_Max, nombre_joueur_min, note_perso)
    elif id_classe == 7:
        [nom, espece, caracteristique, luminosite, eau, pot, cache_pot, ou_elle_est, date, note] = arguments
        plus = Plantes(id, nom, espece, caracteristique, luminosite, eau, pot, cache_pot, ou_elle_est, date, note)
    # Ajoute l'objet à la bonne classe de la cosmotheque
    Cosmotheque.theque[id_classe].theque.append(plus)
    Cosmotheque.theque[id_classe].nb_objet_collection()
    ajout_csv(id, id_classe, arguments)
    message_erreur(4, 1) # MessageBox de réussite de la création


def modif_theque(id, id_classe, arguments):
    """
################ Fonction modif_theque ################
#
#   Prend en argument : id          Un entier
#                       id_classe   Un entier
#                       arguments   Une liste qui contient
#                               l'ensemble des paramêtre de chaque classe
#   Retourne : Rien
#   Cette fonction permet de modifier un objet de la classe
#       passé en paramêtre, de la modifier à la theque de la
#       bonne classe et dans le fichier csv.
#
#######################################################
    """
    global Cosmotheque
    nom_classe = Liste_Categorie[id_classe]
    theque = Cosmotheque.theque[id_classe].theque
    for i in theque:
        if i.id == id:
            # Modification des paramêtre de l'objet en fonction de la catégorie
            if id_classe == 1:
                [i.titre, i.annee, i.createur, i.recompense, i.acteurs, i.genre, i.note, i.prix, i.dat_visio, i.note_perso] = arguments
            elif id_classe == 2:
                [i.titre, i.annee, i.createur, i.recompense, i.acteurs, i.genre, i.note, i.plateforme, i.dat_visio, i.der_episode_vu, i.note_perso] = arguments
            elif id_classe == 3:
                [i.titre, i.annee, i.createur, i.genre, i.recompense, i.etat, i.note, i.prix, i.tome, i.narration, i.note_perso] = arguments
            elif id_classe == 4:
                [i.titre, i.annee, i.createur, i.genre, i.recompense, i.prix, i.note] = arguments
            elif id_classe == 5:
                [i.titre, i.annee, i.createur, i.genre, i.recompense, i.note, i.prix, i.console, i.nbh, i.nbjM, i.nbjm, i.note_perso] = arguments
            elif id_classe == 6:
                [i.titre, i.annee, i.createur, i.genre, i.recompense, i.note, i.prix, i.support, i.nbjM, i.nbjm, i.note_perso] = arguments
            elif id_classe == 7:
                [i.nom, i.espece, i.caracteristique, i.luminosite, i.eau, i.pot, i.cache_pot, i.ou_elle_est, i.date, i.note] = arguments
    modif_csv(id, id_classe, arguments)
    message_erreur(4, 2) # MessageBox de réussite de modification


def suppr_theque(id, id_classe):
    """
################ Fonction suppr_theque ################
#
#   Prend en argument : id          Un entier
#                       id_classe   Un entier
#   Retourne : Rien
#   Cette fonction permet de supprimé un objet de la classe
#       passé en paramêtre et de la supprimé à la theque de la
#       bonne classe et dans le fichier csv.
#
#######################################################
    """
    global Cosmotheque
    j = 0
    for i in Cosmotheque.theque[id_classe].theque:
        if i.id == id:
            Cosmotheque.theque[id_classe].theque.pop(j)
        j += 1
    Cosmotheque.theque[id_classe].nb_objet_collection()
    suppr_csv(id, Cosmotheque.user)
    message_erreur(4, 3) # MessageBox de réussite de supréssion


def ajout_csv(id, id_classe, arguments):
    """
################ Fonction ajout_csv ################
#
#   Prend en argument : id  Un entier
#                       id_classe Un entier
#                       arguments   Une liste avec
#                           les caractéristique de la classe
#   Retourne : Rien
#   Cette fonction permet d'ajouter au fichier csv l'ensemble
#       des caractéristique de l'ogbet à ajouter.
#
####################################################
    """
    global Cosmotheque
    chemain = Chemain_Data + Nom_CSV
    csv = open(chemain, 'a')
    ligne = str(id) + ";" + Cosmotheque.user + ";" + str(id_classe) + ";"
    for i in arguments:
        if type(i) == "<class 'list'>":
            ajout = ""
            for x in i:
                if ajout != "":
                    ajout += "!"
                ajout += str(x)
        else:
            ajout = str(i).replace("\n", "\\n").replace(";", ".,")
        ligne += ajout + ";"
    ligne += "\n"
    csv.writelines(ligne)
    csv.close()


def modif_csv(id, id_classe, arguments):
    """
################ Fonction modif_csv ################
#
#   Prend en argument : id  Un entier
#                       id_classe Un entier
#                       arguments   Une liste avec
#                                les caractéristique de la classe
#   Retourne : Rien
#   Cette fonction permet de supprimer l'objet puis de le recréer
#       dans le fichier csv en fonction de l'ensemble
#       des caractéristique de l'objet à modifier.
#
####################################################
    """
    global Cosmotheque
    chemain = Chemain_Data + Nom_CSV
    csv_r = open(chemain, 'r')
    lignes = csv_r.readlines()
    csv_r.close()

    ligne_id = str(id) + ";" + Cosmotheque.user + ";" + str(id_classe)
    for i in arguments:
        if str(type(i)) == "<class 'list'>":
            ajout = ""
            for x in i:
                if ajout != "":
                    ajout += "!"
                ajout += str(x)
        else:
            ajout = str(i).replace("\n", "\\n").replace(";", ";,")
        ligne_id += ";" + ajout
    ligne_id += "\n"

    f_o = open(chemain, 'w')
    for i in lignes:
        j = i.split(";")
        if j[0] == str(id) and j[1] == Cosmotheque.user:
            f_o.writelines(ligne_id)
        else:
            f_o.writelines(i)
    f_o.close()


def suppr_csv(id, user):
    """
################ Fonction suppr_csv ################
#
#   Prend en argument : id  Un entier
#                       user   Une chaine de caractère
#   Retourne : Rien
#   Cette fonction permet de supprimer l'objet du
#       fichier csv.
#
####################################################
    """
    chemain = Chemain_Data + Nom_CSV
    csv_r = open(chemain, 'r')
    lignes = csv_r.readlines()
    csv_r.close()

    csv_w = open(chemain, 'w')
    for i in lignes:
        j = i.split(";")
        if j[0] != str(id) and j[1] == user:
            csv_w.writelines(i)
    csv_w.close()



def retour(f, nb, event=""): # En appuyant sur un des boutons "Retour" des différentes fenêtres
    """
################ Fonction retour #####################
#
#   Prend en argument : f   un objet Tkinter
#                       nb  un entier
#                       event
#   Retourne : Rien
#   Cette fonction permet de gérer le changement de fenêtre
#       lors des appuis sur le bouton quitter ou retour.
#   L'argument event recupère l'information de l'évenement quand 
#       la touche Echap est préssée.
#
######################################################
    """
    global Cosmotheque
    if nb == 0:
        f.destroy()
        fen(Tk(), 1) # Retour à la page de connexion
    elif nb == 1: # Destruction de tous
        f.destroy()
    elif nb == 2:
        f.destroy()
        Cosmotheque = Collection(Nom_Projet)
        fen(Tk(), 1) # Revenir à la page de connexion
    elif nb == 3:
        f.destroy()
        fen(Tk(), 2) # Revenir à la page de sélection de l'activité
    elif nb == 4:
        f.destroy()
        fen(Tk(), 3) # Retour à la page de pré-sélection
    elif nb == 5:
        f.destroy()
        fen(Tk(), 3) # Retour à la page de pré-sélection
    elif nb == 6:
        f.destroy()
        fen(Tk(), 2) # Retour à la page de sélection de l'activité


def validation(nb, quant, f, plus = [], event = ""):
    """
################ Fonction validation #################
#
#   Prend en argument : nb  un entier
#                       quant   un entier
#                       f   un objet Tkinter
#                       plus    une liste d'argument
#                       event pris en compte pour les appuis de touche
#   Retourne : Rien
#   Cette fonction permet de gérer le changement de fenêtre
#       lors des appuis sur les boutons de celle ci.
#
######################################################
    """
    global User
    if nb == 0: # Page de création
        # Création d'un nouvelle utilisateur
        User = creat(plus)
        if len(User) != 0:
            f.destroy()
            fen(Tk(), 2) # Page de sélection de l'activité
    elif nb == 1: # Page de connexion
        # Appuis sur le bouton "Connexion"
        if quant == 1:
            User = mdp(plus) # Vérification de la connexion
            if len(User) != 0:
                f.destroy()
                fen(Tk(), 2) # Page de selection de l'activité
        # Appuis sur le bouton de "Création" d'un nouveau profil
        elif quant == 2:
            f.destroy()
            fen(Tk(), 0) # Page de Création d'un nouvelle utilisateur
    elif nb == 2: # Page de sélection de l'activité
        # Appuis sur le bouton de "Modification et Visualisation"
        if quant == 1:
            f.destroy()
            fen(Tk(), 3) # Page de pré-sélection
        # Appuis sur le bouton "Création" d'un nouvelle Objet
        elif quant == 2:
            f.destroy()
            fen(Tk(), 6, [0]) # Page de Création d'un nouvelle objet
    elif nb == 3: # Page de pré-sélection
        # Appui sur le bouton "Recherche dans toute la Cosmotheque"
        if quant == 1:
            retour = Recherche_all()
        # Appuis sur le bouton "Recherche par Catégorie"
        elif quant == 2:
            retour = Recherche_Categorie(plus[1])
        # Appuis sur le bouton "Recherche par Mot-Clés"
        elif quant == 3:
            retour = Recherche_Mot_Cles(plus)
        # Appuis sur le bouton "Recherche par Top10"
        elif quant == 4:
            retour = Top10_Categorie(plus[1])
        if retour != []:
            # retour contient l'ensemble des objets pré-sélection suite à une recherche dans la cosmotheque
            f.destroy()
            fen(Tk(), 4, retour) # Page de sélection d'un objet
    elif nb == 4: # Page de sélection d'un objet
        plus = trouver_selection(plus[0], plus[1])
        f.destroy()
        fen(Tk(), 5, plus) # Page de modification d'un objet
    elif nb == 6 or nb == 5: # Page de modification et de visualisation d'un object
        quant.append("")
        quoi = nb-5
        # Suite à l'appuis au bouton "Modifier"
        # Quand l'objet est un Film
        if quant[0] == 1:
            creer_modif_Film(plus, quoi, quant[1]) # Crée l'objet de la Cosmotheque et du CSV
        # Quand l'objet est une Série
        elif quant[0] == 2:
            creer_modif_Serie(plus, quoi, quant[1]) # Crée l'objet de la Cosmotheque et du CSV
        # Quand l'objet est une Livre
        elif quant[0] == 3:
            creer_modif_Livre(plus, quoi, quant[1]) # Crée l'objet de la Cosmotheque et du CSV
        # Quand l'objet est un Morceau
        elif quant[0] == 4:
            creer_modif_Morceau(plus, quoi, quant[1]) # Crée l'objet de la Cosmotheque et du CSV
        # Quand l'objet est un Jeu Vidéo
        elif quant[0] == 5:
            creer_modif_Jeu_Video(plus, quoi, quant[1]) # Crée l'objet de la Cosmotheque et du CSV
        # Quand l'objet est un Jeu de Société
        elif quant[0] == 6:
            creer_modif_Jeu_Societe(plus, quoi, quant[1]) # Crée l'objet de la Cosmotheque et du CSV
        # Quand l'objet est une Plante
        elif quant[0] == 7:
            creer_modif_Plante(plus, quoi, quant[1]) # Crée l'objet de la Cosmotheque et du CSV
        # Permet de suprimer l'objet sélectionné avec le bouton "Suprimer"
        elif quant[0] == 0:
            suppr_theque(plus[0], plus[1]) # Supprime l'objet de la Cosmotheque et du CSV
            f.destroy()
            fen(Tk(), 3) # Page de pré-selection


def changement(f, liste_Combo, event):
    """
################ Fonction changement #################
#
#   Prend en argument : f   un objet Tkinter
#                       liste_Combo un objet Tkinter.liste_combo
#                       event Evenement de clic sur la liste
#   Retourne : Rien
#   Cette fonction permet de modifier la fenêtre en fonction
#       du menu déroulant.
#
######################################################
    """
    Id = index(liste_Combo.get(), Liste_Categorie)
    f.destroy()
    fen(Tk(), 6, [Id])


def fen(f, nb, Id = []):
    """
################ Fonction fen ########################
#
#   Prend en argument : f   un objet Tkinter
#                       nb  un entier
#                       Id  une liste ou un entier en fonction de nb
#   Retourne : Rien
#   Cette fonction permet d'initialiser l'ensemble
#       des fenêtres de l'application
#       En fonction de l'entier nb
#   Pour nb = 0 : Création d'un nouvelle utilisateur
#        nb = 1 : Page de chargement
#        nb = 2 : Page de selection de l'activité (Modification/Visualisation et Création)
#        nb = 3 : Page de pré-selection des Objets pour la modification
#        nb = 4 : Page de selection des Objets pré-sélectionné
#        nb = 5 : Page de Visuallisation et de modification
#        nb = 6 : Page de Création d'un nouvelle Objet
#
#######################################################
    """
    global User

    # Parametrage de la fenêtre
    f.focus_force() # Passage au premier plan
    f.resizable(False, False) # Impossibilité de modifié les dimentions de la fenêtre

    if nb == 6 and Id == []:
        Id = 0

    # Parametrage des paramêtre commun à chaque fenêtre
    quitter = partial(retour, f, nb) # partial permet d'appeler une fonction avec arguments : partial(nom_fonction, *args)
    t = Nom_Projet + ".exe"
    f.title(t)
    f.bind('<KeyPress-Escape>', quitter)

    if nb == 0: # Page de création d'un nouvelle utilisateur
        # Création des Widgets
        t = "Création d'un nouvelle espace dans la " + Nom_Projet
        text = Label(f, text = t)
        text_user = Label(f, text = "Nom : ")
        entre_user = Entry(f)
        text_mdp = Label(f, text = "Mot de passe : ")
        entre_mdp = Entry(f, show = "*")
        text_cmdp = Label(f, text = "Confirmation du mot de passe : ")
        entre_cmdp = Entry(f, show = "*")
        value_Cb = IntVar()
        Cb_robot = Checkbutton(f, text="Je certifie ne pas être un robot ", variable=value_Cb)
        e = [entre_user, entre_mdp, entre_cmdp, value_Cb]
        valid = partial(validation, nb, nb, f, e)
        bouton_valid = Button(f, text="Création", command=valid)
        bouton_quitter = Button(f, text="Retour", command=quitter)

        # Appuis sur la touche entré pour valider
        f.bind('<KeyPress-Return>', valid)

        # Placement des Widgets
        text.grid(row=0, column=0, columnspan=4, pady=10)
        text_user.grid(row=1, column=0, padx=(20,0))
        entre_user.grid(row=1, column=1, padx=(20,0))
        text_mdp.grid(row=2, column=0, padx=(20,0))
        entre_mdp.grid(row=2, column=1, padx=(20,0))
        text_cmdp.grid(row=3, column=0, padx=(20,0))
        entre_cmdp.grid(row=3, column=1, padx=(20,0))
        Cb_robot.grid(row=4, column=0, columnspan=2)
        bouton_valid.grid(row=5, column=3)
        bouton_quitter.grid(row=6, column=4, padx=(20,0), pady=(20,0))

    elif nb == 1: # Page de connection
        # Création des Widgets
        text = Label (f, text = "Connexion : ")
        text_user = Label(f, text="Nom : ")
        entre_user = Entry(f)
        text_mdp = Label(f, text="Mot de passe : ")
        entre_mdp = Entry(f, show = "*")
        valid = partial(validation, nb, 1, f, [entre_user, entre_mdp])
        bouton_valid = Button(f, text="Valider", command=valid)
        creat = partial(validation, nb, 2, f)
        bouton_creat = Button(f, text="Créer un nouvelle espace", command=creat)
        bouton_quitter = Button(f, text="Quitter", command=quitter)

        # Appuis sur la touche entré pour valider
        f.bind('<KeyPress-Return>', valid)

        # Placement des Widgets
        text.grid(row=0, column=0, columnspan=4, pady=10)
        text_user.grid(row=1, column=0, padx=(20,0))
        entre_user.grid(row=1, column=1, padx=(20,0))
        text_mdp.grid(row=2, column=0, padx=(20,0))
        entre_mdp.grid(row=2, column=1, padx=(20,0))
        bouton_valid.grid(row=3, column=2)
        bouton_creat.grid(row=4, column=0, columnspan=2, padx=(20,0), pady=(20,0))
        bouton_quitter.grid(row=5, column=3, padx=(20,0), pady=(20,0))

    elif nb == 2: # Page de sélection (Création, modification ou visualisation des objets de la Cosmotheque)
        # Création des Widgets
        txt = "Bonjour "+ User
        text1 = Label(f, text=txt)
        text2 = Label(f, text="Que veux tu faire ?")
        valid1 = partial(validation, nb, 1, f)
        bouton1 = Button(f, text="Visualiser ou Modifier", command=valid1)
        valid2 = partial(validation, nb, 2, f)
        bouton2 = Button(f, text="Ajouter", command=valid2)
        bouton_quitter = Button(f, text="Déconnection", command=quitter)

        f.bind('<KeyPress-Left>', valid1) # Flèche de Gauche pour Visualiser ou Modifier
        f.bind('<KeyPress-Right>', valid2) # FLèche de Droite pour Créer

        # Placement des Widgets
        text1.grid(row=0, column=0, columnspan=3, pady=10)
        text2.grid(row=1, column=0, columnspan=2, pady=10)
        bouton1.grid(row=2, column=0, padx=(20,0), pady=5)
        bouton2.grid(row=2, column=1, padx=(20,0), pady=5)
        bouton_quitter.grid(row=3, column=2, padx=(20,0), pady=(20,0))

    elif nb == 3: # Page de pré-sélection des Objets
        # Création des Widgets
        text1 = Label(f, text="Que souhaites tu chercher ?")
        text2 = Label(f, text="Catégorie de la recherche : ")
        listeCombo = ttk.Combobox(f, values=Liste_Categorie)
        text3 = Label(f, text="Mots-clés de la recherche : ")
        entre_mc = Entry(f)
        Entree = [entre_mc, listeCombo]
        valid1 = partial(validation, nb, 1, f, Entree)
        t = "Recherche dans l'ensemble de la " + Nom_Projet
        bouton1 = Button(f, text=t, command=valid1)
        valid2 = partial(validation, nb, 2, f, Entree)
        t = "Recherche par Catégorie"
        bouton2 = Button(f, text=t, command=valid2)
        valid3 = partial(validation, nb, 3, f, Entree)
        t = "Recherche par Mots-Clés"
        bouton3 = Button(f, text=t, command=valid3)
        valid4 = partial(validation, nb, 4, f, Entree)
        t = "Top 10 par Catégorie"
        bouton4 = Button(f, text=t, command=valid4)
        bouton_quitter = Button(f, text='Retour', command=quitter)

        # Initialisation des Widgets (ListeCombo et Entry)
        listeCombo.current(0)
        entre_mc.insert(0, "Mot(s)-clé(s)")

        f.bind('<KeyPress-Left>', valid1) # Flèche de Gauche pour chercher dans l'ensemble
        f.bind('<KeyPress-Down>', valid2) # Flèche du Bas pour chercher par catégorie
        f.bind('<KeyPress-Right>', valid3) # Flèche de Droite pour chercher par mot-clés
        f.bind('<KeyPress-Up>', valid4) # Flèche du Haut pour chercher le Top10 par Catégorie

        # Placement des Widgets
        text1.grid(row=0, column=0, columnspan=3, pady=10)
        text2.grid(row=1, column=0, padx=20, pady=10)
        text3.grid(row=1, column=1, padx=20, pady=10)
        listeCombo.grid(row=2, column=0, padx=5)
        entre_mc.grid(row=2, column=1, padx=5)
        bouton2.grid(row=3, column=0, padx=10, pady=(20,0))
        bouton3.grid(row=3, column=1, padx=10, pady=(20,0))
        bouton4.grid(row=4, column=0, padx=10, pady=(20,0))
        bouton1.grid(row=4, column=1, padx=10, pady=(20,0))
        bouton_quitter.grid(row=5, column=3, padx=(20,0), pady=(20,0))

    elif nb == 4: # Page de sélection des Objets
        # Création et parametrage d'une barre de déroulement
        canvas = Canvas(f)
        scroll = Scrollbar(f, orient='vertical', command=canvas.yview)
        canvas_frame = Frame(canvas)
        canvas.create_window(canvas.winfo_rootx(), canvas.winfo_rooty(), anchor='nw', window=canvas_frame)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion = canvas.bbox("all")))

        # Elaboration du reste de la page
        text = Label(f, text="Sélection de l'objet à voir ou modifier")
        bouton_quitter = Button(f, text='Retour', command=quitter)
        x = 0
        while x < len(Id): # Création et placement des Button pour chaque Object pré-sélectionné
            i = Id[x]
            t = str(i[0]) + " - " + i[1] + " - " + i[2] + " - " + i[3]
            valid = partial(validation, nb, nb, f, [i[0], i[1]])
            Bouton = Button(canvas_frame, text=t, command=valid).grid(row=x, column=0, padx=10, pady=10)
            x += 1

        # Placement des Widgets
        text.grid(row=0, column=0, columnspan=2, pady=10)
        canvas.grid(row=1, column=0)
        scroll.grid(row=1, column=1, sticky="ns")
        bouton_quitter.grid(row=2, column=2, padx=(20,0), pady=(20, 0))

    elif nb == 6 or nb == 5: # Page de modification, visualisation et de création des Objects
        if nb == 6: # Création, parametrage et placement des Widgets spécifique à la création
            t = "Ajouter du contenu à la " + Nom_Projet
            listeCombo = ttk.Combobox(f, values=Liste_Categorie)
            listeCombo.current(Id[0])
            par_changement = partial(changement, f, listeCombo)
            listeCombo.bind("<<ComboboxSelected>>", par_changement)
            nperso = ""

            listeCombo.grid(row=1, column=0, columnspan=3, pady=10)

        elif nb == 5: # Création, parametrage et placement des Widgets spécifique à la modification et visualisation
            t = "Modification du contenu à la " + Nom_Projet
            id = str(Id[1]) + '.'
            t_id1 = Label(f, text="Id : ")
            t_id2 = Label(f, text=id)

            t_id1.grid(row=1, column=0, pady=10)
            t_id2.grid(row=1, column=1, padx=5, pady=10)
            nperso = str(Id[-1])

        # Création des Widgets commun
        ouvrir_note_perso = partial(ouvrir_nperso, nb, nperso)
        text = Label(f, text=t)
        bouton_quitter = Button(f, text="Retour", command=quitter)

        # Placer le Widget commun
        text.grid(row=0, column=0, columnspan=4, pady=10)

# Pour la suite, chaque page et créer en fonction de la catégorie de l'Objet
        if Id[0] == 0: # Uniquement lors de la création d'Objet
            bouton_quitter.grid(row=2, column=3, padx=(20,0), pady=(20,0))

        elif Id[0] == 1: # Catégorie FILM
            # Création des Widgets
            t_titre = Label(f, text='Titre : ')
            e_titre = Entry(f)
            t_crea = Label(f, text='Réalisateur : ')
            e_crea = Entry(f)
            t_annee = Label(f, text="Année : ")
            e_annee = Entry(f)
            t_genre = Label(f, text="Genre : ")
            e_genre = Entry(f)
            t_recomp = Label(f, text="Récompense : ")
            e_recomp = Entry(f)
            t_prix = Label(f, text="Prix d'achat : ")
            e_prix = Entry(f)
            t_note = Label(f, text="Note /5 : ")
            e_note = Entry(f)
            t_acteurs = Label(f, text="Acteurs principaux (séparés d'un ; ) : ")
            e_acteurs = Entry(f)
            t_date = Label(f, text="Date de visionnage : ")
            e_date = DateEntry(f, selectmode="day")
            b_date = Button(f, text="Clear", command=lambda:vider_entre([e_date]))
            b_nperso = Button(f, text="Notes Personnelles", command=ouvrir_note_perso)

            Entre = [e_titre, e_crea, e_annee, e_recomp, e_genre, e_prix, e_note, e_acteurs, e_date]

            if nb == 5:
                # Insersion pour la visualisation
                e_titre.insert(0, str(Id[2]))
                e_crea.insert(0, str(Id[4]))
                e_annee.insert(0, str(Id[3]))
                e_genre.insert(0, str(Id[5]))
                e_recomp.insert(0, str(Id[7]))
                e_prix.insert(0, str(Id[9]))
                e_note.insert(0, str(Id[8]))
                e_acteurs.insert(0, str(Id[6]))
                e_date.set_date(Id[10])
                # Parametrage lors de la visualisation et modification
                t_bouton = "Modifier"
                t_boutonfplus = "Supprimer"
                f_plus = partial(validation, nb, [0], [Id[1], Id[0]])
            elif nb == 6:
                # Parametrage lors de la création
                t_bouton = "Ajouter"
                t_boutonfplus = "Réinitialiser"
                f_plus = partial(vider_entre, Entre)

            valid = partial(validation, nb, Id, f, Entre)
            boutonfplus = Button(f, text=t_boutonfplus, command=f_plus)
            bouton = Button(f, text=t_bouton, command=valid)

            f.bind('<KeyPress-Return>', valid) # Touche Entrée pour valider la création ou le modification

            # Placement des Widgets
            t_titre.grid(row=2, column=0, pady=10)
            e_titre.grid(row=2, column=1, padx=5, pady=10)
            t_crea.grid(row=3, column=0, pady=10)
            e_crea.grid(row=3, column=1, padx=5, pady=10)
            t_annee.grid(row=4, column=0, pady=10)
            e_annee.grid(row=4, column=1, padx=5, pady=10)
            t_genre.grid(row=5, column=0, pady=10)
            e_genre.grid(row=5, column=1, padx=5, pady=10)
            t_recomp.grid(row=6, column=0, pady=10)
            e_recomp.grid(row=6, column=1, padx=5, pady=10)
            t_prix.grid(row=7, column=0, pady=10)
            e_prix.grid(row=7, column=1, padx=5, pady=10)
            t_note.grid(row=8, column=0, pady=10)
            e_note.grid(row=8, column=1, padx=5, pady=10)
            t_acteurs.grid(row=9, column=0, pady=10)
            e_acteurs.grid(row=9, column=1, padx=5, pady=10)
            t_date.grid(row=10, column=0, pady=10)
            e_date.grid(row=10, column=1, padx=5, pady=10)
            b_date.grid(row=10, column=2)
            b_nperso.grid(row=11, column=1, padx=5, pady=10)

            boutonfplus.grid(row=12, column=0, padx=10, pady=10)
            bouton.grid(row=12, column=3, padx=10, pady=10)
            bouton_quitter.grid(row=13, column=4, padx=(20,0), pady=(20,0))

        elif Id[0] == 2: # Catégorie SERIE
            # Création des Widgets commun
            t_titre = Label(f, text='Titre : ')
            e_titre = Entry(f)
            t_crea = Label(f, text='Réalisateur : ')
            e_crea = Entry(f)
            t_annee = Label(f, text="Année : ")
            e_annee = Entry(f)
            t_genre = Label(f, text="Genre : ")
            e_genre = Entry(f)
            t_recomp = Label(f, text="Récompense : ")
            e_recomp = Entry(f)
            t_note = Label(f, text="Note /5 : ")
            e_note = Entry(f)
            t_acteurs = Label(f, text="Acteurs principaux : ")
            e_acteurs = Entry(f)
            t_date = Label(f, text="Date de visionnage : ")
            e_date = DateEntry(f, selectmode="day")
            b_date = Button(f, text="Clear", command=lambda:vider_entre([e_date]))
            t_plat = Label(f, text="Plateforme : ")
            e_plat = Entry(f)
            t_der_e = Label(f, text="Dernier épisode vu :")
            e_der_e = Entry(f)
            b_nperso = Button(f, text="Notes Personnelles", command=ouvrir_note_perso)

            Entre = [e_titre, e_crea, e_annee, e_genre, e_recomp, e_note, e_acteurs, e_date, e_plat, e_der_e]
            if nb == 5:
                # Insertion pour la visualisation
                e_titre.insert(0, str(Id[2]))
                e_crea.insert(0, str(Id[4]))
                e_annee.insert(0, str(Id[3]))
                e_genre.insert(0, str(Id[7]))
                e_recomp.insert(0, str(Id[5]))
                e_note.insert(0, str(Id[8]))
                e_acteurs.insert(0, str(Id[6]))
                e_date.set_date(Id[10])
                e_plat.insert(0, str(Id[9]))
                e_der_e.insert(0, str(Id[11]))
                # Parametrage lors de la visualisation
                t_bouton = "Modifier"
                t_boutonfplus = "Supprimer"
                f_plus = partial(validation, nb, [0], [Id[1], Id[0]])
            elif nb == 6:
                # Parametrage lors de la création
                t_bouton = "Ajouter"
                t_boutonfplus = "Réinitialiser"
                f_plus = partial(vider_entre, Entre)

            valid = partial(validation, nb, Id, f, Entre)
            boutonfplus = Button(f, text=t_boutonfplus, command=f_plus)
            bouton = Button(f, text=t_bouton, command=valid)
            f.bind('<KeyPress-Return>', valid) # Touche Entrée pour valider

            # Placement des Widgets
            t_titre.grid(row=2, column=0, pady=10)
            e_titre.grid(row=2, column=1, padx=5, pady=10)
            t_crea.grid(row=3, column=0, pady=10)
            e_crea.grid(row=3, column=1, padx=5, pady=10)
            t_annee.grid(row=4, column=0, pady=10)
            e_annee.grid(row=4, column=1, padx=5, pady=10)
            t_genre.grid(row=5, column=0, pady=10)
            e_genre.grid(row=5, column=1, padx=5, pady=10)
            t_recomp.grid(row=6, column=0, pady=10)
            e_recomp.grid(row=6, column=1, padx=5, pady=10)
            t_note.grid(row=7, column=0, pady=10)
            e_note.grid(row=7, column=1, padx=5, pady=10)
            t_acteurs.grid(row=8, column=0, pady=10)
            e_acteurs.grid(row=8, column=1, padx=5, pady=10)
            t_date.grid(row=9, column=0, pady=10)
            e_date.grid(row=9, column=1, padx=5, pady=10)
            b_date.grid(row=9, column=2)
            t_plat.grid(row=10, column=0, pady=10)
            e_plat.grid(row=10, column=1, padx=5, pady=10)
            t_der_e.grid(row=11, column=0, pady=10)
            e_der_e.grid(row=11, column=1, padx=5, pady=10)
            b_nperso.grid(row=12, column=1, padx=5, pady=10)

            boutonfplus.grid(row=13, column=0, padx=10, pady=10)
            bouton.grid(row=13, column=3, padx=10, pady=10)
            bouton_quitter.grid(row=14, column=4, padx=(20,0), pady=(20,0))

        elif Id[0] == 3: # Catégorie LIVRE
            # Placement des WIdgtes
            t_titre = Label(f, text='Titre : ')
            e_titre = Entry(f)
            t_crea = Label(f, text='Auteur : ')
            e_crea = Entry(f)
            t_annee = Label(f, text="Année : ")
            e_annee = Entry(f)
            t_genre = Label(f, text="Genre : ")
            e_genre = Entry(f)
            t_recomp = Label(f, text="Récompense : ")
            e_recomp = Entry(f)
            t_prix = Label(f, text="Prix d'achat : ")
            e_prix = Entry(f)
            t_note = Label(f, text="Note /5 : ")
            e_note = Entry(f)
            t_etat = Label(f, text="Etat : ")
            e_etat = ttk.Combobox(f, values=Liste_Etat)
            t_narration = Label(f, text="Type de naration : ")
            e_narration = ttk.Combobox(f, values=Liste_Narration)
            t_tome = Label(f, text="N° de tome : ")
            e_tome = Entry(f)
            b_nperso = Button(f, text="Notes Personnelles", command=ouvrir_note_perso)

            Entre = [e_titre, e_crea, e_annee, e_genre, e_recomp, e_prix, e_etat, e_note, e_narration, e_tome]
            if nb == 6:
                # Initialisation et parametrage de la création
                e_etat.current(0)
                e_narration.current(0)
                t_bouton = "Ajouter"
                t_boutonfplus = "Réinitialiser"
                f_plus = partial(vider_entre, Entre)
            elif nb == 5:
                # Initialisation de la modification
                e_titre.insert(0, str(Id[2]))
                e_crea.insert(0, str(Id[4]))
                e_annee.insert(0, str(Id[3]))
                e_genre.insert(0, str(Id[5]))
                e_recomp.insert(0, str(Id[6]))
                e_prix.insert(0, str(Id[9]))
                e_note.insert(0, str(Id[8]))
                e_etat.current(index(Id[7], Liste_Etat))
                e_narration.current(index(Id[11], Liste_Narration))
                e_tome.insert(0, str(Id[10]))
                # Parametrage de la modification
                t_bouton = "Modifier"
                t_boutonfplus = "Supprimer"
                f_plus = partial(validation, nb, [0], [Id[1], Id[0]])
                pdf = partial(ouvrir_pdf, str(Id[2]), str(Id [10]))
                boutonpdf = Button(f, text="Ouvrir le livre", command=pdf)
                boutonpdf.grid(row=13, column=1, padx=10, pady=10)

            valid = partial(validation, nb, Id, f, Entre)
            boutonfplus = Button(f, text=t_boutonfplus, command=f_plus)
            bouton = Button(f, text=t_bouton, command=valid)
            f.bind('<KeyPress-Return>', valid) # Touche Entrée pour valider

            # Placement des Widgets
            t_titre.grid(row=2, column=0, pady=10)
            e_titre.grid(row=2, column=1, padx=5, pady=10)
            t_crea.grid(row=3, column=0, pady=10)
            e_crea.grid(row=3, column=1, padx=5, pady=10)
            t_annee.grid(row=4, column=0, pady=10)
            e_annee.grid(row=4, column=1, padx=5, pady=10)
            t_genre.grid(row=5, column=0, pady=10)
            e_genre.grid(row=5, column=1, padx=5, pady=10)
            t_recomp.grid(row=6, column=0, pady=10)
            e_recomp.grid(row=6, column=1, padx=5, pady=10)
            t_prix.grid(row=7, column=0, pady=10)
            e_prix.grid(row=7, column=1, padx=5, pady=10)
            t_note.grid(row=8, column=0, pady=10)
            e_note.grid(row=8, column=1, padx=5, pady=10)
            t_etat.grid(row=9, column=0, pady=10)
            e_etat.grid(row=9, column=1, padx=5, pady=10)
            t_narration.grid(row=10, column=0, pady=10)
            e_narration.grid(row=10, column=1, padx=5, pady=10)
            t_tome.grid(row=11, column=0, pady=10)
            e_tome.grid(row=11, column=1, padx=5, pady=10)
            b_nperso.grid(row=12, column=1, padx=5, pady=10)

            boutonfplus.grid(row=13, column=0, padx=10, pady=10)
            bouton.grid(row=13, column=2, padx=10, pady=10)
            bouton_quitter.grid(row=14, column=3, padx=(20,0), pady=(20,0))

        elif Id[0] == 4: # Catégorie MUSIQUE
            # Création des Widgets
            t_titre = Label(f, text='Titre : ')
            e_titre = Entry(f)
            t_crea = Label(f, text='Artiste : ')
            e_crea = Entry(f)
            t_annee = Label(f, text="Année : ")
            e_annee = Entry(f)
            t_genre = Label(f, text="Genre : ")
            e_genre = Entry(f)
            t_recomp = Label(f, text="Récompense : ")
            e_recomp = Entry(f)
            t_prix = Label(f, text="Prix d'achat : ")
            e_prix = Entry(f)
            t_note = Label(f, text="Note /5 : ")
            e_note = Entry(f)

            Entre = [e_titre, e_crea, e_annee, e_genre, e_recomp, e_prix, e_note]
            if nb == 5:
                # Initialisation pour la modification
                e_titre.insert(0, str(Id[2]))
                e_crea.insert(0, str(Id[4]))
                e_annee.insert(0, str(Id[3]))
                e_genre.insert(0, str(Id[5]))
                e_recomp.insert(0, str(Id[6]))
                e_prix.insert(0, str(Id[7]))
                e_note.insert(0, str(Id[8]))
                # Parametrage pour la modification
                t_bouton = "Modifier"
                t_boutonfplus = "Supprimer"
                f_plus = partial(validation, nb, [0], [Id[1], Id[0]])
            elif nb == 6:
                # Parametrage pour la création
                t_bouton = "Ajouter"
                t_boutonfplus = "Réinitialiser"
                f_plus = partial(vider_entre, Entre)

            valid = partial(validation, nb, Id, f, Entre)
            boutonfplus = Button(f, text=t_boutonfplus, command=f_plus)
            bouton = Button(f, text=t_bouton, command=valid)
            f.bind('<KeyPress-Return>', valid) # Touche Entrée pour valider

            # Placement des Widgets
            t_titre.grid(row=2, column=0, pady=10)
            e_titre.grid(row=2, column=1, padx=5, pady=10)
            t_crea.grid(row=3, column=0, pady=10)
            e_crea.grid(row=3, column=1, padx=5, pady=10)
            t_annee.grid(row=4, column=0, pady=10)
            e_annee.grid(row=4, column=1, padx=5, pady=10)
            t_genre.grid(row=5, column=0, pady=10)
            e_genre.grid(row=5, column=1, padx=5, pady=10)
            t_recomp.grid(row=6, column=0, pady=10)
            e_recomp.grid(row=6, column=1, padx=5, pady=10)
            t_prix.grid(row=7, column=0, pady=10)
            e_prix.grid(row=7, column=1, padx=5, pady=10)
            t_note.grid(row=8, column=0, pady=10)
            e_note.grid(row=8, column=1, padx=5, pady=10)

            boutonfplus.grid(row=9, column=0, padx=10, pady=10)
            bouton.grid(row=9, column=2, padx=10, pady=10)
            bouton_quitter.grid(row=10, column=3, padx=(20,0), pady=(20,0))

        elif Id[0] == 5: # Catégorie JEUX VIDEO
            # Création des Widgets
            t_titre = Label(f, text='Titre : ')
            e_titre = Entry(f)
            t_crea = Label(f, text='Studio : ')
            e_crea = Entry(f)
            t_annee = Label(f, text="Année : ")
            e_annee = Entry(f)
            t_genre = Label(f, text="Genre : ")
            e_genre = Entry(f)
            t_recomp = Label(f, text="Récompense : ")
            e_recomp = Entry(f)
            t_prix = Label(f, text="Prix d'achat : ")
            e_prix = Entry(f)
            t_note = Label(f, text="Note /5 : ")
            e_note = Entry(f)
            t_console = Label(f, text="Console : ")
            e_console = Entry(f)
            t_nbh = Label(f, text="Nb d'heure de jeu : ")
            e_nbh = Entry(f)
            t_nbjM = Label(f, text="Nb de joueurs Max : ")
            e_nbjM = Entry(f)
            t_nbjm = Label(f, text="Nb de joueurs min : ")
            e_nbjm = Entry(f)
            b_nperso = Button(f, text="Notes Personnelles", command=ouvrir_note_perso)

            Entre = [e_titre, e_crea, e_annee, e_genre, e_recomp, e_prix, e_note, e_console, e_nbh, e_nbjM, e_nbjm]
            if nb == 5:
                # Initialisation pour la modification
                e_titre.insert(0, str(Id[2]))
                e_crea.insert(0, str(Id[4]))
                e_annee.insert(0, str(Id[3]))
                e_genre.insert(0, str(Id[5]))
                e_recomp.insert(0, str(Id[6]))
                e_prix.insert(0, str(Id[8]))
                e_note.insert(0, str(Id[7]))
                e_console.insert(0, str(Id[9]))
                e_nbh.insert(0, str(Id[10]))
                e_nbjM.insert(0, str(Id[11]))
                e_nbjm.insert(0, str(Id[12]))
                # Parametrage pour la modification
                t_bouton = "Modifier"
                t_boutonfplus = "Supprimer"
                f_plus = partial(validation, nb, [0], [Id[1], Id[0]])
            elif nb == 6:
                # Parametrage pour la modification
                t_bouton = "Ajouter"
                t_boutonfplus = "Réinitialiser"
                f_plus = partial(vider_entre, Entre)

            valid = partial(validation, nb, Id, f, Entre)
            boutonfplus = Button(f, text=t_boutonfplus, command=f_plus)
            bouton = Button(f, text=t_bouton, command=valid)
            f.bind('<KeyPress-Return>', valid) # Touche Entrée pour valider

            # Placement des Widgets
            t_titre.grid(row=2, column=0, pady=10)
            e_titre.grid(row=2, column=1, padx=5, pady=10)
            t_crea.grid(row=3, column=0, pady=10)
            e_crea.grid(row=3, column=1, padx=5, pady=10)
            t_annee.grid(row=4, column=0, pady=10)
            e_annee.grid(row=4, column=1, padx=5, pady=10)
            t_genre.grid(row=5, column=0, pady=10)
            e_genre.grid(row=5, column=1, padx=5, pady=10)
            t_recomp.grid(row=6, column=0, pady=10)
            e_recomp.grid(row=6, column=1, padx=5, pady=10)
            t_prix.grid(row=7, column=0, pady=10)
            e_prix.grid(row=7, column=1, padx=5, pady=10)
            t_note.grid(row=8, column=0, pady=10)
            e_note.grid(row=8, column=1, padx=5, pady=10)
            t_console.grid(row=9, column=0, pady=10)
            e_console.grid(row=9, column=1, padx=5, pady=10)
            t_nbh.grid(row=10, column=0, pady=10)
            e_nbh.grid(row=10, column=1, padx=5, pady=10)
            t_nbjM.grid(row=11, column=0, pady=10)
            e_nbjM.grid(row=11, column=1, padx=5, pady=10)
            t_nbjm.grid(row=12, column=0, pady=10)
            e_nbjm.grid(row=12, column=1, padx=5, pady=10)
            b_nperso.grid(row=13, column=1, padx=5, pady=10)

            boutonfplus.grid(row=14, column=0, padx=10, pady=10)
            bouton.grid(row=14, column=2, padx=10, pady=10)
            bouton_quitter.grid(row=15, column=3, padx=(20,0), pady=(20,0))

        elif Id[0] == 6: # Catégorie JEUX DE SOCIETE
            # Placement des Widgets
            t_titre = Label(f, text='Titre : ')
            e_titre = Entry(f)
            t_crea = Label(f, text='Marque : ')
            e_crea = Entry(f)
            t_annee = Label(f, text="Année : ")
            e_annee = Entry(f)
            t_genre = Label(f, text="Genre : ")
            e_genre = Entry(f)
            t_recomp = Label(f, text="Récompense : ")
            e_recomp = Entry(f)
            t_prix = Label(f, text="Prix d'achat : ")
            e_prix = Entry(f)
            t_note = Label(f, text="Note /5 : ")
            e_note = Entry(f)
            t_nbmin = Label(f, text="Nb de participant Min : ")
            e_nbmin = Entry(f)
            t_nbmax = Label(f, text="Nb de participant Max : ")
            e_nbmax = Entry(f)
            t_support = Label(f, text="Support du jeu : ")
            e_support = Entry(f)
            b_nperso = Button(f, text="Notes Personnelles", command=ouvrir_note_perso)

            Entre = [e_titre, e_crea, e_annee, e_genre, e_recomp, e_prix, e_note, e_nbmax, e_nbmin, e_support]
            if nb == 5:
                # Initialisation pour  la modification
                e_titre.insert(0, str(Id[2]))
                e_crea.insert(0, str(Id[4]))
                e_annee.insert(0, str(Id[3]))
                e_genre.insert(0, str(Id[5]))
                e_recomp.insert(0, str(Id[6]))
                e_prix.insert(0, str(Id[8]))
                e_note.insert(0, str(Id[7]))
                e_nbmin.insert(0, str(Id[10]))
                e_nbmax.insert(0, str(Id[11]))
                e_support.insert(0, str(Id[9]))
                # Parametrage pour la modification
                t_bouton = "Modifier"
                t_boutonfplus = "Supprimer"
                f_plus = partial(validation, nb, [0], [Id[1], Id[0]])
            elif nb == 6:
                # Parametrage pour la création
                t_bouton = "Ajouter"
                t_boutonfplus = "Réinitialiser"
                f_plus = partial(vider_entre, Entre)

            valid = partial(validation, nb, Id, f, Entre)
            boutonfplus = Button(f, text=t_boutonfplus, command=f_plus)
            bouton = Button(f, text=t_bouton, command=valid)
            f.bind('<KeyPress-Return>', valid) # Touche Entrée pour valiider

            # Placement des Widgets
            t_titre.grid(row=2, column=0, pady=10)
            e_titre.grid(row=2, column=1, padx=5, pady=10)
            t_crea.grid(row=3, column=0, pady=10)
            e_crea.grid(row=3, column=1, padx=5, pady=10)
            t_annee.grid(row=4, column=0, pady=10)
            e_annee.grid(row=4, column=1, padx=5, pady=10)
            t_genre.grid(row=5, column=0, pady=10)
            e_genre.grid(row=5, column=1, padx=5, pady=10)
            t_recomp.grid(row=6, column=0, pady=10)
            e_recomp.grid(row=6, column=1, padx=5, pady=10)
            t_prix.grid(row=7, column=0, pady=10)
            e_prix.grid(row=7, column=1, padx=5, pady=10)
            t_note.grid(row=8, column=0, pady=10)
            e_note.grid(row=8, column=1, padx=5, pady=10)
            t_nbmin.grid(row=9, column=0, pady=10)
            e_nbmin.grid(row=9, column=1, padx=5, pady=10)
            t_nbmax.grid(row=10, column=0, pady=10)
            e_nbmax.grid(row=10, column=1, padx=5, pady=10)
            t_support.grid(row=11, column=0, pady=10)
            e_support.grid(row=11, column=1, padx=5, pady=10)
            b_nperso.grid(row=12, column=1, padx=5, pady=10)

            boutonfplus.grid(row=13, column=0, padx=10, pady=10)
            bouton.grid(row=13, column=2, padx=10, pady=10)
            bouton_quitter.grid(row=14, column=3, padx=(20,0), pady=(20,0))

        elif Id[0] == 7: # Catégorie PLANTE
            # Création des Widgets
            t_nom = Label(f, text='Nom : ')
            e_nom = Entry(f)
            t_espece = Label(f, text='Espèce : ')
            e_espece = Entry(f)
            t_carac = Label(f, text="Caractéristique : ")
            e_carac = Entry(f)
            t_lum = Label(f, text="Luminosité : ")
            e_lum = Entry(f)
            t_eau = Label(f, text="Besoin en eau : ")
            e_eau = Entry(f)
            t_pot = Label(f, text="Pot : ")
            e_pot = Entry(f)
            t_c_pot = Label(f, text="Cache pot : ")
            e_c_pot = Entry(f)
            t_ou_est = Label(f, text="Ou est elle : ")
            e_ou_est = Entry(f)
            t_date = Label(f, text="Date d'achat : ")
            e_date = DateEntry(f, selectmode="day")
            b_date = Button(f, text="Clear", command=lambda:vider_entre([e_date]))
            t_note = Label(f, text="Note /5 : ")
            e_note = Entry(f)

            Entre = [e_nom, e_espece, e_carac, e_lum, e_eau, e_pot, e_c_pot, e_ou_est, e_date, e_note]
            if nb == 5:
                # Initialisation pour la modification
                e_nom.insert(0, str(Id[2]))
                e_espece.insert(0, str(Id[3]))
                e_carac.insert(0, str(Id[4]))
                e_lum.insert(0, str(Id[5]))
                e_eau.insert(0, str(Id[6]))
                e_pot.insert(0, str(Id[7]))
                e_c_pot.insert(0, str(Id[8]))
                e_ou_est.insert(0, str(Id[9]))
                e_date.set_date(Id[10])
                e_note.insert(0, str(Id[11]))
                # Parametrage pour la modification
                t_bouton = "Modifier"
                t_boutonfplus = "Supprimer"
                f_plus = partial(validation, nb, [0], [Id[1], Id[0]])
            elif nb == 6:
                # Parametrage pour la création
                t_bouton = "Ajouter"
                t_boutonfplus = "Réinitialiser"
                f_plus = partial(vider_entre, Entre)

            valid = partial(validation, nb, Id, f, Entre)
            boutonfplus = Button(f, text=t_boutonfplus, command=f_plus)
            bouton = Button(f, text=t_bouton, command=valid)
            f.bind('<KeyPress-Return>', valid) # Touche Entrée pour valider

            # Placement des Widgets
            t_nom.grid(row=2, column=0, pady=10)
            e_nom.grid(row=2, column=1, padx=5, pady=10)
            t_espece.grid(row=3, column=0, pady=10)
            e_espece.grid(row=3, column=1, padx=5, pady=10)
            t_carac.grid(row=4, column=0, pady=10)
            e_carac.grid(row=4, column=1, padx=5, pady=10)
            t_lum.grid(row=5, column=0, pady=10)
            e_lum.grid(row=5, column=1, padx=5, pady=10)
            t_eau.grid(row=6, column=0, pady=10)
            e_eau.grid(row=6, column=1, padx=5, pady=10)
            t_pot.grid(row=7, column=0, pady=10)
            e_pot.grid(row=7, column=1, padx=5, pady=10)
            t_c_pot.grid(row=8, column=0, pady=10)
            e_c_pot.grid(row=8, column=1, padx=5, pady=10)
            t_ou_est.grid(row=9, column=0, pady=10)
            e_ou_est.grid(row=9, column=1, padx=5, pady=10)
            t_date.grid(row=10, column=0, pady=10)
            e_date.grid(row=10, column=1, padx=5, pady=10)
            b_date.grid(row=10, column=2)
            t_note.grid(row=11, column=0, pady=10)
            e_note.grid(row=11, column=1, padx=5, pady=10)

            boutonfplus.grid(row=12, column=0, padx=10, pady=10)
            bouton.grid(row=12, column=2, padx=10, pady=10)
            bouton_quitter.grid(row=13, column=3, padx=(20,0), pady=(20,0))



############################################################
################### Programme Principale ###################
############################################################

# Création de la Cosmotheque
Cosmotheque = Collection(Nom_Projet)
for i in Liste_Categorie:
    Cosmotheque._ajouter_theque(Classe(i))
win = Tk() # Création de la fenêtre
fen(win,1) # Initialisation de la fenêtre à la page de connexion
mainloop()
