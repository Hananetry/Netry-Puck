# Importe le module pygame ainsi que les classes que j'ai créé
import pygame
from player import Player
from ghost import Ghost
from point_score import Points

import time

# Initialise pygame
pygame.init()

# Définit la résolution et le titre de la fenêtre
screen = pygame.display.set_mode((500, 375))
pygame.display.set_caption("Netry Puck")

# Charge plusieurs police de charactère
medium_font = pygame.font.Font("images/RetroGaming.ttf", 14)
smaller_font = pygame.font.Font("images/RetroGaming.ttf", 13)

# Charge l'image de fond (le labyrinthe)
backgroundGame = pygame.image.load("images/backgroundGame.PNG")
backgroundGame_rect = backgroundGame.get_rect(topleft=(0, 0))

# Charge l'image de Game Over
backgroundGameOver = pygame.image.load("images/gameover.PNG")
backgroundGameOver_rect = backgroundGameOver.get_rect(topleft=(0, 0))

# L'image de Game Over si on a aucun point
backgroundGameOver0 = pygame.image.load("images/gameover0.PNG")
backgroundGameOver0_rect = backgroundGameOver0.get_rect(topleft=(0, 0))

# L'image si on gagne une partie (quand on a 1980 points)
backgroundWin = pygame.image.load("images/win.PNG")
backgroundWin_rect = backgroundWin.get_rect(topleft=(0, 0))

# Charge le fond d'acceuil
backgroundPress = pygame.image.load("images/presstostart.PNG")
backgroundPress_rect = backgroundPress.get_rect(topleft=(0, 0))


# Variable contenant le texte "1 player" en utilisant la police définit avant
text_player = smaller_font.render("1 player", True, "black")

"""
Une liste contenant des objets fantômes
L'avantage d'une liste par rapport à utiliser 4 objets différents est qu'il est beaucoup plus simple de manipuler les données
Exemple :
Si j'ai envie de mettre 30 fantômes, je n'ai que le range de ma boucle a modifié, tandis que si je créais chaque objet séparément j'aurais du créer
26 nouveaux objets
"""
ghostList = []

for i in range(4):
    ghostList.append(Ghost(195 + 15 * i, 150))

# run est sur true tant que le jeu tournera
run = True

# Crée une instance de la classe Player et la classe Points
player = Player()
pointt3 = Points()


# Image de la pacgomme valant 130 points
image130p = pygame.image.load("images/130p.png")
image130p_rect = image130p.get_rect()

# fonction permettant d'afficher la derniere pacgomme  
def lastscore():
    if pointt3.score == 1850:
        image130p_rect.x = 165
        image130p_rect.y = 255
        screen.blit(image130p, image130p_rect)

    if player.Netry_rect.x == image130p_rect.x and player.Netry_rect.y == image130p_rect.y:
        pointt3.score += 2000
        image130p_rect.x = -500
        image130p_rect.y = -500

# Score maximale pour gagner
scoreWin = 1980

# Va contenir le temps de démarrage et le temp de fin pour connaitre le temps écoulé durant la partie
starttime = 0
endtime = 0

# Contient le texte du temps écoulé
text_time = smaller_font.render(
    "timer : " + str(int(endtime - starttime)) + " s ", True, "black")

# Passe l'état sur "running" pour dire que le jeu est en train de tourner
state = "running"

# Stocke le temps actuel dans endtime
endTime = time.time()

