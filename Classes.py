#   -*- coding:Utf8 -*-
########################################
#   Programme python
#   Nom : Classes.py
#   Auteur :    LE GUEN Antonin
#               LE MERCIER Aurore
#               ROCHE Corentin
#   Version : 3
#   Date : 23/11/2022
#########################################
#########################################
#
#   Programme qui correspond à l'ensemble des
#   classes pour le programme principale Cosmotheque.py
#
#########################################
#########################################
#
# Listes des classes dans ce programme :
#       Collection (Nom_Projet, Theque = [], user = "")
#           Theque contient des objets Classes
#       Classe (Nom_classe, Theque = [])
#           Theque contient des objets (Film, Serie, Livres, ...)
#       Mere (id, titre, annee, createur, recompense = "", genre = "", note = 0, prix = 0)
#       Film (id, titre, annee, realisateur, genre = "", acteurs_principaux = [], recompense = "", note = 0, date_visio = "", note_perso = "", prix = "")
#       Serie (id, titre, annee, realisateur, genre = "", acteurs_principaux = [], recompense = "", note = 0, plateforme = "", date_visio = "", dev = "", note_perso = "")
#       Livres (id, titre, annee, auteur, genre = "", recompense = "", etat = "", note = 0, prix = 0, tome = 0, narration = "", note_perso = "")
#       Morceau (id, titre, annee, artiste, genre = "", recompense = "", prix = 0, note = 0)
#       Jeux_Video (id, titre, annee, studio, genre = "", recompense = "", note = 0, prix = 0, console = "", nbh = 0, nbjM = 1, nbjm = 1, note_perso = '')
#       Jeux_Societe (self, id, titre, annee, marque, genre = "", recompense = "", note = 0, prix = 0, support = "", nbjM = 1, nbjm = 1, note_perso = '')
#       Plantes (id, nom, espece, caract = "", luminosite = "", eau = "", pot = "", cache_pot = "", ou_elle_est = "", date = "", note = 0)
#
#########################################

###########################################################
######################### Classes #########################
###########################################################


############### Classe Collection ################
#
#   Prend en argument : Nom_Projet, theque = [], user = ""
#   
#   Cette classe correspond à l'ensemble de la Cosmotheque
#       il permet de stocker l'ensemble des classes.
#
###################################################

class Collection:
    def __init__(self, Nom_Projet, theque = [], user = ""):
        self.nom = Nom_Projet
        self.theque = theque
        self.nb_theque = len(self.theque)
        if theque == []:
            self.nb_objet = 0
        else:
            self.nb_objet_collection()
        self.user = user


    def __str__(self):
        self.nb_theque = len(self.theque)
        t = """
################ """ + self.nom
        if self.user !="":
            t = t + " pour " + self.user
        t = t + """ ################
*
*   Il y a dans la """ + self.nom + " , " + str(self.nb_theque) + """ collections :
*
*"""
        for i in self.theque:
            t = t + i.__str__()
        t = t + """
*
############################################################
"""
        return t

    def _ajouter_theque(self, collection):
        self.theque.append(collection)
        self.nb_theque = len(self.theque)

    def nb_objet_collection(self):
        x = 0
        for i in self.theque:
            i.nb_objet_collection()
            x += i.nombre
        self.nb_objet = x


############### Classe Classe ################
#
#   Prend en argument : classe, theque = []
#   
#   Cette classe correspond à l'ensemble d'une classe
#       de la Cosmotheque il permet de stocker 
#       l'ensemble des objets d'une classe.
#
###############################################

class Classe:
    def __init__(self, classe, theque = []):
        self.theque = []
        self.nombre = len(self.theque)
        self.classe = classe

    def __str__(self):
        t = """
######## La collection """ + self.classe + """ ########
*
*      Il y a """ + str(self.nombre) + """ objet dans la collection
*
###############
*
*   """
        for i in self.theque:
            t = t + i.__str__() + """
###############
*"""
        t = t + """
*
##############################"""
        return t

    def nb_objet_collection(self):
        self.nombre = len(self.theque)


############### Autres Classes ################
#
#   Les différentes classes qui suivent sont basé sur 
#       la classe Mere. Les classes stockent les infos 
#       sur un objet de la cosmotheque (Film, Serie, Livre, ...)
#
###############################################

class Mere():
    def __init__(self, id, titre, annee, createur, recompense = "", genre = "", note = 0, prix = 0):
        self.id = id
        self.titre = titre
        self.annee = annee
        self.recompense = recompense
        self.genre = genre
        self.note = note
        self.prix = prix
        self.createur = createur

    def __str__(self):
        t = """
*       Titre : """ + self.titre
        if self.annee != "":
            t = t + """
*       Année de sortie : """ + str(self.annee)
        if self.note != "":
            t = t + """
*       Note : """ + str(self.note) + "/5"
        if self.genre != "":
            t = t + """
*       Genre : """ + self.genre
        if self.recompense != "":
            t = t + """
*       Récompense : """ + self.recompense
        if self.prix != 0 and self.prix != "":
            t = t + """
*       Prix : """ + str(self.prix) + " EUR"
        return t


class Film(Mere):
    def __init__(self, id, titre, annee, realisateur, genre = "", acteurs_principaux = [], recompense = "", note = 0, date_visio = "", note_perso = "", prix = ""):
        super().__init__(id, titre, annee, realisateur, genre, recompense, note, prix)
        self.dat_visio = date_visio
        self.acteurs = acteurs_principaux
        self.note_perso = note_perso

    def __str__(self):
        t = """
*       Réalisateur : """ + self.createur + super().__str__()
        if self.dat_visio != datetime.date(1900, 1, 1) and self.dat_visio != "":
            t = t + """
*       Date de dernier visionage : """ + str(self.dat_visio)
        if self.acteurs != [] and self.acteurs != "":
            t = t + """
*       Acteurs principaux : """
            for i in self.acteurs:
                t = t + """
*           """ + str(i)
        if self.note_perso != "":
            t = t + """
*           """ + self.note_perso
        return t


