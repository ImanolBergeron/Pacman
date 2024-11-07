import pygame, sys, copy
import random
from pygame import mixer
from time import sleep
clock = pygame.time.Clock()
pygame.init()
mixer.init()
mixer.music.load("Images/PacManTheme.mp3")
mixer.music.set_volume(0.7)
color = (40,40,40)
pygame.display.set_caption('PACMAN')
screen = pygame.display.set_mode((1625,980))
fond = pygame.image.load("Images/FondMap1.jpg").convert()
piece = pygame.image.load("Images/PieceDor.png").convert_alpha()
piece = pygame.transform.scale(piece,(35,35))
Gpiece = pygame.image.load("Images/Grosspiece.png").convert_alpha()
Gpiece = pygame.transform.scale(Gpiece,(35,35))
fantome1 = pygame.image.load("Images/Fantome1.png").convert_alpha()
fantome2 = pygame.image.load("Images/Fantome2.png").convert_alpha()
fantome3 = pygame.image.load("Images/Fantome3.png").convert_alpha()
fantome4 = pygame.image.load("Images/Fantome4.png").convert_alpha()
fantome5 = pygame.image.load("Images/Fantome5.png").convert_alpha()
fantome1 = pygame.transform.scale(fantome1, (35,35))
fantome2 = pygame.transform.scale(fantome2, (35,35))
fantome3 = pygame.transform.scale(fantome3, (35,35))
fantome4 = pygame.transform.scale(fantome4, (35,35))
fantome5 = pygame.transform.scale(fantome5, (35,35))
balle = pygame.image.load("Images/balle.jpg").convert_alpha()
balle = pygame.transform.scale(balle,(35,35))
GmOv = pygame.image.load("Images/GameOver.jpg").convert_alpha()
luigi = pygame.image.load("Images/Luigi.png").convert_alpha()
Life = pygame.image.load("Images/Fullvie.png").convert_alpha()
Lifedeux = pygame.image.load("Images/2tiersvies.png").convert_alpha()
Lifeun = pygame.image.load("Images/1tiersVie.png").convert_alpha()
Lifezero = pygame.image.load("Images/nolife.png").convert_alpha()
Life = pygame.transform.scale(Life,(400,200))
Lifedeux = pygame.transform.scale(Lifedeux,(400,200))
Lifeun = pygame.transform.scale(Lifeun,(400,200))
Lifezero = pygame.transform.scale(Lifezero,(400,200))
BtnPlay = pygame.image.load("Images/Play.png").convert_alpha()
BtnRestart = pygame.image.load("Images/restart.png").convert_alpha()
BtnExit = pygame.image.load("Images/Exit.png").convert_alpha()
Mnscr = pygame.image.load("Images/Mainscreen.png").convert_alpha()
Mnscr = pygame.transform.scale(Mnscr,(1625,980))
luigi = pygame.transform.scale(luigi, (35,35))
piece = pygame.transform.scale(piece, (35,35))
screen.blit(fond,(0,0))

