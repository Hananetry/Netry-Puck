"""
Projet Pacman, ici renommé par Netry Puck
fait par Hana Badreddine
Le jeu possède un menu composé d'une page crédit,
une page regle et une page jeu
"""

import pygame  # importation de la librairie pygame

pygame.init()  # initialise pygame

# crée une fenetre de 500 par 375 pixel
screen = pygame.display.set_mode((500, 375))
pygame.display.set_caption("Netry Puck")  # définie le titre de la fenetre

# importation d'une police d'écriture
main_font = pygame.font.Font("images/RetroGaming.ttf", 23)

# importation de l'image de fond du menu
background = pygame.image.load("images/background.jpg")
# définie le point d'ancrage de l'image
background_rect = background.get_rect(topleft=(0, 0))

# importation de l'image qui se superposera sur l'image de fond du menu
fuck = pygame.image.load("images/fuck.png")
# définie le point d'ancrage de l'image
fuck_rect = fuck.get_rect(topleft=(0, 0))

# importation de l'image de la premiere image de fond
GoMenubackground = pygame.image.load("images/GoMenu.png")
GoMenubackground_rect = GoMenubackground.get_rect(
    topleft=(0, 0))  # définie le point d'ancrage de l'image

icon = pygame.image.load("images/icon.png")  # importation de l'image icon
pygame.display.set_icon(icon)  # définie l'icon


class Button():  # debut de la classe
    # constructeur auquelle on passe 4 parametre (ses coordonnées x et y et le nom du bouton)
    def __init__(self, image, x_pos, y_pos, text_input):
        # Passe les paramètres dans des arguments pour les réutiliser dans la classe
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        # définie le point d'ancrage de l'image par les coordonées attitré dans les arguments
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        # Passe le paramètre dans un argument pour le réutiliser dans la classe
        self.text_input = text_input
        # definie le texte avec sa couleur
        self.text = main_font.render(self.text_input, True, "white")
        # définie le point d'ancrage du texte par les coordonées attitré dans les arguments
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):  # crée la méthode update
        screen.blit(self.image, self.rect)  # affiche l'image sur l'écran
        screen.blit(self.text, self.text_rect)  # affiche le texte sur l'écran

    def checkForInput(self, position):  # crée la méthode checkForInput
        # retourne la position de la souris ; tupple = (x,y); tupple[0]= x; tupple[1]=y
        return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)

    def changeColor(self, position):  # crée la méthode changeColor
        # si les coordonnées de la souris sont situé ou se trouve l'image
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(
                self.text_input, True, "black")  # le texte deviens noir
        else:
            # sinon le texte reste blanc
            self.text = main_font.render(self.text_input, True, "white")

    # def delete(self):


# importation de l'image des boutons
button_surface = pygame.image.load("images/button.png")


# objet permettant l'exécution de la classe bouton avec ses parametres
buttonStart = Button(button_surface, 250, 180, "Start Game")

buttonRules = Button(button_surface, 250, 235, "Game Rules")

buttonCredits = Button(button_surface, 250, 290, "Credits")

buttonReturn = Button(button_surface, 250, 315, "Return")


# importation de l'image du bouton caché
button_surface_for_p = pygame.image.load("images/p.jpg")
# objet permettant l'exécution de la classe bouton avec ses parametres
buttonP = Button(button_surface_for_p, 280, 68, "")

#buttonP_Retour = Button(button_surface_for_p, 280, 68,"")

# run est sur true tant que le jeu tournera
run = True
# Système "d'état", cette variable contient l'état dans lequel le jeu est (en train de jouer, dans x menu etc...)
state = "GoMenu"

# Boucle principal
while run:

    #Permet de parcourir les différents évènements qui se sont passées sur l'ordinateur (clic de souris, touche pressé)
    events = pygame.event.get()
    for event in events:
        # Si le joueur ferme la fenêtre avec la croix...
        if event.type == pygame.QUIT:
            #On stop pygame
            pygame.quit()
            # On arrête la boucle
            run = False
            # Et on ferme la fenêtre
            quit()

        # Change l'état si un bouton est cliqué
        if event.type == pygame.MOUSEBUTTONDOWN:

            if (state == "menu" or state == "menu_fuck") and buttonStart.checkForInput(pygame.mouse.get_pos()):
                state = "playing"

            if (state == "menu" or state == "menu_fuck") and buttonRules.checkForInput(pygame.mouse.get_pos()):
                state = "rules"

            if (state == "menu" or state == "menu_fuck") and buttonCredits.checkForInput(pygame.mouse.get_pos()):
                state = "credits"

            if (state == "rules" or state == "credits") and buttonReturn.checkForInput(pygame.mouse.get_pos()):
                state = "menu"

            if state == "menu" and buttonP.checkForInput(pygame.mouse.get_pos()):
                state = "menu_fuck"

            # if state == "menu" and buttonP_Retour.checkForInput(pygame.mouse.get_pos()):
                #state = "menu"

    # Efface le contenu à l'écran pour éviter d'avoir une superposition d'image
    screen.fill((255, 255, 255))

    # Les prochaines conditions permettent de customiser le menu en fonction de la variable state
    # Pour le menu principal
    if state == "menu":
        screen.blit(background, (background_rect))

        buttonStart.update()
        buttonStart.changeColor(pygame.mouse.get_pos())

        buttonRules.update()
        buttonRules.changeColor(pygame.mouse.get_pos())

        buttonCredits.update()
        buttonCredits.changeColor(pygame.mouse.get_pos())

        buttonP.update()

    # Pour l'easteregg si on presse sur le p
    if state == "menu_fuck":
        screen.blit(background, (background_rect))
        screen.blit(fuck, (fuck_rect))

        buttonStart.update()
        buttonStart.changeColor(pygame.mouse.get_pos())

        buttonRules.update()
        buttonRules.changeColor(pygame.mouse.get_pos())

        buttonCredits.update()
        buttonCredits.changeColor(pygame.mouse.get_pos())

        # buttonP_Retour.update()

    # La page des règles
    if state == "rules":

        # buttonCredits.delete()

        screen.blit(background, (background_rect))
        buttonReturn.update()
        buttonReturn.changeColor(pygame.mouse.get_pos())

        imageRules = pygame.image.load("images/rule.png")
        imageRules_rect = imageRules.get_rect(topleft=(130, 155))
        screen.blit(imageRules, (imageRules_rect))

    # La page des crédits
    if state == "credits":
        screen.blit(background, (background_rect))
        buttonReturn.update()
        buttonReturn.changeColor(pygame.mouse.get_pos())

        imageCredits = pygame.image.load("images/credits.png")
        imageCredits_rect = imageCredits.get_rect(topleft=(130, 155))
        screen.blit(imageCredits, (imageCredits_rect))

    # Permet de démarrer le jeu
    if state == "playing":
        import game

    # Le menu d'acceuil
    if state == "GoMenu":
        screen.blit(GoMenubackground, (GoMenubackground_rect))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = "menu"

    # Permet rafraichir la fenêtre
    pygame.display.update()