class Serie(Film):
    def __init__(self, id, titre, annee, realisateur, genre = "", acteurs_principaux = [], recompense = "", note = 0, plateforme = "", date_visio = "", dev = "", note_perso = ""):
        super().__init__(id, titre, annee, realisateur, genre, acteurs_principaux, recompense, note, date_visio, note_perso)
        self.plateforme = plateforme
        self.der_episode_vu = dev

    def __str__(self):
        t = super().__str__()
        if self.der_episode_vu != "":
            t = t + """
*       Dernier épisode vu : """ + self.der_episode_vu
        if self.plateforme != "":
            t = t + """
*       Plateforme : """ + self.plateforme
        return t


class Livres(Mere):
    def __init__(self, id, titre, annee, auteur, genre = "", recompense = "", etat = "", note = 0, prix = 0, tome = 0, narration = "", note_perso = ""):
        super().__init__(id, titre, annee, auteur, genre, recompense, note, prix)
        self.tome = tome
        self.etat = etat
        self.narration = narration
        self.note_perso = note_perso

    def __str__(self):
        t = """
*       Auteur : """ + self.createur + super().__str__()
        if self.tome != 0 and self.tome != "":
            t = t + """
*       Tome : """ + self.tome
        if self.narration != "":
            t = t + """
*       Narration : """ + self.narration
        if self.etat != "":
            t = t + """
*       Etat : """ + self.etat
        if self.note_perso != "":
            t = t + """
*       Quelque(s) note(s) perso : """ + self.note_perso
        return t


class Morceau(Mere):
    def __init__(self, id, titre, annee, artiste, genre = "", recompense = "", prix = 0, note = 0):
        super().__init__(id, titre, annee, artiste, recompense, genre, note, prix)

    def __str__(self):
        t = """
*       Artiste : """ + self.createur + super().__str__()
        return t


class Jeux_Videos(Mere):
    def __init__(self, id, titre, annee, studio, genre = "", recompense = "", note = 0, prix = 0, console = "", nbh = 0, nbjM = 1, nbjm = 1, note_perso = ''):
        super().__init__(id, titre, annee, studio, recompense, genre, note, prix)
        self.console = console
        self.nbh = nbh
        self.nbjM = nbjM
        self.nbjm = nbjm
        self.note_perso = note_perso

    def __str__(self):
        t = """
*       Studio : """ + self.createur + super().__str__()
        if self.console != "":
            t = t + """
*       Console : """ + self.console
        if self.nbh != 0 and self.nbh != "":
            t = t + """
*       Nombre d'heure de jeu : """ + str(self.nbh) + " h"
        t = t + """
*       Nombre de joueur Maximum : """ + str(self.nbjM) + """
*       Nombre de joueur minimum : """ + str(self.nbjm)
        if self.note_perso != "":
            t = t + """
*       Quelque(s) note(s) perso : """ + self.note_perso
        return t


class Jeux_Societe(Mere):
    def __init__(self, id, titre, annee, marque, genre = "", recompense = "", note = 0, prix = 0, support = "", nbjM = 1, nbjm = 1, note_perso = ''):
        super().__init__(id, titre, annee, marque, recompense, genre, note, prix)
        self.support = support
        self.nbjM = nbjM
        self.nbjm = nbjm
        self.note_perso = note_perso

    def __str__(self):
        t = """
*       Marque : """ + self.createur + super().__str__()
        if self.support != "":
            t = t + """
*       Support : """ + self.support
        t = t + """
*       Nombre de joueur Maximum : """ + str(self.nbjM) + """
*       Nombre de joueur minimum : """ + str(self.nbjm)
        if self.note_perso != "":
            t = t + """
*       Quelque(s) note(s) perso : """ + self.note_perso
        return t


class Plantes:
    def __init__(self, id, nom, espece, caract = "", luminosite = "", eau = "", pot = "", cache_pot = "", ou_elle_est = "", date = "", note = 0):
        self.id = id
        self.nom = nom
        self.espece = espece
        self.caracteristique = caract
        self.luminosite = luminosite
        self.eau = eau
        self.pot = pot
        self.cache_pot = cache_pot
        self.ou_elle_est = ou_elle_est
        self.date = date
        self.note = note

    def __str__(self):
        t = """
*       Nom : """ + self.nom + """
*       Espèce : """ + self.espece + """
*       Note : """ + str(self.note) + "/5"
        if self.caracteristique != "":
            t = t + """
*       Caractéristique : """ + self.caracteristique
        if self.luminosite != "":
            t = t + """
*       Besoin en lumière : """ + self.luminosite
        if self.eau != "":
            t = t + """
*       Besoin en eau : """ + self.eau
        if self.pot != "":
            t = t + """
*       Pot : """ + self.pot
        if self.cache_pot != "":
            t = t + """
*       Cache pot : """ + self.cache_pot
        if self.ou_elle_est != "":
            t = t + """
*       Positionnement : """ + self.ou_elle_est
        if self.date != datetime.date(1900, 1, 1) and self.date != "":
            t = t + """
*       Date : """ + str(self.date)
        return t

    def nb_objet_collection(self):
        self.nombre = len(self.theque)
