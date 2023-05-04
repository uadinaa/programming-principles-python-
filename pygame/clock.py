import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100, 'hour2': RADIUS - 80} #'digit': RADIUS - 30}

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds

font = pygame.font.SysFont('Verdana', 60)
img = pygame.image.load('mickeyclock33.jpg .png').convert_alpha()
bg = pygame.image.load('White_full.png').convert()
bg_rect = bg.get_rect()
bg_rect.center = WIDTH, HEIGHT
dx, dy = 1, 1

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    dx *= -1 if bg_rect.left > 0 or bg_rect.right < WIDTH else 1
    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < HEIGHT else 1
    bg_rect.centerx += dx
    bg_rect.centery += dy
    surface.blit(bg, bg_rect)
    surface.blit(img, (0, 0))
    
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    image = pygame.image.load("/Users/altynai/pp1/2 sem/practicing the game/photo5260444677235132240.jpg")

    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 8)
    pygame.draw.line(surface, pygame.Color('red'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)
    pygame.draw.circle(surface, pygame.Color('red'), (H_WIDTH, H_HEIGHT), 8) #center 

    pygame.display.flip()
    clock.tick(20)