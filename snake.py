# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True

direction = (1, 0)
fruit = (10, 10)

def col_pos(a,color = (255, 0, 0)):
    for c in a:
        x = 20*c[0] # coordonnée x (colonnes) en pixels
        y = 20*c[1] # coordonnée y (lignes) en pixels
        width = 20 # largeur du rectangle en pixels
        height = 20 # hauteur du rectangle en pixels
        rect = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, color, rect)

def move(sn,dir):
    head=(sn[0][0] + dir[0], sn[0][1] + dir[1])
    sn=[head]+sn[:-1]
    return sn

snake = [
    (10, 15),
    (11, 15),
    (12, 15),]

while running:
    screen.fill((255,255,255))
    for i in range(30):
        for j in range(30):
            if (i+j)%2==1:
                x = 20*i # coordonnée x (colonnes) en pixels
                y = 20*j # coordonnée y (lignes) en pixels
                width = 20 # largeur du rectangle en pixels
                height = 20 # hauteur du rectangle en pixels
                rect = pg.Rect(x, y, width, height)
                # appel à la méthode draw.rect()
                color = (0, 0, 0)
                pg.draw.rect(screen, color, rect)
    
    col_pos(snake)

    pg.display.update()
    clock.tick(5)
    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_UP and direction!=(0,1):
                direction= (0,-1)
            if event.key == pg.K_DOWN and direction!=(0,-1):
                direction= (0,1)
            if event.key == pg.K_LEFT and direction!=(1,0):
                direction= (-1,0)
            if event.key == pg.K_RIGHT and direction!=(1,0):
                direction= (1,0)
    snake=move(snake,direction)
# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()