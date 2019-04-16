import pygame
import snake
import options

pygame.init()

display_width = 1280
display_height = 720

white = (255, 255, 255)
d_white = (250, 250, 250)
black = (0, 0, 0)
teal = (0, 128, 128)
blue_black = (50, 50, 50)
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock=pygame.time.Clock()

#image of snake for menu TODO: maybe make it move if possible
kawaiisnake=pygame.image.load("E:\CGM\kawaiisnakexx.png")

#display fn for all clipart TODO: dont you dare make another one
def clipdisp(x,y,z):
    gameDisplay.blit(z,(x,y))

def text_objects(text,font,colorfg):
    textSurface=font.render(text,True,colorfg)
    return textSurface, textSurface.get_rect()

def message_display(text,colorfg,i):
    largeText = pygame.font.Font('04B_30__.ttf',70)
    TextSurf, TextRect = text_objects(text, largeText,colorfg)
    TextRect.center = ((display_width/2),(display_height/2+(100*i)))
    gameDisplay.blit(TextSurf, TextRect)

#TODO:add variable to make flashing
def option(optionno):
    color=[black,black,black]
    option=["new game","options","exit"]
    if(optionno>3 or optionno<1):
        return 1
        color[0]=teal
    else:
        color[optionno-1]=teal
    for i in range(1,4):    
        message_display(option[i-1],color[i-1],i-1)

def newgame():
    print("w1")
    snake.game()
    gameDisplay.fill(white)

def settings():
    print("w2")
    options.option(0)

def exiter():
    print("w3")
    pygame.quit()
    quit()     

def menu():
    y=1
    pygame.display.set_caption("menu")
    crashed=False
    gameDisplay.fill(white)
    pygame.display.update()
    while not crashed:
        clipdisp((display_width/2-120),(display_height/2-300),kawaiisnake)
        option(y)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    if y>=3:
                        y=1
                    else:
                        y+=1
                if event.key==pygame.K_UP:
                    if y<=1:
                        y=3
                    else:
                        y-=1
                if event.key==pygame.K_RETURN:
                    switcher={
                        1: newgame,
                        2: settings,
                        3: exiter
                    }
                    func=switcher.get(y)
                    func()
            if event.type==pygame.QUIT:
                crashed=True
        pygame.display.update()
        clock.tick(60)

menu()       