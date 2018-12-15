import pygame
from pygame.locals import *
import time
import math
from plateau import *
pygame.init()

def timer(depart):
    if depart == 0:
        tmps = 0
    else:
        tmps = math.floor(time.perf_counter())- depart
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    fontObj = pygame.font.Font('freesansbold.ttf',35)
    texteSurface = fontObj.render(str(tmps),True,BLACK,WHITE)
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (500,0)
    ecran.blit(texteSurface,texteRect)
    pygame.display.update()

def selectionD(perso,x,y):
    if perso == 1:
        ecran.blit(perso_bas,(x,y))
    elif perso == 2:
        ecran.blit(perso_haut,(x,y))
    elif perso == 3:
        ecran.blit(perso_droite,(x,y))
    elif perso == 4:
        ecran.blit(perso_gauche,(x,y))

def selectionM(ennemi,m_x,m_y):
    if ennemi == 1:
        ecran.blit(mario,(m_x,m_y))
    elif ennemi == 2:
        ecran.blit(mario_ht_bs,(m_x,m_y))
    elif ennemi == 3:
        ecran.blit(mario_drt,(m_x,m_y))
    elif  ennemi == 4:
        ecran.blit(mario_gch,(m_x,m_y))

def display(depart,x,y,perso,numTab,m_y,m_x,ennemi):
    ecran.blit(pygame.transform.scale(fond, resolution), (0, 0))
    abs = 0
    ordo = 0
    for ligne in board[numTab]:
        for case in ligne:
            if case== 1:
                ecran.blit(mur,(abs,ordo))
            if case== 2:
                ecran.blit(echelle,(abs,ordo))
            abs+=40
        abs=0
        ordo+=40
    ecran.blit(arriveM,(0,0))
    ecran.blit(arriveD,(760,800))
    ecran.blit(pygame.transform.scale(b_bouton, (100,35)), (600, 0))
    selectionM(ennemi,m_x,m_y)
    selectionD(perso,x,y)
    timer(depart)
    pygame.display.update()

def new(depart,play,x,y,niv,m_x,m_y):
    depart = 0
    play,niv = False,False
    x,y,m_x,m_y= 0,0,760,800
    return depart,play,x,y,niv,m_x,m_y

