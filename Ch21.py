import pygame, sys
from pygame.locals import *

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400,300))

    
    '''
    x = 20
    y = 20

    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (x, y), 10)
    pygame.display.update()

    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
    pygame.quit()
    '''

    red = 5
    green = 5
    blue = 5
    
    fonts = pygame.font.get_fonts()
    font = fonts.pop()
    while fonts:
        try:
            new_font = pygame.font.SysFont(font, 30)
        except:
            pass

        text = new_font.render(font + "  Hello Robert", 1, (red, green, blue))
        screen.fill(BLACK)
        screen.blit(text, (100, 150))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                font = fonts.pop()

                red += 5
                if red > 255:
                    red = 255
                    
                    green += 5
                    if green > 255:
                        green = 255
                    
                        blue += 5
                        if blue > 255:
                            blue = 255

    '''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x -= 2
                elif event.key == K_RIGHT:
                    x += 2
                elif event.key == K_UP:
                    y -= 2
                elif event.key == K_DOWN:
                    y += 2

        pygame.draw.rect(screen, BLACK, (0, 0, 400, 300))
        pygame.draw.circle(screen, RED, (x, y), 10)
        pygame.display.update()
        #pygame.time.delay(500)
    '''
    
if __name__ == "__main__":
    main()
