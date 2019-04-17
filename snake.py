import pygame
import time
import random

pygame.init()

#frequency, size, channels, buffersize
# defines the width and height of the display
display_width = 1280
display_height = 720

white = (255, 255, 255)
d_white = (250, 250, 250)
black = (0, 0, 0)
brown=(210,105,30)
teal = (0, 128, 128)
blue1=(0, 119, 190)
blue_black = (50, 50, 50)
green=(178,255,112)
red=(254,95,85)
game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
factor = 10
got_food = pygame.mixer.Sound("E:\CGM\snakepy\coin.wav")
so_dead=pygame.mixer.Sound("E:\CGM\snakepy\dead.wav")
class snake_body:
    x = 0
    y = 0


    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

class level_pop:
    x = 0
    y = 0
    color=black


    def __init__(self, x_position, y_position,colorp):
        self.x = x_position
        self.y = y_position
        self.color=colorp

snake = []
danger=[]
def snake_start(snake):
    del snake[:]
    for i in range(16):
        snake.append(snake_body(100, (100+(10*(15-i)))))


# class food():
#     x=0
#     y=0
#
#     def __init__(self):

def block(displaywidth,displayht):
    z=[]
    for i in range(13):
        x=random.randrange(0,displaywidth-100)
        y=random.randrange(0,displayht-100)
        z.append(snake_body(x,y))
    return z

def levelcr(level):
    global danger
    k=0
    for i in range(len(level)):
        l=random.randrange(4,8)
        for j in range(0,40,l):
            if l%2==0:
                danger.append(level_pop(level[i].x+k*10,level[i].y,brown))
                k+=1
            else:
                
                danger.append(level_pop(level[i].x+k*10,level[i].y+k*10,blue1))
                k+=1
#moves snake
def update_snake(score):
    i = len(snake) - 1


    while i > 0:
        snake[i].x = snake[i - 1].x
        snake[i].y = snake[i - 1].y
        i -= 1


def check_death():
    if snake[0].x < 1 or snake[0].x > display_width or snake[0].y < 1 or snake[0].y > display_height:
        if pygame.mixer.get_init():
            pygame.mixer.Sound.play(so_dead)
            pygame.mixer.music.stop()
        return True
    for i in range(1, len(snake)):
        if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
            if pygame.mixer.get_init():
                pygame.mixer.Sound.play(so_dead)
                pygame.mixer.music.stop()
            return True
    for i in range(len(danger)):
        if snake[0].x < danger[i].x+10 and snake[0].x > danger[i].x-10 and snake[0].y < danger[i].y+10 and snake[0].y >danger[i].y-10:
            return True    
    return False
#draws on display environment
def drawsnake(snake):
    x=True
    for i in range(len(snake)):
        if x:
            pygame.draw.rect(game_display, red, (snake[i].x, snake[i].y, factor, factor))
            x = False
        elif not x:
            pygame.draw.rect(game_display, white, (snake[i].x, snake[i].y, factor, factor))
            x = True
    for i in range(len(danger)):
        pygame.draw.rect(game_display, danger[i].color, (danger[i].x, danger[i].y, factor, factor))




def food():
    food_x = random.randrange(5, display_width - 5)
    food_y = random.randrange(5, display_height - 5)
    for i in range(len(danger)):
        if food_x < danger[i].x+10 and food_x > danger[i].x-10 and food_y < danger[i].y+10 and food_y >danger[i].y-10:
            food_x+=100
            food_y+=100
    return food_x,food_y


#TODO: call game function
def game():
    if pygame.mixer.get_init():
        pygame.mixer.music.load("E:\\CGM\\snakepy\\bggame.wav")
        pygame.mixer.music.play()
    levelcr(block(display_width,display_height))
    snake_start(snake)
    food_x,food_y=food()
    print(food_x, food_y)
    score = 60
    score=60
    x = 0
    y = 0
    x_change = 0
    y_change = 0
    first_time = True
    eat = True
    escap=False
    while not escap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if first_time:
                    x_change = 10
                    y_change = 0
                    first_time=False
                elif event.key == pygame.K_a:
                    if x_change is not 10:
                        x_change = -10
                        y_change = 0
                elif event.key == pygame.K_d:
                    if x_change != -10:
                        x_change = 10
                        y_change = 0
                elif event.key == pygame.K_w:
                    if y_change is not 10:
                        x_change = 0
                        y_change = -10
                elif event.key == pygame.K_s:
                    if y_change != -10:
                        x_change = 0
                        y_change = 10
                elif event.key == pygame.K_c:
                    x_change = 0
                    y_change = 0
                elif event.key==pygame.K_ESCAPE:
                    escap=True
                    break


        if not first_time:
            update_snake(score)
        if score % 10 == 0 and eat:
            snake.append(snake_body(snake[len(snake)-1].x, snake[len(snake)-1].y))
            print(len(snake))
            eat = False

        snake[0].x += x_change
        snake[0].y += y_change
        if snake[0].x < food_x+10 and snake[0].x > food_x-10 and snake[0].y < food_y+10 and snake[0].y >food_y-10:
            if pygame.mixer.get_init():
                pygame.mixer.Sound.play(got_food)
            score = score + 10
            food_x,food_y=food()
            eat = True

        if escap==False:
            escap=check_death()
        if escap==True:
            pygame.mixer.music.stop()
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                pygame.mixer.music.load("E:\\CGM\\snakepy\\dead.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.stop()
        game_display.fill(green)

        pygame.draw.rect(game_display, black, (food_x, food_y, factor, factor))
        drawsnake(snake)

        pygame.display.update()
        time.sleep(0.035)
clock.tick(120)