mapp =    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 6, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 6, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1,'A', 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0,1, 1, 1 ,1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 6, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 6, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 0, 1, 1, 6, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 'B', 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
           [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [7, 0, 1, 'C', 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 7],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 33, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0,1],
           [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
           [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 6, 1, 0, 1, 1, 0, 0, 0, 1, 1],
           [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
           [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 'D', 0, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 6, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 0, 0, 0, 1, 6, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 6, 1, 0, 1],
           [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 3, 0, 0, 'E', 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
           [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
           
           

def Jeu(MAP,nom):
    """
fonction principale du jeu s'occupant de la boucle pygame
et gérant les appellantions successives veillant au fonctionnement du jeu
    """
    MAPP = copy.deepcopy(MAP)
    nom , ScrMax = RchScore(nom)
    font = pygame.font.Font('freesansbold.ttf', 40)
    pseudo = font.render(str(nom),1,(199, 21, 133))
    ScrTotal = 0
    mixer.music.play(-1)
    apparition_piece(MAPP)
    affichemap(MAPP) 
    vies = 3
    liste = [['A','haut'],['B','droite'],['C','haut'],['D','haut'],['E','bas']]
    pygame.display.flip()
    run = True
    first = False
    while run == True:
        MAPP = TestMAP(MAPP)
        sleep(0.2)
        
        afficheScore(ScrMax,ScrTotal,pseudo)
        if vies >=0:
            SvVies = vies
            for fantome in liste:
                n,d = fantome
                fantome[1],vies = déplacementF(MAPP,d,n,vies)
                affichageVie(vies)
                afficheScore(ScrMax,ScrTotal,pseudo)
                pygame.display.flip()
            if SvVies != vies:
                x,y = 14,15
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    mixer.music.stop()
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        Direction = 'haut'
                        first = True
                    if event.key == pygame.K_DOWN:
                        Direction = 'bas'
                        first = True
                    if event.key == pygame.K_LEFT:
                        Direction = 'gauche'
                        first = True
                    if event.key == pygame.K_RIGHT:
                        Direction = 'droite'
                        first = True
            if first == True:
                vies,ScrTotal = déplacement(MAPP,Direction,ScrTotal,ScrMax,vies,pseudo,nom)
                affichageVie(vies)
                afficheScore(ScrMax,ScrTotal,pseudo)
                pygame.display.flip()
        else:
            PartiePerdue(nom,ScrTotal)
            rejouer(nom)

def Start():
    """
affiche l'écrant de début et un bouton et lance
le jeu si la fonction détecte un clic de souris sur
le bouton
    """
    screen.blit(Mnscr,(0,0))
    screen.blit(BtnPlay,(700,700))
    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                mixer.music.stop()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    x,y = pygame.mouse.get_pos()
                    if x > 700 and x < 1200and y > 700 and y < 931:
                        nom = Username()
                        screen.blit(fond,(0,0))
                        Jeu(mapp,nom)
    
def rejouer(nom):
    """
à la fin du jeu affiche de bouton un pour relancer une
partie, et qui conserve le pseudo du joueur et l'autre pour
quitter et fermer le jeu
    """
    screen.blit(BtnRestart,(587.5,700))
    screen.blit(BtnExit,(587.5,780))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            mixer.music.stop()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed():
                x,y = pygame.mouse.get_pos()
                if x > 587.5 and x < 812.5 and y > 700 and y < 771:
                    Jeu(mapp,nom)
                if x > 587.5 and x < 812.5 and y > 780 and y < 851:
                    pygame.display.quit()
                    mixer.music.stop()
                    sys.exit()
                    
                      
    

def affichemap(mappy):
    """
affiche les murs,les fantomes et le joueur sur
la carte
    """
    for ligne in range(len(mappy)):
        for colone in range(len(mappy[ligne])):
            if mappy[ligne][colone] == 1:
                pygame.draw.rect(screen, color, pygame.Rect(35*colone,35*ligne,35,35))
            elif mappy[ligne][colone] == 'A':
                screen.blit(fantome1,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 'B':
                screen.blit(fantome2,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 'C':
                screen.blit(fantome3,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 'D':
                screen.blit(fantome4,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 'E':
                screen.blit(fantome5,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 5:
                screen.blit(piece,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 6:
                screen.blit(Gpiece,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 2:
                screen.blit(luigi,(colone*35,ligne*35))
            elif mappy[ligne][colone] == 33:
                screen.blit(balle,(colone*35,ligne*35))
    pygame.display.flip()
    
def déplacement(MAP,Direction,ScrTotal,ScrMax,vies,pseudo,nom):
    """
gère les différents déplacements du joueur, s'occupe aussi
du calcul du score et gère les collision avec les fantomes
donc les morts
    """
    x,y = position_joueur(MAP)
    Lif = False
    Mort = False
    if Direction == 'haut':
        if MAP[x-1][y] != 1:
            if MAP[x-1][y] == 5:
                ScrTotal += 20
            elif MAP[x-1][y] == 6:
                ScrTotal += 200
            elif MAP[x-1][y] is str :
                vies -= 1
                Mort = True
            elif MAP[x-1][y] == 10:
                ScrTotal += 400
            if Mort == True:
                MAP[x][y] = 0
                MAP[14][15] = 2
                x,y = 14,15
                Mort = False
                Lif = True
            else:
                MAP[x][y] = 0
                MAP[x-1][y] = 2
                x = x-1
                
            screen.blit(fond,(0,0))
            afficheScore(ScrMax,ScrTotal,pseudo)
            affichageVie(vies)
            affichemap(MAP)
            if Lif == True :
                Lif = False
                return vies,ScrTotal
        return vies,ScrTotal
    if Direction == 'bas':
        if MAP[x+1][y] != 1:
            if MAP[x+1][y] == 5:
                ScrTotal +=20
            elif MAP[x+1][y] == 6:
                ScrTotal += 200
            elif MAP[x+1][y] is str :
                vies -= 1
                Mort = True
            elif MAP[x+1][y] == 10:
                ScrTotal += 400
            if Mort == True:
                MAP[x][y] = 0
                MAP[14][15] = 2
                x,y = 14,15
                Mort = False
                Lif = True
            else:
                MAP[x][y] = 0
                MAP[x+1][y] = 2
                x = x+1 
            screen.blit(fond,(0,0))
            afficheScore(ScrMax,ScrTotal,pseudo)
            affichageVie(vies)
            affichemap(MAP)
            if Lif == True :
                Lif = False
                return vies,ScrTotal
        return vies,ScrTotal
    if Direction == 'gauche':
        if y-1 > -1 and MAP[x][y-1] != 1:
            if MAP[x][y-1] == 5:
                ScrTotal += 20
            elif MAP[x][y-1] == 6:
                ScrTotal += 200
            elif MAP[x][y-1] is str  : 
                vies -= 1
                Mort = True
            elif MAP[x][y-1] == 10:
                ScrTotal += 400
            if Mort == True:
                MAP[x][y] = 0
                MAP[14][15] = 2
                x,y = 14,15
                Mort = False
                Lif = True
            else:
                MAP[x][y] = 0
                MAP[x][y-1] = 2
                y = y-1
            screen.blit(fond,(0,0))
            afficheScore(ScrMax,ScrTotal,pseudo)
            affichageVie(vies)
            affichemap(MAP)
            if Lif == True :
                Lif = False
                return vies,ScrTotal
        if y-1 == -1:
            MAP[x][y] = 0
            MAP[x][34] = 2
            y = 34
            screen.blit(fond,(0,0))
            afficheScore(ScrMax,ScrTotal,pseudo)
            affichageVie(vies)
            affichemap(MAP)
        return vies,ScrTotal
    if Direction == 'droite':
        if y +1 < 35 and MAP[x][y+1] != 1 : 
            if MAP[x][y+1] == 5:
                ScrTotal += 20
            elif MAP[x][y+1] == 6:
                ScrTotal += 200
            elif MAP[x][y+1] is str :
                vies -= 1
                Mort = True
            elif MAP[x][y+1] == 10:
                ScrTotal += 400
            if Mort == True:
                MAP[x][y] = 0
                MAP[14][15] = 2
                x,y = 14,15
                Mort = False
                Lif = True
            else:
                MAP[x][y] = 0
                MAP[x][y+1] = 2
                y = y+1
            screen.blit(fond,(0,0))
            afficheScore(ScrMax,ScrTotal,pseudo)
            affichageVie(vies)
            affichemap(MAP)
            if Lif == True :
                Lif = False
                return vies,ScrTotal     
        if y+1 == 35:
            MAP[x][y] = 0
            MAP[x][0] = 2
            y = 0
            screen.blit(fond,(0,0))
            afficheScore(ScrMax,ScrTotal,pseudo)
            affichageVie(vies)
            affichemap(MAP)
        return vies,ScrTotal
    
    
def déplacementF(MAP,d,n,vies):
    """
gère les déplacements des fantomes
    """
    L = []
    if d == "haut":
        a,b = position_fantome(MAP,n)
        if MAP[a-1][b] == 2:
            MAP[a-1][b] = 0
            vies = vies-1  
        h = MAP[a-1][b]
        MAP[a-1][b] = n
        MAP[a][b] = h
        a,b = position_fantome(MAP,n)
        if MAP[a-1][b] != 1 and a-1 > 0:
            L.append("haut")
        if MAP[a][b-1] != 1:
            L.append("gauche")
        if MAP[a][b+1] != 1:
            L.append("droite")
        if L ==[]:
            L.append("bas")
    elif d == "bas":
        a,b = position_fantome(MAP,n)
        if MAP[a+1][b] == 2:
            MAP[a+1][b] = 0
            vies = vies-1
        h = MAP[a+1][b]
        MAP[a+1][b] = n
        MAP[a][b] = h
        a,b = position_fantome(MAP,n)
        if MAP[a+1][b] != 1 and a +1 < 27:
            L.append("bas")
        if MAP[a][b-1] != 1:
            L.append("gauche")
        if MAP[a][b+1] != 1:
            L.append("droite")
        if L == []:
            L.append("haut")
    elif d == "gauche" :
        a,b = position_fantome(MAP,n)
        if MAP[a][b-1] == 2:
            MAP[a][b-1] = 0
            vies = vies-1
        if b-1 == -1:
            MAP[a][b] = 0 
            MAP[a][33] = n
            b = 33
        else :
            h = MAP[a][b-1]
            MAP[a][b-1] = n
            MAP[a][b] = h
        a,b = position_fantome(MAP,n)
        if MAP[a+1][b] != 1:
            L.append("bas")
        if MAP[a][b-1] != 1 and b-1 > 0:
            L.append("gauche")
        if MAP[a-1][b] != 1:
            L.append("haut")
        if L == []:
            L.append("droite")
    elif d == "droite":
        a,b = position_fantome(MAP,n)
        if MAP[a][b+1] == 2:
            MAP[a][b+1] = 0
            vies = vies-1
        if b+1 == 34:
            MAP[a][b] = 0
            MAP[a][0] = n
            b = 0
        else : 
            h = MAP[a][b+1]
            MAP[a][b+1] = n
            MAP[a][b] = h
        a,b = position_fantome(MAP,n)
        if MAP[a+1][b] != 1:
            L.append("bas")
        if MAP[a][b+1] != 1 and b+1 < 34:
            L.append("droite")
        if MAP[a-1][b] != 1:
            L.append("haut")
        if L == []:
            L.append("gauche")
    d = random.choice(L)
    screen.blit(fond,(0,0))
    affichemap(MAP)
    return d,vies 

def affichageVie(vies):
    """
affiche la barre de vie en bas
a droite de l'écran , la barre évolue en
fonction du vnombre de vies
    """
    font = pygame.font.Font('freesansbold.ttf', 80)
    V = str(vies)+"x"
    if vies == 3:
        screen.blit(Life,(1250,700))
    if vies == 2: 
        screen.blit(Lifedeux,(1250,700))
    if vies == 1:
        screen.blit(Lifeun,(1250,700))
    if vies == 0:
        screen.blit(Lifezero,(1250,700))

def TestMAP(MAP):
    """
regarde la map, s'il reste des pieces ou des grosses pièces
dessus , renvoie la carte sinon réinitialise la carte
    """
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] == 5 or MAP[i][j] == 6:
                return MAP
    MAP = copy.deepcopy(mapp)
    MAP = apparition_piece(MAP)
    return MAP

def apparition_piece(mape):
    """
    remplace les 0 de la matrice par des 5
    ce qui correspond à des pièces
    """
    for i in range(len(mape)):
        for j in range(len(mape[i])):
            if mape[i][j] == 0:
                mape[i][j] = 5
    return mape
def position_joueur(MAP):
    """
    regarde la map et cherche la position du joueur
    qui est 2 dans la matrice MAP
    s'il n'est pas trouvé donc qu'il est mort , le met
    à ses coordonées initiales
    """
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] == 2:
                return i,j
    if 2 not in MAP:
        i,j = 14,15
        return i,j
            
def position_fantome(MAP,n):
    """
vérifie les positions des fantomes à chaque
déplacements, s'il ne sont pas sur la carte donc manger,
les remets à leur positions initiales
    """
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] == n:
                return i,j
    if n not in MAP:
        if n == 'A':
            return 5,4
        if n == 'B':
            return 9,24
        if n == 'C':
            return 3,13
        if n == 'D':
            return 26,19
        if n == 'E':
            return 16,23

                
            
def RchScore(nom):
    """
    Demande le nom du joueur afin de voir s'il a déjà joué,
    si oui nous retourne son meilleur score.
    """            
    with open('Scores.txt','r')as fichier:
       raw = fichier.read()
    joueurs=raw.split('\n')
    for i in range(len(joueurs)):
        joueurs[i]=joueurs[i].split(',')
        if joueurs[i][0]== nom:
            return nom,int(joueurs[i][1])
    return nom ,0

def afficheScore(ScrMax,ScrTotal,pseudo):
    """
    compare le score max du joueur et le score actuel et affiche
    le score max et actuel si jamais le score actuel est plus grand
    que le meilleur score remplace le score max par l'actuel
    """
    font = pygame.font.Font('freesansbold.ttf', 80)
    Name = font.render('PACMAN',1,(0, 204, 203))
    
    if ScrMax < ScrTotal:
        ScrMax = ScrTotal
    ScrMaxx = font.render(str(ScrMax),1,(0, 204, 203))
    Scr = font.render(str(ScrTotal),1,(199, 21, 133))
    screen.blit(Name,(1230,30))
    screen.blit(ScrMaxx,(1300,330))
    screen.blit(Scr,(1300,430))
    screen.blit(pseudo,(1240,230))

def SauvegardeScore(nom,ScrTotal):
    """
    Sauvegarde le score du joueur
    si jamais c'est un nouveau joueur
    cré un élément à son nom, si c'est un ancien 
    conserve l'ancien meilleur score.
    """
    saved=False
    with open('Scores.txt','r')as fichier:
        raw = fichier.read()
    joueurs=raw.split('\n')
    for i in range(len(joueurs)):
        joueurs[i]=joueurs[i].split(',')
        if joueurs[i][0]== nom:
            if int(joueurs[i][1]) < ScrTotal:
                joueurs[i][1]= ScrTotal
            saved=True
            
    if not saved:
        joueurs.append([nom,ScrTotal])
    raw =""
    for joueur in joueurs:

        raw = raw +",".join(str(v) for v in joueur)+'\n'
    raw = raw[0:-1]
    with open('Scores.txt','w')as fichier:
        fichier.write(raw)


def Username():
    """
    cré une case permettant d'insérer le nom du
    joueur ne pouvant pas dépasser les
    12 charactères
    """
    font = pygame.font.Font('freesansbold.ttf', 80)
    input_box = pygame.Rect(550,300,550,90)
    color_inactive = pygame.Color((199, 21, 133))
    color_active = pygame.Color((255, 127, 0))
    color = color_inactive
    txt = font.render('Votre nom : ',1,(0, 204, 203))
    active = False
    username = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return username
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if len(username) < 10 :
                            username += event.unicode
                        else:
                            pass                       
        screen.blit(fond,(0,0))
        screen.blit(txt,(600,200))
        txt_surface = font.render(username, True, color)
        width = max(550, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)


def PartiePerdue(nom,ScrTotal):
    """
appelé lorsque le joueur n'a plus de vies et meurs encore un
fois , affiche à l'écran 'Game Over' et sauvegarde
le score
    """
    screen.blit(GmOv,(200,50))
    pygame.display.flip()
    SauvegardeScore(nom,ScrTotal)
 

if __name__ == '__main__':
    Start()
