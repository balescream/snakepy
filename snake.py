import pygame
import time
import random

pygame.init()

# defines the width and height of the display
display_width = 1280
display_height = 720

white = (255, 255, 255)
d_white = (250, 250, 250)
black = (0, 0, 0)
teal = (0, 128, 128)
blue_black = (50, 50, 50)
game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
factor = 10

class snake_body:
    x = 0
    y = 0


    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position


snake = [snake_body(0,0)]

def snake_start(snake):
    del snake[:]
    for i in range(16):
        snake.append(snake_body(20+(10*(15-i)), 20))


# class food():
#     x=0
#     y=0
#
#     def __init__(self):






def update_snake(score):
    i = len(snake) - 1


    while i > 0:
        snake[i].x = snake[i - 1].x
        snake[i].y = snake[i - 1].y
        i -= 1


def check_death():
    if snake[0].x < 1 or snake[0].x > display_width or snake[0].y < 1 or snake[0].y > display_height:
        return True
    for i in range(1, len(snake)):
        if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
            return True
    return False

def drawsnake(snake):
    for i in range(len(snake)):
        pygame.draw.rect(game_display, teal, (snake[i].x, snake[i].y, factor, factor))


def game():
    snake_start(snake)
    food_x = random.randrange(5, display_width - 5)
    food_y = random.randrange(5, display_height - 5)
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
                first_time = False
                if event.key == pygame.K_a:
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
            score = score + 10
            food_x = random.randrange(5, display_width - 5)
            food_y = random.randrange(5, display_height - 5)
            eat = True

        escap=check_death()
        game_display.fill(white)


        pygame.draw.rect(game_display, black, (food_x, food_y, factor, factor))
        drawsnake(snake)

        pygame.display.update()
        time.sleep(0.035)
clock.tick(60)