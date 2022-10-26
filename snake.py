# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

from random import randint, random
import pygame as pg
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--larg',type=int)
parser.add_argument('--haut',type=int)
parser.add_argument('--taille',type=int)
args = parser.parse_args()
larg=args.larg
haut=args.haut
taille=args.taille
if type(larg)!=int:
    larg=30
if type(haut)!=int:
    haut=30
if type(taille)!=int:
    taille=20

pg.init()
screen = pg.display.set_mode((larg*taille, haut*taille))
clock = pg.time.Clock()



running = True

direction = (1, 0)
fruit = (3, 3)
score=0
snake = [
    (3, 0),
    (2, 0),
    (1, 0),]
lost=False

def col_pos(a,color = (255, 0, 0)):
    for c in a:
        x = taille*c[0] # coordonnée x (colonnes) en pixels
        y = taille*c[1] # coordonnée y (lignes) en pixels
        width = taille # largeur du rectangle en pixels
        height = taille # hauteur du rectangle en pixels
        rect = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, color, rect)

def move(sn,dir):
    head=(sn[0][0] + dir[0], sn[0][1] + dir[1])
    tail=sn[-1]
    sn=[head]+sn[:-1]
    return sn,tail

def eat(sn,fr,tail,sc):
    if sn[0]==fr:
        sn.append(tail)
        sc+=1
        while True:
            fr=(randint(0,larg-1),randint(0,haut-1))
            if fr not in sn:
                break
        return fr,sc
    return fr,sc

def lose(sn):
    if (sn[0] in sn[1:]) or (sn[0][0]<0 or sn[0][0]>larg-1 or sn[0][1]<0 or sn[0][1]>haut-1):
        return True
    return False



while running:
    if lost==False:
        screen.fill((255,255,255))
        for i in range(larg):
            for j in range(haut):
                if (i+j)%2==1:
                    x = taille*i # coordonnée x (colonnes) en pixels
                    y = taille*j # coordonnée y (lignes) en pixels
                    width = taille # largeur du rectangle en pixels
                    height = taille # hauteur du rectangle en pixels
                    rect = pg.Rect(x, y, width, height)
                    
                    color = (0, 0, 0)
                    pg.draw.rect(screen, color, rect)
        
        col_pos(snake)  #colorie le snake
        
        col_pos([snake[0]],(0,0,255))   #optionel, colorie la tete du snake

        col_pos([fruit],(255,128,0))        #colorie le fruit
        pg.display.update()
        clock.tick(5)
        lost=lose(snake)
        
    else:
        pg.display.set_caption(f"Score: {score}")
    
    
    p=False   #quand on appuie sur deux touches rapidement on peut faire un demi tour, d'ou l'utilite de cette variable
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == pg.KEYDOWN:
            
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_UP and direction!=(0,1) and p==False:
                direction= (0,-1)
                p=True
            if event.key == pg.K_DOWN and direction!=(0,-1) and p==False:
                direction= (0,1)
                p=True
            if event.key == pg.K_LEFT and direction!=(1,0) and p==False:
                direction= (-1,0)
                p=True
            if event.key == pg.K_RIGHT and direction!=(-1,0) and p==False:
                direction= (1,0)
                p=True
            if lost==True and event.key== pg.K_r:
                lost =False
                direction = (1, 0)
                fruit = (3, 3)
                score=0
                snake = [
                    (1, 0),
                    (0, 0),
                    (-1, 0),]

    snake,tail=move(snake,direction)
    fruit,score=eat(snake,fruit,tail,score)


pg.quit()