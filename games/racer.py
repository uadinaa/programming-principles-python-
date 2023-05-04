import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1916
SPEED = 5
SCORE = 0
COIN = 0


previous_coin = 0 
time_collision = time.time()
collision = False

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("YOU DIED", True, BLACK)
 
background = pygame.image.load("road_0.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("DO NOT DIE")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("redcar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
        self.weight = 1 
      def move(self):
        global COIN 
        self.rect.move_ip(0,5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("271561.png")
        self.rect = self.image.get_rect()
        self.rect.center = (196, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                     
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while 1:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 1 
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    coinss = font_small.render("Coins: " + str(COIN), True, WHITE)
    DISPLAYSURF.blit(coinss, (10,30))
    scores = font_small.render(str(SCORE), True, WHITE)
    DISPLAYSURF.blit(scores, (10,10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        
    if pygame.sprite.spritecollideany(P1, enemies):

          DISPLAYSURF.fill(WHITE)
          DISPLAYSURF.blit(game_over, (50,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()  

    cur_time = time.time()
    
    if C1.rect.colliderect(P1.rect):
        if cur_time - time_collision > 1:
            time_collision = time.time()
            COIN += C1.weight
            collision = True

    C1.move()

    # doesn't dispaly coin after collosion
    if not collision:
        DISPLAYSURF.blit(C1.image, C1.rect)
        time3 = time.time()

    # coin disappears for 0.5 seconds after collision
    if cur_time - time3 > 0.5:
        time3 = time.time()
        collision = False
        
    pygame.display.update()
    clock.tick(60)