import pygame
import random 

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

bg = pygame.image.load("snake/Assets/BG.png").convert_alpha()
snekf = pygame.image.load("snake/Assets/snekf.png").convert_alpha()
snekb = pygame.image.load("snake/Assets/snekb.png").convert_alpha()
appl = pygame.image.load("snake/Assets/apple.png").convert_alpha()


def menu ():
    pygame.display.set_caption("Menu")


    font = pygame.font.Font(None, 100)
    MenuText = pygame.transform.scale((pygame.image.load("snake/Assets/logo.png").convert_alpha()), (313*1.5,57*1.5))
    Menurectangle = MenuText.get_rect(center=(300, 200))
    
    play_image=pygame.image.load("snake/Assets/playbutton.png").convert_alpha()
    play_image_hover=play_image.copy()
    play_image_hover.fill((200, 200, 200), special_flags=pygame.BLEND_RGB_MULT)
    
    play_rect=play_image.get_rect(center=(300,400))
    
    clock = pygame.time.Clock()

    while True:
        Mousepos = pygame.mouse.get_pos()

        screen.blit(bg, (0,0))

        screen.blit(MenuText, Menurectangle)

        if play_rect.collidepoint(Mousepos):
            screen.blit(play_image_hover, play_rect)
        else:
            screen.blit(play_image, play_rect)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_rect.collidepoint(event.pos):
                        pygame.display.set_caption("Snake")
                        play()
                        return
                    
        pygame.display.flip()
        clock.tick(60)


def play ():

    running = True
    snekpos = [(120,300), (60, 300), (0, 300)]
    new_head = snekpos[0]
    clock = pygame.time.Clock()
    tickspeed = 500
    direction = "right"
    currentdirection = "right"
    newdirection = "right"
    last = pygame.time.get_ticks()
    apple = "yes"
    applex = random.randint(0,9)*60
    appley = random.randint(0,9)*60

    while running:

        #rendering snake
        screen.fill((46, 16, 16))
        for body in snekpos[1:]:
            screen.blit(snekb, body)
        head = snekpos[0]
        if newdirection == "up":
            screen.blit(pygame.transform.rotate(snekf, 180), head)
        if newdirection == "down":
            screen.blit(snekf, head)
        if newdirection == "right":
            screen.blit(pygame.transform.rotate(snekf, 90), head)
        if newdirection == "left":
            screen.blit(pygame.transform.rotate(snekf, 270), head)

        #inputs
        if (pygame.key.get_pressed() [pygame.K_UP] or pygame.key.get_pressed() [pygame.K_w]) and currentdirection != "down":
            direction = "up"
        if (pygame.key.get_pressed() [pygame.K_DOWN] or pygame.key.get_pressed() [pygame.K_s]) and currentdirection != "up":
            direction = "down"
        if (pygame.key.get_pressed() [pygame.K_LEFT] or pygame.key.get_pressed() [pygame.K_a]) and currentdirection != "right":
            direction = "left"
        if (pygame.key.get_pressed() [pygame.K_RIGHT] or pygame.key.get_pressed() [pygame.K_d]) and currentdirection != "left":
            direction = "right"

        #rendering apple, and making you be able to collect it
        screen.blit(pygame.transform.scale(appl, (40, 40)), (applex + 10, appley + 10))    

        if (applex, appley) == new_head: 
                apple = "no"

        if apple == "no":
            while (applex, appley) in snekpos:
                applex = random.randint(0,9)*60
                appley = random.randint(0,9)*60 
            apple = "yes"


        
        #tickspeed zone
        now = pygame.time.get_ticks()
        if now - last > tickspeed: 

            #movement
            head_x, head_y = snekpos[0]

            if direction == "up":
                head_y -= 60
            elif direction == "down":
                head_y += 60
            elif direction == "left":
                head_x -= 60
            elif direction == "right":
                head_x += 60
            newdirection = direction
            new_head = (head_x, head_y)

            #dying 
            if new_head in snekpos:
                running = False
            snekpos.insert(0, new_head)

            last = now
            currentdirection = direction
            new_head = snekpos[0]

            #making player not grow when no apple
            if not (applex, appley) == new_head:
                snekpos.pop()
            if head_x < 0 or head_x > 540 or head_y < 0 or head_y > 540:
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ =="__main__":
    menu()