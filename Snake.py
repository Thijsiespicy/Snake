import pygame
import random 

pygame.init()

screen = pygame.display.set_mode((600, 600))

snek = pygame.image.load("Assets/snek.png").convert()
appl = pygame.image.load("Assets/apple.png").convert()

running = True
snekpos = [(120,300), (60, 300), (0, 300)]
clock = pygame.time.Clock()
speed = 500
direction = "right"
last = pygame.time.get_ticks()
apple = "no"

while running:
    screen.fill((46, 16, 16))
    for segment in snekpos:
        screen.blit(snek, segment)
    if (pygame.key.get_pressed() [pygame.K_UP] or pygame.key.get_pressed() [pygame.K_w]) and currentdirection != "down":
        direction = "up"
    if (pygame.key.get_pressed() [pygame.K_DOWN] or pygame.key.get_pressed() [pygame.K_s]) and currentdirection != "up":
        direction = "down"
    if (pygame.key.get_pressed() [pygame.K_LEFT] or pygame.key.get_pressed() [pygame.K_a]) and currentdirection != "right":
        direction = "left"
    if (pygame.key.get_pressed() [pygame.K_RIGHT] or pygame.key.get_pressed() [pygame.K_d]) and currentdirection != "left":
        direction = "right"
   
    now = pygame.time.get_ticks()
    if now - last > speed: 

        head_x, head_y = snekpos[0]

        if direction == "up":
            head_y -= 60
        elif direction == "down":
            head_y += 60
        elif direction == "left":
            head_x -= 60
        elif direction == "right":
            head_x += 60

        new_head = (head_x, head_y)

        snekpos.insert(0, new_head)
        snekpos.pop()
        last = now
        currentdirection = direction
    head_x, head_y = snekpos[0]

    if apple == "no":
       applex = random.randint(0,10)
       appley = random.randint(0,10)
       applex = applex * 60 + 10
       appley = appley * 60 + 10
       apple = "yes"



    screen.blit(appl, (applex, appley))

    if head_x < 0 or head_x > 540 or head_y < 0 or head_y > 540:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

    clock.tick(60)

pygame.quit()