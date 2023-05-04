import pygame
import datetime

pygame.init()
surface = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

img = pygame.image.load(r'/Users/altynai/pp1/2 sem/lab7/mickeyclock-2.jpeg')
handforsec = pygame.image.load(r'/Users/altynai/pp1/2 sem/lab7/hand11.png')
handformin = pygame.image.load(r'/Users/altynai/pp1/2 sem/lab7/29A857A7-3403-4548-A21E-7D4B5F731A6D-removebg-preview.png')
handforsec = pygame.transform.scale(handforsec, (85, 500))
handformin = pygame.transform.scale(handformin, (220, 500))

minute = datetime.datetime.now().minute
second = datetime.datetime.now().second

delta_minute = minute - 30
delta_second = second - 30
oldtime = datetime.datetime.now().second

angle2 = -6 * delta_minute
angle = -6 * delta_second

count = second

def rotate_img(angle, angle2):
    rotated_img = pygame.transform.rotate(handforsec, angle)
    rotated_img2 = pygame.transform.rotate(handformin, angle2)
    rotated_rect = rotated_img.get_rect(center = (500, 350))
    rotated_rect2 = rotated_img2.get_rect(center = (500, 350))
    return rotated_img, rotated_rect, rotated_img2, rotated_rect2



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    t = datetime.datetime.now()
    surface.blit(img, (0, 0))

    rotating_img, rotated_rect, rotating_img2, rotated_rect2 = rotate_img(angle, angle2) 
    surface.blit(rotating_img, rotated_rect)

    surface.blit(rotating_img2, rotated_rect2)

    pygame.draw.circle(surface, (0, 0, 0), (504, 354), 20)
    minute, second =  t.minute, t.second
    
    cur_time =  datetime.datetime.now().second
    time_passed = cur_time - oldtime

    if time_passed >= 1 or time_passed <= -50:
        count += 1
        angle -= 6
        oldtime = cur_time
        
    if count >= 60:
            angle2 -= 6
            count = 0
    
    pygame.display.flip()
    clock.tick(20)