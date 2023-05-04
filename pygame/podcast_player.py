import pygame
import os

library = {}
def get_image(path):
        global library
        image = library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                library[path] = image
        return image


path2 = "/Users/altynai/pp1/2 sem/images/photo.jpg"
x = 1
y = 1

path = "/Users/altynai/pp1/2 sem/sounds"
listofsongs = os.listdir(path) 
i = 0

def play_music():
    pygame.mixer.music.load(os.path.join(path, listofsongs[i])) 
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def next_music():
    global i
    i = (i + 1) % len(listofsongs)
    play_music()

def prev_music():
    global i
    i = (i - 1) % len(listofsongs)
    play_music()

pygame.init() 
screen = pygame.display.set_mode((878, 586)) 
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy(): 
                    pause_music()
                else:
                    unpause_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()
            
    
    screen.fill((255,255,255))
    screen.blit(get_image(path2), (x,y))
        
    pygame.display.flip()
    clock.tick(60)