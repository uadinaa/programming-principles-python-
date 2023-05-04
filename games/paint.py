import pygame as pg

pg.init()
sc = pg.display.set_mode((1200, 700))
pg.display.set_caption("творческое место")
clock = pg.time.Clock()

aqua = (0,255,255)
red = (220,20,60)
violet = (138,43,226)
blue = (100,149,237)
greenish = (193,255,193)
kirpish = (255,125,64)
yellow = (255,255,0)
plankton = (3,168,158)
navy = (0,0,128)
black = (20, 20, 20)
white = (255,255,255)


a = pg.Rect(0,10, 50, 50)
r = pg.Rect(0,80, 50, 50)
b = pg.Rect(0, 150, 50, 50)
v = pg.Rect(0, 220, 50, 50)
g = pg.Rect(0, 290, 50, 50)
k = pg.Rect(0, 360, 50, 50)
y = pg.Rect(0, 430, 50, 50)
p = pg.Rect(0, 500, 50, 50)
w = pg.Rect(0, 570, 50, 50)
n = pg.Rect(0, 640, 50, 50)


buttons = [[aqua,       a], 
           [red,        r], 
           [blue,       b], 
           [violet,     v],
           [greenish,   g],
           [kirpish,    k],
           [yellow,     y],
           [plankton,   p],
           [white,      w],
           [navy,       n]]

clr = (255,255,255)

def changeclr():
    global clr

    px, py = pg.mouse.get_pos()
    push = pg.mouse.get_pressed()

    if push[0]:
        if px < 50 and 10 < py < 60:
            clr = aqua
        if px < 130 and px < 50 and py > 80:
            clr = red
        if py < 200 and px < 50 and py > 150:
            clr = blue
        if py < 270 and px < 50 and py > 220:
            clr = violet
        if py < 340 and px < 50 and py > 290:
            clr = greenish
        if py < 410 and px < 50 and py > 360:
            clr = kirpish
        if py < 480 and px < 50 and py > 430:
            clr = yellow
        if py < 550 and px < 50 and py > 500:
            clr = plankton
        if py < 620 and px < 50 and py > 570:
            clr = white
        if py < 690 and px < 50 and py > 640:
            clr = navy

def painting(mode):
    px, py = pg.mouse.get_pos()
    push = pg.mouse.get_pressed()
    
    if push[0]:
        if mode == "circle line":
            pg.draw.circle(sc, clr, (px, py), 5)
        elif mode == "square":
            pg.draw.rect(sc, clr, pg.Rect((px-20), (py-20), 40, 40),20)
        elif mode == "circle":
            pg.draw.circle(sc, clr, (px, py), 25,25)
        elif mode == "erase":
             pg.draw.circle(sc, (0,0,0), (px, py), 40)

def delete():
      key = pg.key.get_pressed()
      if key[pg.K_d]: #delete
          sc.fill((0, 0, 0))

drawing = "circle line"
do = True
while do:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            do = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                drawing = 'circle'
            elif event.key == pg.K_s:
                drawing = 'square'
            elif event.key == pg.K_e:
                drawing = 'erase'
            
    for i in buttons:   #color  rect
        pg.draw.rect(sc, i[0], i[1])
    
    painting(drawing)
    changeclr()
    delete()


    clock.tick(900)
    pg.display.update()