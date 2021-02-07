from tkinter import *
from tkinter.messagebox import *
from copy import deepcopy

from Joueur import Joueur
from Zombie import Zombie


class Jeu(Canvas):


#####################################################################
#                                                                   #
#                    Liste des niveaux                              #
# 0 = sol, 1 = mur, 2 = zombie, 3 = bouton, 4 = porte, 5 = drapeau, #
#                                                                   #
#####################################################################

#L'identifiant 6 est utilisé dans l'éditeur pour les portes ouvertes

    
    #Niveau -1
    custom=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    #Niveau 0
    tuto=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 2, 0, 1, 1, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
    niveau1=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 0, 1, 0, 0, 3, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    niveau2=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
             [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 5, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 4, 1, 0, 1, 1, 0, 1, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1],
             [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 1, 2, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
             [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
             [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 2, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 0, 0, 3, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    niveau3=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
             [1, 0, 0, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    niveau4=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 1, 3, 0, 0, 2, 0, 1, 0, 0, 5, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 4, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 1, 4, 4, 1, 1, 0, 0, 1, 1, 1, 1, 4, 1, 1, 1, 1, 4, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 2, 0, 1],
             [1, 0, 3, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    niveau5=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1 ,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
             [1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1],
             [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    fin=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, width=672, height=672, **kwargs)
        
        #Textures
        self.murTexture = PhotoImage(file = "Mur.gif")
        self.solTexture = PhotoImage(file = "Sol.gif")
        self.boutonTexture = PhotoImage(file = "Bouton.gif")
        self.porteTexture = PhotoImage(file = "Porte.gif")
        self.porteOuverteTexture = PhotoImage(file = "Porte_ouverte.gif")
        self.drapeauTexture = PhotoImage(file = "Drapeau.gif")
        self.J1Texture = PhotoImage(file = "Joueur1.gif")
        self.J2Texture = PhotoImage(file = "Joueur2.gif")
        self.zombieTexture = PhotoImage(file = "Zombie.gif")
        self.tutorielTexture = PhotoImage(file = "Tutoriel.gif")
        self.editeurTexture = PhotoImage(file = "Editeur.gif")
        
        #Detection des touches
        self.fenetre = parent
        self.fenetre.bind("<Key>", self.eventClavier)


#############################################
#                                           #
#       Initialisation du niveau            #
#                                           #
#############################################


    def afficher(self, niveau): #Affichage et mise en place d'un niveau
        self.delete("all")
        self.niveau = niveau
        #Chargement du niveau
        if niveau == -1:
            self.niveauActuel = deepcopy(self.custom)
        if niveau == 0:
            self.niveauActuel = deepcopy(self.tuto)
        if niveau == 1:
            self.niveauActuel = deepcopy(self.niveau1)
        if niveau == 2:
            self.niveauActuel = deepcopy(self.niveau2)
        if niveau == 3:
            self.niveauActuel = deepcopy(self.niveau3)
        if niveau == 4:
            self.niveauActuel = deepcopy(self.niveau4)
        if niveau == 5:
            self.niveauActuel = deepcopy(self.niveau5)
        if niveau == 6:
            self.niveauActuel = deepcopy(self.fin)
            
        #Initialisation des manches
        self.deplacement = 0
        
        #Création des joueurs
        self.joueur1 = Joueur(2, 2, 1, self)
        self.joueur2 = Joueur(4, 2, 2, self)
        
        #Création des listes (remplies lors de la lecture de la matrice)
        self.zombies = []
        self.portes = []
        self.portesX = []
        self.portesY = []

        #Affichage de la grille (21x21 blocs)
        for y in range(0, 21):
            for x in range (0, 21):
                if(self.niveauActuel[y][x] == 0): #Sol
                    self.create_image(16 + x * 32, 16 + y * 32, image = self.solTexture)
                if(self.niveauActuel[y][x] == 1): #Mur
                    self.create_image(16 + x * 32, 16 + y * 32, image = self.murTexture)
                if(self.niveauActuel[y][x] == 2): #Zombie
                    self.zombies.append(Zombie(x, y, len(self.zombies), self))
                    self.create_image(16 + x * 32, 16 + y * 32, image = self.solTexture)
                if(self.niveauActuel[y][x] == 3): #Bouton
                    self.create_image(16 + x * 32, 16 + y * 32, image = self.solTexture)
                    self.create_image(16 + x * 32, 16 + y * 32, image = self.boutonTexture)
                if(self.niveauActuel[y][x] == 4): #Porte
                    self.portes.append(self.create_image(16 + x * 32, 16 + y * 32, image = self.porteTexture))
                    self.portesX.append(x)
                    self.portesY.append(y)
                if(self.niveauActuel[y][x] == 5): #Drapeau
                    self.create_image(16 + x * 32, 16 + y * 32, image = self.solTexture)
                    self.create_image(16 + x * 32, 16 + y * 32, image = self.drapeauTexture)
                    
        #Affichage des joueurs 
        self.J1 = self.create_image(16 + self.joueur1.getPositionX() * 32, 16 + self.joueur1.getPositionY() * 32, image = self.J1Texture)
        self.J2 = self.create_image(16 + self.joueur2.getPositionX() * 32, 16 + self.joueur2.getPositionY() * 32, image = self.J2Texture)

        self.Z = [] #Affichage de tout les zombies
        for i in range(0, len(self.zombies)):
            self.Z.append(self.create_image(16 + self.zombies[i].getPositionX() * 32, 16 + self.zombies[i].getPositionY() * 32, image = self.zombieTexture))

        #Tutoriel
        if(niveau == 0):
            self.create_image(336, 336, image = self.tutorielTexture)

        #Editeur
        if(niveau == -1):
            self.activeEditeur(True) #Active l'éditeur si le niveau actuel est -1 (terrain a éditer)
            self.create_image(26, 26, image = self.editeurTexture) #Interface editeur
            self.blocEditeur = self.create_image(26, 26, image = self.murTexture) #Interface editeur
        else:
            self.activeEditeur(False) #Active l'éditeur si le niveau actuel est -1 (terrain a éditer)

        #Change le titre de la fenêtre en fonction du niveau
        if(niveau == -1):
            self.fenetre.title("Zombies ! - Editeur")
        elif(niveau == 0):
            self.fenetre.title("Zombies ! - Tutoriel")
        else:
            self.fenetre.title("Zombies ! - Niveau " + str(niveau))
        
        self.pack()


#############################################
#                                           #
#               Collisions                  #
#                                           #
#############################################


    def testCollision(self, x, y): #Retourne True si collision
        if(self.niveauActuel[y][x] == 1 or self.niveauActuel[y][x] == 4):
            return True
        if(self.joueur1.getPositionX() == x and self.joueur1.getPositionY() == y):
            return True
        if(self.joueur2.getPositionX() == x and self.joueur2.getPositionY() == y):
            return True
        for i in range(0, len(self.zombies)):
            if(self.zombies[i].getPositionX() == x and self.zombies[i].getPositionY() == y):
                return True
            
        return False #Si aucune des conditions n'est remplie, il n'y a pas de collision


    def testBouton(self): #Vérifie si un des boutons est activé, dans quel cas les portes s'ouvrent
        boutonActif = False
        if(self.niveauActuel[self.joueur1.getPositionY()][self.joueur1.getPositionX()] == 3): #Bouton activé par le joueur 1
            boutonActif = True
        if(self.niveauActuel[self.joueur2.getPositionY()][self.joueur2.getPositionX()] == 3): #Bouton activé par le joueur 2
            boutonActif = True
        for i in range(0, len(self.zombies)):
            if(self.niveauActuel[self.zombies[i].getPositionY()][self.zombies[i].getPositionX()] == 3): #Bouton activé par un zombie
                boutonActif = True
        
        if(boutonActif): #Ouverture des portes
            for i in range(0, len(self.portes)):
                self.itemconfig(self.portes[i], image = self.porteOuverteTexture)
                self.niveauActuel[self.portesY[i]][self.portesX[i]] = 6 #Identifiant 6 utilisé dans l'éditeur
        else: #Fermeture des portes
            for i in range(0, len(self.portes)):
                self.itemconfig(self.portes[i], image = self.porteTexture)
                self.niveauActuel[self.portesY[i]][self.portesX[i]] = 4


    def testDrapeau(self): #Vérifie si un drapeau est atteint, dans quel cas le niveau est complété
        drapeau = False
        if(self.niveauActuel[self.joueur1.getPositionY()][self.joueur1.getPositionX()] == 5): #Le joueur 1 a fini le niveau
            drapeau = True
        if(self.niveauActuel[self.joueur2.getPositionY()][self.joueur2.getPositionX()] == 5): #Le joueur 2 a fini le niveau
            drapeau = True

        if(drapeau):
            self.victoire()


#############################################
#                                           #
#              Fin de niveau                #
#                                           #
#############################################


    def gameOver(self, numero): #Un des joueurs a été mordu
        if(self.niveau == -1):
            showwarning("GAME OVER", "Vous avez échoué a votre propre niveau !")
        else:
            showwarning("GAME OVER", "Le joueur " + str(numero) + " a été mordu !\nVous avez perdu le niveau " + str(self.niveau) + " !")
            
        self.recommencer()


    def victoire(self): #Un des joueurs a atteint un drapeau
        if(self.niveau == -1):
            showinfo("Victoire !","Vous avez fini votre propre niveau !")
            self.niveau = -1
        elif(self.niveau == 0):
            showinfo("Victoire !","Vous avez fini le tutoriel !")
            self.niveau = 1
        elif(self.niveau == 5):
            showinfo("Victoire !","Vous avez fini le jeu !")
            self.niveau = 6
        else:
            showinfo("Victoire !","Vous avez fini le niveau " + str(self.niveau) + " !")
            self.niveau += 1
        
        self.afficher(self.niveau)


    def recommencer(self): #Le boutton recommencer du menu a été pressé
        self.afficher(self.niveau)
        self.depalcement = 0


#############################################
#                                           #
#          Afficher déplacements            #
#                                           #
#############################################


    def afficherDeplacementJoueur(self, joueur, x, y): #Déplacement d'un joueur
        if(joueur == 1):
            self.move(self.J1, x * 32, -y * 32)
        elif(joueur == 2):
            self.move(self.J2, x * 32, -y * 32)
        self.testBouton()
        self.testDrapeau()


    def afficherDeplacementZombie(self, x, y, numero): #Déplacement d'un zombie
        self.move(self.Z[numero], x * 32, y * 32)
        self.testBouton()


#############################################
#                                           #
#                 Clavier                   #
#                                           #
#############################################


    def eventClavier(self, event): #Actif pour tout les evenements du clavier
        #Déplacement du joueur 1
        if(event.keysym == "z" or event.keysym == "Z"): 
            self.joueur1.deplacer(0, 1)
            self.deplacement += 1
        if(event.keysym == "d" or event.keysym == "D"):
            self.joueur1.deplacer(1, 0)
            self.deplacement += 1
        if(event.keysym == "s" or event.keysym == "S"):
            self.joueur1.deplacer(0, -1)
            self.deplacement += 1
        if(event.keysym == "q" or event.keysym == "Q"):
            self.joueur1.deplacer(-1, 0)
            self.deplacement += 1

        #Déplacement du joueur 1 
        if(event.keysym == "Up"):
            self.joueur2.deplacer(0, 1)
            self.deplacement += 1
        if(event.keysym == "Right"):
            self.joueur2.deplacer(1, 0)
            self.deplacement += 1
        if(event.keysym == "Down"):
            self.joueur2.deplacer(0, -1)
            self.deplacement += 1
        if(event.keysym == "Left"):
            self.joueur2.deplacer(-1, 0)
            self.deplacement += 1

        #Déplacement des zombie si la somme des déplacement des joueur > 2
        if(self.deplacement >= 2): 
            self.deplacement = 0
            self.joueurMort = 0
            for i in range(0, len(self.zombies)):
                self.zombies[i].deplacer(self.joueur1, self.joueur2)

            if(not self.joueurMort == 0):
                self.gameOver(self.joueurMort)

        #Clavier mode editeur
        if(self.niveau == -1):
            if(event.keysym == "1"):
                self.blocActuel = 1
            if(event.keysym == "2"):
                self.blocActuel = 2
            if(event.keysym == "3"):
                self.blocActuel = 3
            if(event.keysym == "4"):
                self.blocActuel = 4
            if(event.keysym == "5"):
                self.blocActuel = 5
            self.afficherBlocEditeur() #Affiche le bloc selectionné


#############################################
#                                           #
#                 Edtieur                   #
#                                           #
#############################################

                
    def activeEditeur(self, activer):
        if(activer == True):
            self.fenetre.bind("<Button-1>", self.poserBloc) #Clic gauche
            self.fenetre.bind("<Button-3>", self.effacerBloc) #Clic droit
            self.blocActuel = 1
        else:
            self.fenetre.unbind("<Button-1>")
            self.fenetre.unbind("<Button-3>")
    
    def poserBloc(self, event): #Place un bloc sous la souris (clic gauche)
        x = int(event.x / 32)
        y = int(event.y / 32)

        if(self.testCollision(x, y) or not self.niveauActuel[y][x] == 0): #On n'execute pas la suite si il y a quelque chose a l'endrois ciblé
            return
        
        if(self.blocActuel == 1):
            self.create_image(16 + x * 32, 16 + y * 32, image = self.murTexture)
            self.niveauActuel[y][x] = 1
            
        if(self.blocActuel == 2):
            self.zombies.append(Zombie(x, y, len(self.zombies), self))
            self.Z.append(self.create_image(16 + self.zombies[len(self.zombies) - 1].getPositionX() * 32, 16 + self.zombies[len(self.zombies) - 1].getPositionY() * 32, image = self.zombieTexture))

        if(self.blocActuel == 3):
            self.create_image(16 + x * 32, 16 + y * 32, image = self.boutonTexture)
            self.niveauActuel[y][x] = 3

        if(self.blocActuel == 4):
            self.portes.append(self.create_image(16 + x * 32, 16 + y * 32, image = self.porteTexture))
            self.portesX.append(x)
            self.portesY.append(y)
            self.niveauActuel[y][x] = 4

        if(self.blocActuel == 5):
            self.create_image(16 + x * 32, 16 + y * 32, image = self.drapeauTexture)
            self.niveauActuel[y][x] = 5

        self.premierPlan()


    def effacerBloc(self, event): #Efface le bloc sous la souris (clic droit)
        x = int(event.x / 32)
        y = int(event.y / 32)
        
        if(self.niveauActuel[y][x] == 4 or self.niveauActuel[y][x] == 6): #Empeche de supprimer les portes
            return
        
        self.niveauActuel[y][x] = 0 
        self.create_image(16 + x * 32, 16 + y * 32, image = self.solTexture)

        self.premierPlan()


    def premierPlan(self): #Place les joueurs et zombies au premier plan pour qu'ils restent devant les nouveaux blocs
        self.tag_raise(self.J1)
        self.tag_raise(self.J2)
        
        for i in range(0, len(self.zombies)):
             self.tag_raise(self.Z[i])


    def afficherBlocEditeur(self): #Affiche le bloc sélectionné en haut a gauche de l'écran
        if(self.blocActuel == 1):
            self.itemconfig(self.blocEditeur, image = self.murTexture)
        if(self.blocActuel == 2):
            self.itemconfig(self.blocEditeur, image = self.zombieTexture)
        if(self.blocActuel == 3):
            self.itemconfig(self.blocEditeur, image = self.boutonTexture)
        if(self.blocActuel == 4):
            self.itemconfig(self.blocEditeur, image = self.porteTexture)
        if(self.blocActuel == 5):
            self.itemconfig(self.blocEditeur, image = self.drapeauTexture)





