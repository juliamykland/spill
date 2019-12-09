import pygame
pygame.init()

size = (1200,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
done = False


bg = pygame.image.load("bakgrunn.png")
bg_tilpasset = pygame.transform.scale(bg,(size))
screen.blit(bg_tilpasset, (0, 0))



spiller = pygame.image.load("figur.png")
spiller_size = pygame.transform.scale(spiller, (100,80))
spillerx = 50
spillery = 50
dx = dy = 10
screen.blit(spiller_size, (spillerx, spillery))


money_s = (70,70)
money = pygame.image.load("penge.png")
money_size = pygame.transform.scale(money, (money_s))
screen.blit(money_size, (0, 0))



while not done:
    for e in pygame.event.get():
        if e.type==pygame.KEYDOWN:
            if e.type == pygame.QUIT:
                done = True
            if e.key == pygame.K_LEFT:
                spillerx = spillerx - dx
            if e.key == pygame.K_RIGHT:
                spillerx = spillerx + dx
                
            if e.key == pygame.K_DOWN:
                spillery = spillery + dy
                
            if e.key == pygame.K_UP:
                spillery = spillery - dy
    screen.blit(bg_tilpasset, (0, 0))        
#    screen.blit(spiller, (spillerx, spillery))
    screen.blit(spiller_size, (spillerx, spillery))
    screen.blit(money_size, (70, 70))
    pygame.display.update()
    
    
    
pygame.quit()


