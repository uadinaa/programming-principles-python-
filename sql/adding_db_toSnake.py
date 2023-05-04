import pygame as pg 
import psycopg2
from random import randint, randrange, choice
name = input("input the user's name: ") 

config = psycopg2.connect(
   host="localhost",
    database="postgres",
    user="postgres",
    password="")

current = config.cursor()


sql = '''
    SELECT * FROM snake WHERE username = %s; 
'''


current.execute(sql, [name])
config.commit()
data = current.fetchone()

if data == None: # создаем начальные данные если игрока нет в базе данных


    sql = '''
        INSERT INTO snake VALUES(%s, 0, 0);
    '''


    current.execute(sql, [name])
    config.commit()
else: # если он уже есть в базе данных, высвечиваем в консоль его последний уровень


    sql = '''
    SELECT level FROM snake WHERE username = %s;
    '''


    current.execute(sql, [name])
    final = current.fetchone()
    print(*final)
    config.commit()



pg.init()

w, h, fps, level, step = 800, 800, 4, 0, 40 # разделяем окно на 400 квадратиков, 20 на 20
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Snake Game')
is_running, lose, paused = True, False, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 40)
surf = pg.Surface((390, 390))
bg = pg.image.load("background.jpg")
bg = pg.transform.scale(bg, (w, h))
gameover = pg.image.load("gameover.jpg")
gameover = pg.transform.scale(gameover, (390, 390))
cur_sc = 0
pg.mixer.init()
timmer = 8000
rush = False

class Food:
    def __init__(self, im):
        # задаем рандомные координаты для еды в диапазоне игрового поля с шагом в 40
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.r = 0
        self.image = im

    def draw(self):
        rect = pg.Rect(self.x, self.y, step, step)  
        screen.blit(self.image, rect)
        
    def draw2(self):
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.r = randint(1, 2)
        self.image = pg.image.load(f'food{self.r}.jpg')

class Snake:
    def __init__(self):
        self.speed = step
        self.body = [[360, 360]] # изначальные координаты головы
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = 'green'
    
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN: # движение змейки по нажатию на клавиатуру
                if event.key == pg.K_a and self.dx == 0: # чтобы при нажатии налево, змейка не двигалась вправо
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_d and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_w and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_s and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed

        # передвигаем части тела змейки по х и у на предыдущие координаты
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        # передвигаем голову змейки по х и у на следующие координаты
        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))
    
    # проверяем когда змейка съедает еду
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y: # если координаты головы змейки совпадают с координатами еды
            self.score += f.r # добавляем разный скор соответствующий разным видам еды
            #pg.mixer.Sound('./music/eat.mp3').play()
            global rush
            rush = True
            self.body.append([1000, 1000]) 
    
    # заканчиваем игру, если голова змейки столкнеться со своим телом
    def self_collide(self):
        global is_running
        if self.body[0] in self.body[1:]: # если голова змейки и входит в массив координат тела змейки
            lose = True # запускаем цикл 'game_over' 
            # pg.mixer.music.stop()
            # pg.mixer.Sound('./music/gameover.wav').play()
            # pg.mixer.music.stop()

    # проверяем чтобы еда не оказалась на теле змейки
    def check_food(self, f:Food): 
        if [f.x, f.y] in self.body: # если координаты еды входят в массив координат тела змейки
            f.draw2() # заново рисуем еду


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pic = pg.image.load("wall.png")


    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

def disappear(t):
    pg.time.set_timer(pg.USEREVENT, t)

# создаем объекты змейки и еды
s = Snake()
f = Food(pg.image.load(f'food{randint(1,2)}.jpg'))
disappear(5000)
# запускаем основной цикл
while is_running:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.USEREVENT and rush == False: # еда появляется каждые пять секунд
            f.draw2() # через 5 секунд перерисовывается
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p: # ставим игру на паузу
                paused = True
    screen.blit(bg, (0, 0))

    # прорисовываем стенки с помощью заранее написанных паттернов  
    my_walls = open(f'wall{level}.txt', 'r').readlines() # читает каждую линию как отдельный лист
    walls = []
    for i, line in enumerate(my_walls): # проходимся по индексу и строке
        for j, each in enumerate(line): # проходимся по каждому элементу в строке
            if each == "+":
                walls.append(Wall(j * step, i * step)) # добавляем каждый блок стенки в лист

    # вызываем методы классов
    f.draw()
    s.draw()
    s.move(events) # нажать любую клавишу (a, s, d, w) чтобы начать игру
    s.collide_food(f)
    s.self_collide()
    s.check_food(f)

    # высвечиваем текущие баллы и уровень на экран
    counter = score.render(f'Score: {s.score}', True, 'black')
    screen.blit(counter, (50, 50))
    l = score.render(f'Level: {level}', True, 'black')
    screen.blit(l, (50, 80))

    # условие для перехода на следующий уровень
    if s.score >= 3:
        #pg.mixer.Sound('./music/nextlevel.mp3').play()
        level += 1 # увеличиваем уровень
        level %= 4 
        fps += 2 # увеличиваем скорость
        s.score = 0 # новый счетчик для следующего уровня
        cur_sc += 3

    # высвечиваем стенки на экран
    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y: # перерисовываем еду, если она оказалась на стенках
            f.draw2()

        if s.body[0][0] == wall.x and s.body[0][1] == wall.y: # останавливаем игру, если голова змейки столкнеться со стенкой
            lose = True
            # pg.mixer.music.stop()
            # pg.mixer.Sound('./music/gameover.wav').play()
            # pg.mixer.music.stop()

    if rush == True: # если мы съедаем еду, она заново перерисовывается и она заново будет стоять 5 секунд
        timmer = 5000
        disappear(timmer)
        f.draw2() 
        rush = False
    
    # запускаем цикл паузы
    while paused: 
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                paused = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_u:
                    paused = False # возобнавляем игру
                if event.key == pg.K_c:
                    a = cur_sc + s.score # обновляем текущие данные в базе данных
                    sql = '''
                        UPDATE snake SET score = %s, level = %s WHERE username = %s;
                    '''
                    current.execute(sql, [a, level, name])
                    config.commit()  
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (315, 350))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (317, 385))
        txt = score.render(f'Press "C" to save your current state', True, 'white')
        screen.blit(txt, (212, 420))
        pg.display.flip()
        
    # запускаем цикл 'game_over'
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False   
        surf.blit(gameover, (0, 0))
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (272, 180))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (272, 250))
        pg.display.flip()
        cur_sc += s.score
        l = level

    pg.display.flip()
pg.quit()
# после окончания игры обновляем данные игрока в базе данных
sql = '''
    UPDATE snake SET score = %s, level = %s WHERE username = %s;
'''
current.execute(sql, [cur_sc, l, name])
config.commit()
current.close()
config.close()