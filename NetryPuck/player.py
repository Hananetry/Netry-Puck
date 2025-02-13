# Importe les librairies necessaire
import pygame

"""
Classe Player

Attribut :
    -imageNetry, contient l'image du personnage
    -Netry_rect, contient les coordoonées du personnage
    -direction, contient la direction du personnage

Méthode :
    -move_right: ajoute 15 aux abscisses (la taille d'un bloc)
    -move_left: ajoute -15 aux abscisses
    -move_down: ajoute -15 aux ordonnées
    -move_up: ajoute -15 aux ordonnées

    -updatePos: modifie la position du personnage en fonction de sa direction
    -setDirection: Setter pour l'attribut direction
    -updateDirection: change la direction du personnage par une direction aléatoire en prenant en compte les collisions
"""

class Player():
    # Constructeur
    def __init__(self):
        self.imageNetry = pygame.image.load("images/netry_ouvert_right.PNG")
        self.Netry_rect = self.imageNetry.get_rect()
        self.Netry_rect.x = 225
        self.Netry_rect.y = 285
        self.direction = 'I'
 
 
    # Les différentes méthodes pour mettre à jour les coordoonées
    def move_right(self):
        self.Netry_rect.x += 15
        #pygame.time.wait(500)
        
         
    def move_left(self):
        self.Netry_rect.x -= 15
        #pygame.time.wait(500)
        
    def move_down(self):        
        self.Netry_rect.y += 15
        #pygame.time.wait(500)
        
    def move_up(self):        
        self.Netry_rect.y -= 15
        #pygame.time.wait(500)

    def updatePos(self, maze):
        # Change la direction du personnage
        # Vérifie si la direction et que la couleur du bloc au dessus soit bien la couleur d'une route
        if (self.direction == 'U') and maze.get_at((self.Netry_rect.x, self.Netry_rect.y - 15)) == (80, 80, 80, 255):
            self.move_up()
            self.imageNetry = pygame.image.load("images/netry_ouvert_up.PNG")
        if (self.direction == 'D') and maze.get_at((self.Netry_rect.x, self.Netry_rect.y + 15)) == (80, 80, 80, 255):
            self.move_down()
            self.imageNetry = pygame.image.load("images/netry_ouvert_down.PNG")
        if (self.direction == 'R') and maze.get_at((self.Netry_rect.x + 15, self.Netry_rect.y)) == (80, 80, 80, 255):
            self.move_right()
            self.imageNetry = pygame.image.load("images/netry_ouvert_right.PNG")
        if (self.direction == 'L') and maze.get_at((self.Netry_rect.x - 15, self.Netry_rect.y)) == (80, 80, 80, 255):
            self.move_left()
            self.imageNetry = pygame.image.load("images/netry_ouvert_left.PNG")
    
    def setDirection(self, direction):
        # Vérifie que le paramètre rentré n'est pas le même que dans direction
        if self.direction != direction:
            self.direction = direction
            
            
                      