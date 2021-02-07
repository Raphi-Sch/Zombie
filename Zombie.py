from tkinter import *
from random import randint
from math import sqrt

class Zombie():
    x=0
    y=0
    numero = 0 #Identifiant du zombie
    
    def __init__(self, x , y, numero, jeu):
        self.x = x
        self.y = y
        self.numero = numero
        self.jeu = jeu

    def deplacer(self, joueur1, joueur2): #Déplace le zombie en fonction de la direction du joueur sinon d'un chemin possible
        self.distanceJoueur(joueur1,joueur2) #Calcule les distances entre le zombie et chaque joueur
        
        if self.distJoueur1 == 1:
            self.jeu.joueurMort = 1
            return

        if self.distJoueur2 == 1:
            self.jeu.joueurMort = 2
            return
        
        move = False
        direction = self.suivreJoueur() #Suis le joueur en fonction de sa potion
        
        if(direction == "N" and not self.jeu.testCollision(self.x, self.y + 1)): #Déplacement Haut
            self.y += 1
            self.jeu.afficherDeplacementZombie(0, 1, self.numero)
            move = True
            
        if(direction == "S" and not self.jeu.testCollision(self.x, self.y - 1)): #Déplacement Bas
            self.y -= 1
            self.jeu.afficherDeplacementZombie(0, -1, self.numero)
            move = True
            
        if(direction == "E" and not self.jeu.testCollision(self.x + 1, self.y)): #Déplacement Droite
            self.x += 1
            self.jeu.afficherDeplacementZombie(1, 0, self.numero)
            move = True
            
        if(direction == "W" and not self.jeu.testCollision(self.x - 1, self.y)): #Déplacement Gauche
            self.x -= 1
            self.jeu.afficherDeplacementZombie(-1, 0, self.numero)
            move = True

        if(move == False): #Si il n'y a aucun déplacement (obstacle rencontré), le zombie analyse la situtation
            chemin = self.cheminPossible()
            if(chemin == "N"): #Deplacement Haut
                self.y += 1
                self.jeu.afficherDeplacementZombie(0, 1, self.numero)
                
            if(chemin == "S"): #Deplacement Bas
                self.y -= 1
                self.jeu.afficherDeplacementZombie(0, -1, self.numero)
                
            if(chemin == "E"): #Deplacement Droite
                self.x += 1
                self.jeu.afficherDeplacementZombie(1, 0, self.numero)
                
            if(chemin == "W"): #Deplacement Gauche
                self.x -= 1
                self.jeu.afficherDeplacementZombie(-1, 0, self.numero)

    def distanceJoueur(self,joueur1,joueur2): #Calcule la distance entre le joueur le plus proche et un zombie
        self.distJoueur1 = sqrt((joueur1.getPositionX()-self.x)**2 +(joueur1.getPositionY()-self.y)**2)#Th de Pythagore
        self.distJoueur2 = sqrt((joueur2.getPositionX()-self.x)**2 +(joueur2.getPositionY()-self.y)**2)

        
        self.dx = 0 #Position X relative
        self.dy = 0 #Position Y relative
        
        if(self.distJoueur1 < self.distJoueur2): #Si le joueur 1 est le plus proche
            self.dx = joueur1.getPositionX() - self.x
            self.dy = joueur1.getPositionY() - self.y
        else: #Si le joueur 2 est le plus proche
            self.dx = joueur2.getPositionX() - self.x
            self.dy = joueur2.getPositionY() - self.y
    
    def suivreJoueur(self): #Retourne la direction du joueur le plus proche
        if(abs(self.dx) > abs(self.dy)): #Si la distance x à parcrourir est plus grande que la distance y à parcourir
            if(self.dx > 0):
                return "E" #Droite
            elif(self.dx < 0):
                return "W" #Gauche
        else: #Si la distance y à parcrourir est plus grande que la distance x à parcourir
            if(self.dy > 0):
                return "N" #Haut
            elif(self.dy < 0):
                return "S" #Bas

    def cheminPossible(self): #Retourne une direction possible en fonction de la situation
        #Cas 4 blocs
        if(self.jeu.testCollision(self.x,self.y + 1) and self.jeu.testCollision(self.x - 1,self.y) and self.jeu.testCollision(self.x + 1,self.y) and self.jeu.testCollision(self.x, self.y - 1)):
           return ""
        
        #Cas 3 blocs
        #Si il y a qqch Nord + Ouest + Est, prendre Sud
        if(self.jeu.testCollision(self.x,self.y + 1) and self.jeu.testCollision(self.x - 1,self.y) and self.jeu.testCollision(self.x + 1,self.y) ):
            return "S"
        #Si il y a qqch Sud + Ouest + Est, prendre Nord
        if(self.jeu.testCollision(self.x,self.y - 1) and self.jeu.testCollision(self.x - 1,self.y) and self.jeu.testCollision(self.x + 1,self.y) ):
            return "N"
        #Si il y a qqch Nord + Ouest + Sud, prendre Est
        if(self.jeu.testCollision(self.x,self.y + 1) and self.jeu.testCollision(self.x - 1,self.y) and self.jeu.testCollision(self.x,self.y - 1) ):
            return "E"
        #Si il y a qqch Nord + Est + Sud, prendre Ouest
        if(self.jeu.testCollision(self.x,self.y + 1) and self.jeu.testCollision(self.x + 1,self.y) and self.jeu.testCollision(self.x,self.y - 1) ):
            return "W"
        
        #Cas 2 blocs
        #Si il y a qqch Nord + Ouest prendre Est
        if(self.jeu.testCollision(self.x,self.y + 1) and self.jeu.testCollision(self.x - 1,self.y)):
            return "E"
        #Si il y a qqch Nord + Est prendre Ouest
        if(self.jeu.testCollision(self.x,self.y + 1) and self.jeu.testCollision(self.x + 1,self.y)):
            return "W"
        #Si il y a qqch Sud + Ouest prendre Est
        if(self.jeu.testCollision(self.x,self.y - 1) and self.jeu.testCollision(self.x - 1,self.y)):
            return "E"
        #Si il y a qqch Sud + Est prendre Ouest
        if(self.jeu.testCollision(self.x,self.y - 1) and self.jeu.testCollision(self.x + 1,self.y)):
            return "W"

        #Cas 1 bloc
        #Si il y a qqch Nord/Sud prendre Est ou Ouest (en fonction de la direction du joueur) 
        if(self.jeu.testCollision(self.x,self.y + 1) or self.jeu.testCollision(self.x,self.y - 1)):
            if(self.dx < 0):
                return "W"
            if(self.dx > 0):
                return "E"
        #Si il y a qqch Est/Ouest prendre Nord
        if(self.jeu.testCollision(self.x + 1,self.y) or self.jeu.testCollision(self.x - 1,self.y)):
            if(self.dy > 0):
                return "N"
            if(self.dy < 0):
                return "S"
        
    def getPositionX(self): #Retourne la position X du zombie
        return self.x

    def getPositionY(self): #Retourne la position Y du zombie
        return self.y

