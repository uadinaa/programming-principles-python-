import pygame

pygame.init()               
screen = pygame.display.set_mode((500, 500))
done = False

x = 100
y = 100 

clock = pygame.time.Clock()

while not done:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20
        
        screen.fill((255, 255, 255))
        color = (138,43,226) 

        pygame.draw.circle(screen, color,(x,y), 25, 25)
        
        pygame.display.flip()
        clock.tick(60)