from tkinter import *
from tkinter.messagebox import *
from Jeu import Jeu

#Configuration de la fenêtre
fenetre = Tk()
fenetre.config(bg="beige")
fenetre.title("Zombies !")
fenetre.resizable(width=FALSE, height=FALSE)
fenetre.geometry("672x672") #32 pixels fois 21 cases
jeu = Jeu(fenetre)

def chargerNiveau(niveau): #Charge le niveau
    jeu.afficher(niveau)

def recommencer(): #Recomence le niveau
    jeu.recommencer()

def quitter(): #Ferme la fenêtre
    fenetre.destroy()

def aideEditeur():
    texte = "Clic gauche pour poser un objet\nClic droit pour détruire un bloc\n\n"
    texte += "Pavé numérique:\n1 : Selectionner Mur\n2 : Selectionner Zombie\n3 : Selectionner Bouton\n4 : Selectionner Porte\n5 : Selectionner Drapeau\n\n"
    texte += "Il est impossible de supprimer un zombie ou une porte"
    showinfo("Aide Editeur", texte)

def propos():
    showinfo("A propos","Projet d'ISN réalisé durrant l'année scolaire 2015-2016 par:\nStéphane HULOT\nSCHARFF Raphaël\nLIGNOY Charles\n\nContient 5 niveaux, un tutoriel et un mode éditeur de niveau")

#Barre de menu
barreMenu = Menu(fenetre)

#Menu en cascade des différent niveau
choixNiveau = Menu(barreMenu, tearoff = 0)
choixNiveau.add_command(label = "Tutoriel", command = lambda: chargerNiveau(0))
choixNiveau.add_separator()
choixNiveau.add_command(label = "Niveau 1", command = lambda: chargerNiveau(1))
choixNiveau.add_command(label = "Niveau 2", command = lambda: chargerNiveau(2))
choixNiveau.add_command(label = "Niveau 3", command = lambda: chargerNiveau(3))
choixNiveau.add_command(label = "Niveau 4", command = lambda: chargerNiveau(4))
choixNiveau.add_command(label = "Niveau 5", command = lambda: chargerNiveau(5))
choixNiveau.add_separator()
choixNiveau.add_command(label = "Editeur", command = lambda: chargerNiveau(-1))

barreMenu.add_cascade(label = "Niveaux", menu = choixNiveau)

barreMenu.add_command(label = "Recommencer", command = recommencer)
barreMenu.add_command(label = "Quitter", command = quitter)
barreMenu.add_command(label = "Aide Editeur", command = aideEditeur)
barreMenu.add_command(label = "A propos", command = propos)

fenetre.config(menu=barreMenu)

chargerNiveau(0)

fenetre.mainloop()