while run:

    # Ce qu'il se passe quand la partie est en cours
    if state == "running":
        # On affiche le labyrinthe
        screen.blit(backgroundGame, (backgroundGame_rect))

        lastscore()

        # Affiche le score à l'écran
        textscore = smaller_font.render(
            "score : " + str(int(pointt3.score)) + " points", True, "black")
        screen.blit(textscore, (10, 58))

        # Vérifie si un point a été mangé et change sa position si c'est le cas
        pointt3.positionPoints(player)

        # Affiche les points sur l'écran
        screen.blit(pointt3.image55p, pointt3.image55p_rect)
        screen.blit(pointt3.image150p, pointt3.image150p_rect)

        # Affiche le temps écoulé et "player 1" à l'écran
        screen.blit(text_time, (330, 58))

        screen.blit(text_player, (200, 58))

        # Affiche netry à l'écran
        screen.blit(player.imageNetry, player.Netry_rect)

        # Modifie la position du joueur
        player.updatePos(backgroundGame)

        # for ghost in ghostList:
        # ghost.updatePos(backgroundGame)
        #screen.blit(ghost.imageGhost, ghost.Ghost_rect)
        # if ghost.Ghost_rect.x ==  player.Netry_rect.x and  ghost.Ghost_rect.y == player.Netry_rect.y:
        #state = "gameOver"

        # Actualise le temps écoulé depuis le début ainsi que le texte
        startTime = time.time() - endTime
        text_time = smaller_font.render(
            "timer : " + str(int(startTime)) + " s ", True, "black")

        # Pour chaque fantôme de présent dans la liste...
        for ghost in ghostList:
            # Actualise leur position et les affiche à l'écran
            ghost.updatePos(backgroundGame)
            screen.blit(ghost.imageGhost, ghost.Ghost_rect)

            # Puis si un fantôme touche netry, change l'état en gameover ou gameover0 en fonction du score
            if ghost.Ghost_rect.x == player.Netry_rect.x and ghost.Ghost_rect.y == player.Netry_rect.y:
                if pointt3.score > 0:
                    state = "gameOver"
                else:
                    state = "gameOver0"
        # Affiche l'écran d'introduction
        screen.blit(backgroundPress, (backgroundPress_rect))

    # Si on a perdu avec un score de 0
    if state == "gameOver0":
        # Affiche un game over avec le jeu en fond
        screen.blit(backgroundGame, (backgroundGame_rect))
        screen.blit(backgroundGameOver0, (backgroundGameOver0_rect))

        # Affiche le HUD en haut
        screen.blit(text_player, (200, 58))
        screen.blit(textscore, (10, 58))
        screen.blit(text_time, (330, 58))

    # Pareil qu'avant, mais cette fois notre score est plus grand que 0
    if state == "gameOver":
        screen.blit(backgroundGame, (backgroundGame_rect))
        for ghost in ghostList:
            ghost.updatePos(backgroundGame)
            screen.blit(ghost.imageGhost, ghost.Ghost_rect)
        screen.blit(backgroundGameOver, (backgroundGameOver_rect))
        screen.blit(text_player, (200, 58))
        screen.blit(textscore, (10, 58))
        screen.blit(text_time, (330, 58))

    # Si on gagne !
    if pointt3.score >= 1910:
        state = "win"
        screen.blit(backgroundGame, (backgroundGame_rect))
        screen.blit(text_player, (200, 58))
        screen.blit(text_time, (330, 58))
        textscore = smaller_font.render(
            "score : " + str(scoreWin) + " points", True, "black")
        screen.blit(textscore, (10, 58))
        screen.blit(player.imageNetry, player.Netry_rect)
        player.updatePos(backgroundGame)
        screen.blit(backgroundWin, (backgroundWin_rect))
        # Affiche le temps que ca nous a pris
        text_timeWin = medium_font.render(
            "TIME                                  " + str(int(startTime)) + " s ", True, "white")
        screen.blit(text_timeWin, (113, 230))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()


        #deplacement du personnage
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                backgroundPress_rect = backgroundPress.get_rect(  #actualise l'image de fond avant le personnage sinon : personnage invisible
                    center=(-500, -500))
                player.setDirection('R')
            if event.key == pygame.K_LEFT:
                backgroundPress_rect = backgroundPress.get_rect(
                    center=(-500, -500))
                player.setDirection('L')

            if event.key == pygame.K_UP:
                backgroundPress_rect = backgroundPress.get_rect(
                    center=(-500, -500))
                player.setDirection('U')

            if event.key == pygame.K_DOWN:
                backgroundPress_rect = backgroundPress.get_rect(
                    center=(-500, -500))
                player.setDirection('D')

    pygame.time.delay(200) 

    pygame.display.update()
