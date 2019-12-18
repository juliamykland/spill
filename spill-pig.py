import pygame
from pylab import *
import random
import time
pygame.init()
random.seed(1)
pygame.mixer.init()

#variabler
white = (255,255,255)
red = ((255,0,0))
svart = ((0, 0, 0))
bredde = 1200
hoyde = 700
spillerbredde = 100
spillerhoyde = 70
redballbredde = 40
redballhoyde = 40
poeng = 0
font = pygame.font.SysFont("comicsansms", 50)
clock = pygame.time.Clock()
greenballbredde = 40
greenballhoyde = 40
blueballbredde = 50
blueballhoyde = 50


size = (bredde,hoyde)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")   
done = False


bg = pygame.image.load("bg.png")
bg_tilpasset = pygame.transform.scale(bg,(size))
screen.blit(bg_tilpasset, (0, 0))


spiller = pygame.image.load("pig.png")
spiller_size = pygame.transform.scale(spiller, (spillerbredde,spillerhoyde))
spillerx = 300
spillery = 300
dx = dy = 30
screen.blit(spiller_size, (spillerx, spillery))

redball = pygame.image.load("red.png")
redball_size = pygame.transform.scale(redball, (redballbredde, redballhoyde))
redx = randint(10, bredde-10)
redy = randint (10, hoyde-10)
drx=10
dry=10

screen.blit(redball_size, (redx, redy))

greenball = pygame.image.load("green.png")
greenball_size = pygame.transform.scale(greenball, (greenballbredde, greenballhoyde))
greenx = randint (15, bredde-15)
greeny = randint (15, hoyde-15)
dgx = 15
dgy = 15
screen.blit(greenball_size, (dgx, dgy))

blueball = pygame.image.load("blue.png")
blueball_size = pygame.transform.scale(blueball, (blueballbredde, blueballhoyde))
bluex = 400
bluey = 500
dbx = 20
dby = 20
screen.blit(blueball_size, (dbx, dby))


crash_sound = pygame.mixer.Sound("pig_oink.wav") 

while not done:
    redx = redx + drx
    redy = redy + dry
    if redx<0 or redx>bredde-redballbredde:
        drx = -drx
    if redy<0 or redy>hoyde-redballhoyde:
        dry = -dry
    greenx = greenx + dgx
    greeny = greeny + dgy
    if greenx < 0 or greenx > bredde - greenballbredde:
        dgx = -dgx
    if greeny < 0 or greeny > hoyde - greenballhoyde:
        dgy = -dgy
    bluex = bluex + dbx
    bluey = bluey + dby
    if bluex < 0 or bluex > bredde - blueballbredde:
        dbx = -dbx
    if bluey < 0 or bluey > hoyde - blueballhoyde:
        dby = -dby
    score = "Score: "+str(poeng)
    scoretext = font.render(score, 1, red)
    if abs (redx - spillerx) < 20 and abs (redy - spillery) < 20:
        poeng = poeng + 1
        redx = randint(10, bredde-10)
        redy = randint (10, hoyde-10)
        crash_sound.play()
        pygame.mixer.music.stop()
    if abs (greenx - spillerx) < 20 and abs (greeny - spillery) < 20:
        poeng = poeng + 2
        greenx = randint (10, bredde-10)
        greeny = randint (10, hoyde-10)
        crash_sound.play()
        pygame.mixer.music.stop()
    if abs (bluex - spillerx) < 20 and abs (bluey - spillery) < 20:
        poeng = poeng + 2
        bluex = randint (10, bredde-10)
        bluey = randint (10, hoyde-10)
        crash_sound.play()
        pygame.mixer.music.stop()
        
    for e in pygame.event.get():
        if e.type==pygame.KEYDOWN:
            tmpspillerx=spillerx
            tmpspillery=spillery
            
        if e.type == pygame.QUIT:
                done = True 
                
    keys = pygame.key.get_pressed()
                
    if keys[pygame.K_LEFT]:
        tmpspillerx = spillerx - dx   
                    
        if tmpspillerx >0 and tmpspillerx < bredde-spillerbredde:
            spillerx=tmpspillerx
            
    if keys[pygame.K_RIGHT]:
        tmpspillerx = spillerx + dx
                    
        if tmpspillerx >0 and tmpspillerx < bredde-spillerbredde:
            spillerx=tmpspillerx
            
    if keys[pygame.K_DOWN]:
        tmpspillery = spillery + dy
        
        if tmpspillery >0 and tmpspillery < hoyde-spillerhoyde:
            spillery=tmpspillery
        
    if keys[pygame.K_UP]:
        tmpspillery = spillery - dy

                    
        if tmpspillery >0 and tmpspillery < hoyde-spillerhoyde:
            spillery=tmpspillery
        
    clock.tick(60)        
    screen.blit(bg_tilpasset, (0, 0))        
    screen.blit(spiller_size, (spillerx, spillery))
    screen.blit(redball_size, (redx, redy))
    screen.blit(scoretext, (20, 20))
    screen.blit(greenball_size, (greenx, greeny))
    screen.blit (blueball_size, (bluex, bluey))
    pygame.display.update()

#pygame.display.quit()
pygame.quit()
quit()