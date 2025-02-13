# Importe les librairies necessaire
import pygame
from player import Player

"""
Classe Points

Attribut :
    -image55p, contient l'image du point 55
    -image150p, contient l'image du point 150
    -image55p_rect, contient les coordoonées du point
    -image150p_rect, contient les coordoonées du point
    -score, definie comme un entier

Méthode :
    -positionPoints: collision entre netry et points et positions données aux points
 
"""

player = Player()


class Points():
    # Constructeur
    def __init__(self):
        self.image55p = pygame.image.load("images/55p.png")
        self.image55p_rect = self.image55p.get_rect()
        
        self.image150p = pygame.image.load("images/150p.png")
        self.image150p_rect = self.image150p.get_rect()
                
        self.image55p_rect.x = 30
        self.image55p_rect.y = 90
        
        self.image150p_rect.x = 90
        self.image150p_rect.y = 345
        
        self.score = 0
        
        
        
        
        
    def positionPoints(self, player):
        
        if player.Netry_rect.x == self.image55p_rect.x and player.Netry_rect.y == self.image55p_rect.y :
            self.score += 55
            if player.Netry_rect.x == 30 and player.Netry_rect.y == 90:
                self.image55p_rect.x = 45
                self.image55p_rect.y = 120
                
            if player.Netry_rect.x == 45 and player.Netry_rect.y == 120:
                self.image55p_rect.x = 15
                self.image55p_rect.y = 240
                
            if player.Netry_rect.x == 15 and player.Netry_rect.y == 240:
                self.image55p_rect.x = 15
                self.image55p_rect.y = 345
                
            if player.Netry_rect.x == 15 and player.Netry_rect.y == 345:
                self.image55p_rect.x = 75
                self.image55p_rect.y = 300
                
            if player.Netry_rect.x == 75 and player.Netry_rect.y == 300:
                self.image55p_rect.x = 105
                self.image55p_rect.y = 225
                
            if player.Netry_rect.x == 105 and player.Netry_rect.y == 225:
                self.image55p_rect.x = 75
                self.image55p_rect.y = 180
                
            if player.Netry_rect.x == 75 and player.Netry_rect.y == 180:
                self.image55p_rect.x = 135
                self.image55p_rect.y = 135
                
            if player.Netry_rect.x == 135 and player.Netry_rect.y == 135:
                self.image55p_rect.x = 210
                self.image55p_rect.y = 120
                
            if player.Netry_rect.x == 210 and player.Netry_rect.y == 120:
                self.image55p_rect.x = 240
                self.image55p_rect.y = 195
                
            if player.Netry_rect.x == 240 and player.Netry_rect.y == 195:
                self.image55p_rect.x = 285
                self.image55p_rect.y = 225
                
            if player.Netry_rect.x == 285 and player.Netry_rect.y == 225:
                self.image55p_rect.x = 345
                self.image55p_rect.y = 195
                
            if player.Netry_rect.x == 345 and player.Netry_rect.y == 195:
                self.image55p_rect.x = 300
                self.image55p_rect.y = 255
                
            if player.Netry_rect.x == 300 and player.Netry_rect.y == 255:
                self.image55p_rect.x = 285
                self.image55p_rect.y = 90
                
            if player.Netry_rect.x == 285 and player.Netry_rect.y == 90:
                self.image55p_rect.x = 375
                self.image55p_rect.y = 120
                
            if player.Netry_rect.x == 375 and player.Netry_rect.y == 120:
                self.image55p_rect.x = 420
                self.image55p_rect.y = 210
                
            if player.Netry_rect.x == 420 and player.Netry_rect.y == 210:
                self.image55p_rect.x = 420
                self.image55p_rect.y = 255
                
            if player.Netry_rect.x == 420 and player.Netry_rect.y == 255:
                self.image55p_rect.x = 345
                self.image55p_rect.y = 285
                
            if player.Netry_rect.x == 345 and player.Netry_rect.y == 285:
                self.image55p_rect.x = 285
                self.image55p_rect.y = 345
                
            if player.Netry_rect.x == 285 and player.Netry_rect.y == 345:
                self.image55p_rect.x = 420
                self.image55p_rect.y = 345
                
            if player.Netry_rect.x == 420 and player.Netry_rect.y == 345:
                self.image55p_rect.x = -500
                self.image55p_rect.y = -500
                
                
                
                
            
        if player.Netry_rect.x == self.image150p_rect.x and player.Netry_rect.y == self.image150p_rect.y :
            self.score += 150
            if player.Netry_rect.x == 90 and player.Netry_rect.y == 345:
                self.image150p_rect.x = 420
                self.image150p_rect.y = 90
                
            if player.Netry_rect.x == 420 and player.Netry_rect.y == 90:
                self.image150p_rect.x = 45
                self.image150p_rect.y = 210
                
            if player.Netry_rect.x == 45 and player.Netry_rect.y == 210:
                self.image150p_rect.x = 150
                self.image150p_rect.y = 90
                
            if player.Netry_rect.x == 150 and player.Netry_rect.y == 90:
                self.image150p_rect.x = 375
                self.image150p_rect.y = 285
                
            if player.Netry_rect.x == 375 and player.Netry_rect.y == 285:
                self.image150p_rect.x = -500
                self.image150p_rect.y = -500

    
    
        


