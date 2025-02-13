# Importe les librairies necessaire
import pygame
import random

"""
Classe Ghost

Attribut :
    -imageGhost, contient l'image du fantôme
    -Ghost_rect, contient les coordoonées du fantôme
    -direction, contient la direction des fantômes

Méthode :
    -move_right: ajoute 15 aux abscisses (la taille d'un bloc)
    -move_left: ajoute -15 aux abscisses
    -move_down: ajoute -15 aux ordonnées
    -move_up: ajoute -15 aux ordonnées

    -updatePos: modifie la position du fantôme en fonction de sa direction
    -setDirection: Setter pour l'attribut direction
    -updateDirection: change la direction du fantôme par une direction aléatoire en prenant en compte les collisions
"""
class Ghost():

    # Constructeur
    def __init__(self, x, y):
        self.imageGhost = pygame.image.load("images/ghost1.PNG")
        self.Ghost_rect = self.imageGhost.get_rect()
        self.Ghost_rect.x = x
        self.Ghost_rect.y = y
        self.direction = 'I'

    # Les différentes méthode pour mettre à jour les coordoonées
    def move_right(self):
        self.Ghost_rect.x += 15
        # pygame.time.wait(500)

    def move_left(self):
        self.Ghost_rect.x -= 15
        # pygame.time.wait(500)

    def move_down(self):
        self.Ghost_rect.y += 15
        # pygame.time.wait(500)

    def move_up(self):
        self.Ghost_rect.y -= 15
        # pygame.time.wait(500)

    def updatePos(self, maze):
        # Change la direction pour un déplacement "aléatoire" des fantômes 
        self.updateDirection(maze)

        # Vérifie si la direction va vers le haut, et que la couleur du bloc au dessus soit bien la couleur d'une route, si c'est le cas, on le déplace vers le haut
        if (self.direction == 'U') and maze.get_at((self.Ghost_rect.x, self.Ghost_rect.y - 15)) == (80, 80, 80, 255):
            self.move_up()
        # La même en bas
        if (self.direction == 'D') and maze.get_at((self.Ghost_rect.x, self.Ghost_rect.y + 15)) == (80, 80, 80, 255):
            self.move_down()
        #A droite
        if (self.direction == 'R') and maze.get_at((self.Ghost_rect.x + 15, self.Ghost_rect.y)) == (80, 80, 80, 255):
            self.move_right()
        #Et à gauche
        if (self.direction == 'L') and maze.get_at((self.Ghost_rect.x - 15, self.Ghost_rect.y)) == (80, 80, 80, 255):
            self.move_left()

    def setDirection(self, direction):
        # Vérifie que le paramètre rentré n'est pas le même que dans direction
        if self.direction != direction:
            self.direction = direction

    # Méthode pour mettre à jour les directions
    def updateDirection(self, maze):
        # Liste qui contiendra les prochaines direction valide
        possibleDirection = []

        # Vérifie si la couleur en haut en bas à gauche et à droite du fantôme sont bien celle de la route, si c'est le cas on ajoute la direction à la liste des directions possible
        if maze.get_at((self.Ghost_rect.x, self.Ghost_rect.y - 15)) == (80, 80, 80, 255):
            possibleDirection.append('U')
        if maze.get_at((self.Ghost_rect.x, self.Ghost_rect.y + 15)) == (80, 80, 80, 255):
            possibleDirection.append('D')
        if maze.get_at((self.Ghost_rect.x + 15, self.Ghost_rect.y)) == (80, 80, 80, 255):
            possibleDirection.append('R')
        if maze.get_at((self.Ghost_rect.x - 15, self.Ghost_rect.y)) == (80, 80, 80, 255):
            possibleDirection.append('L')

        # Renvoie une direction aléatoire parmi les directions possible
        self.setDirection(possibleDirection[random.randint(0, len(possibleDirection) - 1)])
