from tkinter import *

class Joueur():
    x=0
    y=0
    numero = 0
    
    def __init__(self, x , y, numero, jeu): #Initialisation
        self.x = x
        self.y = y
        self.numero = numero
        self.jeu = jeu

    def deplacer(self, x , y): #Teste les colision avec le terrain puis déplace le joueur
        deplacer = False
        if(x == 1 and not self.jeu.testCollision(self.x + 1, self.y)):
            self.x += 1
            deplacer = True
        if(x == -1 and not self.jeu.testCollision(self.x - 1, self.y)):
            self.x -= 1
            deplacer = True
        if(y == 1 and not self.jeu.testCollision(self.x, self.y - 1)):
            self.y -= 1
            deplacer = True
        if(y == -1 and not self.jeu.testCollision(self.x, self.y + 1)):
            self.y += 1
            deplacer = True

        if(deplacer): #Si aucun obstacle n'est rencontré, on affiche le déplacement
            self.jeu.afficherDeplacementJoueur(self.numero, x, y)

    def getPositionX(self): #Retourne la position X d'un joueur
        return self.x

    def getPositionY(self): #Retourne la position Y d'un joueur
        return self.y