def move(event,board,x,y,perso,numTab,m_y,m_x,ennemi):
    vitesse=40
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            if y < 800:
                y+= vitesse
                if board[numTab][(y+39)//40][x//40] == 1 or board[numTab][(y+39)//40][(x+39)//40] == 1 :
                    y-= vitesse
                else:
                    perso = 2
        if event.key == K_UP:
            if y > 0:
                y-= vitesse
                if board[numTab][(y//40)][x//40] == 1 or board[numTab][(y//40)][(x+39)//40] == 1:
                    y+= vitesse
                else:
                    perso = 2
        if event.key == K_RIGHT:
            if x < 760:
                x+= vitesse
                if board[numTab][(y//40)][(x+39)//40] == 1 or board[numTab][((y+39)//40)][(x+39)//40] == 1:
                    x-= vitesse
                else:
                    perso = 3
        if event.key == K_LEFT:
            if x > 0:
                x-=vitesse
                if board[numTab][(y//40)][x//40] == 1 or board[numTab][((y+39)//40)][x//40] == 1:
                    x+= vitesse
                else:
                    perso = 4
        if event.key == K_z:
            if m_y < 800:
                m_y+= vitesse
                if board[numTab][(m_y+39)//40][m_x//40] == 1 or board[numTab][(m_y+39)//40][(m_x+39)//40] == 1 :
                    m_y-= vitesse
                else:
                    ennemi = 2
        if event.key == K_s:
            if m_y > 0:
                m_y-= vitesse
                if board[numTab][(m_y//40)][m_x//40] == 1 or board[numTab][(m_y//40)][(m_x+39)//40] == 1:
                    m_y+= vitesse
                else:
                    ennemi = 2

        if event.key == K_d:
            if m_x < 760:
                m_x+= vitesse
                if board[numTab][(m_y//40)][(m_x+39)//40] == 1 or board[numTab][((m_y+39)//40)][(m_x+39)//40] == 1:
                    m_x-= vitesse
                else:
                    ennemi = 3
        if event.key == K_a:
            if m_x > 0:
                m_x-=vitesse
                if board[numTab][(m_y//40)][m_x//40] == 1 or board[numTab][((m_y+39)//40)][m_x//40] == 1:
                    m_x+= vitesse
                else:
                    ennemi = 4

    return x,y,perso,m_y,m_x,ennemi

def verif (x,y,m_x,m_y):
    print(m_x,m_y)
    if x == 760 and y == 800:
        winD = pygame.image.load("resultD.png")
        ecran.blit(pygame.transform.scale(winD, resolution), (0, 0))
        return True
    elif m_x == 0 and m_y == 0:
        winM = pygame.image.load("resultM.png")
        ecran.blit(pygame.transform.scale(winM, resolution), (0, 0))
        return True
    elif m_x == x and m_y == y:
        winE = pygame.image.load("resultE.png")
        ecran.blit(pygame.transform.scale(winE, resolution), (0, 0))
        return True
    return False

# Réglage paramètres
resolution = (800,840)
ecran = pygame.display.set_mode(resolution)
pygame.display.set_caption('DK')
fond = pygame.image.load("fond.jpg")
icone = pygame.image.load("icone.jpg")
pygame.display.set_icon(icone)
ecran.blit(pygame.transform.scale(fond, resolution), (0, 0))

# Chargement images
mur = pygame.image.load("mur.png")
start = pygame.image.load("depart.png")
perso_bas = pygame.image.load("dk_bas.png")
perso_haut = pygame.image.load("dk_haut.png")
perso_gauche = pygame.image.load("dk_gauche.png")
perso_droite = pygame.image.load("dk_droite.png")
arriveD = pygame.image.load("arrivee.png")
arriveM = pygame.image.load("champi.jpg.png")
b_bouton = pygame.image.load("bouton.png")
echelle = pygame.image.load("echelle.png")
accueil = pygame.image.load("accueil.png")
mario = pygame.image.load("mario.jpg.png")
mario_ht_bs= pygame.image.load("mario_ht_bs.jpg.png")
mario_drt = pygame.image.load("mario_drt.jpg.png")
mario_gch = pygame.image.load("mario_gch.png")


#Déclaration des variables
board = [tableau_a,tableau_b]
x, y, depart, niv, play, perso,ennemi,numTab = 0, 0, 0, False, False, 1,1,0
poseX,poseY = 0 ,0
m_x,m_y=760,800
continu = True

while continu:
    # Bouton start
    while niv == False:
        ecran.blit(pygame.transform.scale(accueil, resolution), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    niv = True
                    numTab = 0
                if event.key == K_F2:
                    niv = True
                    numTab = 1
    display(depart,x,y,perso,numTab,m_y,m_x,ennemi)
    while play == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONUP:
                poseX, poseY = event.pos
                print(poseX,poseY)
        if poseX > 599 and poseX <701:
            if poseY > -1 and poseY <36:
                play = True
        #On démarre le chrono
        depart = math.floor(time.perf_counter())
    for event in pygame.event.get():
        if event.type == QUIT:
            continu = False
        x, y, perso,m_y,m_x,ennemi = move(event,board,x,y,perso,numTab,m_y,m_x,ennemi)
    if verif(x,y,m_x,m_y):
        pygame.display.update()
        part = False
        while part == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONUP:
                    poseX,poseY = event.pos
                    print(poseX,poseY)
                    if poseX<560 and poseX>280:
                        if poseY<380 and poseY>270:
                            depart,play,x,y,niv,m_x,m_y = new(depart,play,x,y,niv,m_x,m_y)
                            display(depart,x,y,perso,numTab,m_y,m_x,ennemi)
                            part = True
                    elif poseX<560 and poseX>270:
                        print('quit')
                        if poseY<650 and poseY>560:
                            print('quit')
                            continu = False
                            part = True

    else:
        display(depart,x,y,perso,numTab,m_y,m_x,ennemi)
pygame.quit()
