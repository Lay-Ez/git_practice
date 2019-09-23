import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Hola Bitches")



walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')



#character coords and dimensions
x = 50
y = 425
width = 64
height = 64
vel = 5

#jump parameters
isJump = False
jumpCount = 8

#some variables
left = False
right = False
walkCount = 0



def redraw_game_window():
    global walkCount
    win.blit(bg, (0,0))
    pygame.draw.rect(win, (255, 155, 0), (x, y, width, height))
    pygame.display.update()

#mainloop
run = True
while run:
    pygame.time.delay(50)


    #checks if the game is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0 and x > vel:
            x -= vel
    if keys[pygame.K_RIGHT] and x + width + vel < 500:
            x += vel

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -8:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 8
    redraw_game_window()

pygame.quit()
