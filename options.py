import pygame

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

def text_objects(text,font,colorfg):
    textSurface=font.render(text,True,colorfg)
    return textSurface, textSurface.get_rect()

def message_display(text,colorfg,i,size):
    largeText = pygame.font.Font('04b_30__.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText,colorfg)
    TextRect.center = ((display_width/2),(display_height/2+(100*i)))
    gameDisplay.blit(TextSurf, TextRect)

def settings(optionno):
    color=[black,black,black,black]
    option=["sound","display","credits","returntomenu"]
    if(optionno>4 or optionno<1):
        return 1
        color[0]=teal
    else:
        color[optionno-1]=teal
    for i in range(1,5):    
        message_display(option[i-1],color[i-1],i-1,70)


def returntomenu():
    return True
def creditsx():
    nr=True
    while nr:
        gameDisplay.fill(white)
        message_display("Made By Surya and Tanishk",black,0,50)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameDisplay.fill(white)
                    nr=False
                    break
    return False
def soundx():
    print("o1")
    return False
def resol():
    print("o2")
    return False



def option(wcm):
    if wcm==0:
        y=1
        pygame.display.set_caption("options")
        crashed=False
        gameDisplay.fill(white)
        settings(y)
        pygame.display.update()
        while not crashed:
            settings(y)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        if y>=4:
                            y=1
                        else:
                            y+=1
                    if event.key==pygame.K_UP:
                        if y<=1:
                            y=4
                        else:
                            y-=1
                    if event.key==pygame.K_RETURN:
                        switcher={
                            1: soundx,
                            2: resol,
                            3: creditsx,
                            4: returntomenu
                        }
                        func=switcher.get(y)
                        crashed=func()
                        gameDisplay.fill(white)
                if event.type==pygame.QUIT:
                    crashed=True
            pygame.display.update()
clock.tick(60)