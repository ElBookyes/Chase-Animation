import pygame, sys
from pygame.locals import*

pygame.init()
WHITE = (255, 255, 255)
DISPLAYSURF = pygame.display.set_mode((1600, 1000))
pygame.display.set_caption("Dog and Cat chase !")
CatImg = pygame.image.load("cat running yes.png")
DogImg = pygame.image.load("dog runs yes.png")
CatImg1 = pygame.image.load("cat running yes.png")
DogImg1 = pygame.image.load("dog runs yes.png")
MirrorCatImg = pygame.image.load("rightrunning cat.jpg")
MirrorDogImg = pygame.image.load("rightrunning dog.png")
catX = 1100
catY = 300
dogX = 1500
dogY = 300

Catdirection = "left"
Dogdirection = "left"

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(CatImg, (catX, catY))
    DISPLAYSURF.blit(DogImg, (dogX, dogY))

    if Catdirection == "left":
        catX -= 2
        if catX == 100:
            Catdirection = "down"
    if Dogdirection == "left":
        dogX -= 2
        if dogX == 100:
            Dogdirection = "down"
    if Catdirection == "down":
        catY += 2
        if catY == 700:
            Catdirection = "right"
    if Dogdirection == "down":
        dogY += 2
        if dogY == 800:
            Dogdirection = "right"
    if Catdirection == "right":
        CatImg = MirrorCatImg
        catX += 2
        if catX == 1300:
            Catdirection = "up"
    if Dogdirection == "right":
        DogImg = MirrorDogImg
        dogX += 2
        if dogX == 1300:
            Dogdirection = "up"
    if Catdirection == "up":
        catY -= 2
        if catY == 100:
            Catdirection = "left"
            CatImg = CatImg1
    if Dogdirection == "up":
        dogY -= 2
        if dogY == 100:
            Dogdirection = "left"
            DogImg = DogImg1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            sys.exit()

    pygame.display.update()





