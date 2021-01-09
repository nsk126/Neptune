import pygame
import sys

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

black = 0,0,0

pygame.init()

window = (800,600)
screen = pygame.display.set_mode(window)

_background = pygame.Surface(window)

# Player Space Craft
_craftP1 = pygame.image.load("sprites/P2img.png")
_craftP1Rect = _craftP1.get_rect(center=(200, 200))



class bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Single bullet as a rect
    def drawBullet(pos):
        # bullet area = 20 x 15 ~> Y = 20 X = 15 (WIDTH)
        _pos = pos[0]+20, pos[1]
        #bullet color : red
        color = 255, 0, 0
        return pygame.draw.line(_background, color, pos, _pos, width=15)


_bulletPos = 100,100 # temp var for initial cords of bullet
_craftmomentum = [0,0]

while 1:
    shoot = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                _craftmomentum[1] = -1
            if event.key == pygame.K_s:
                _craftmomentum[1] = +1
            if event.key == pygame.K_a:
                _craftmomentum[0] = -1
            if event.key == pygame.K_d:
                _craftmomentum[0] = +1
            if event.key == pygame.K_SPACE:
                shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                _craftmomentum[1] = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                _craftmomentum[0] = 0
            if event.key == pygame.K_SPACE:
                shoot = False


        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     _craftP1Rect = _craftP1Rect.move(0,-5)
        # if keys[pygame.K_s]:
        #     _craftP1Rect = _craftP1Rect.move(0,+5)
        # if keys[pygame.K_a]:
        #     _craftP1Rect = _craftP1Rect.move(-5,0)
        # if keys[pygame.K_d]:
        #     _craftP1Rect = _craftP1Rect.move(+5,0)
        # if keys[pygame.K_SPACE]:
        #     print("space!")

    # Moving Craft rect
    _craftP1Rect = _craftP1Rect.move(_craftmomentum)
    if shoot == True:
        _bulletRect = drawBullet(_bulletPos)

    """
    Note: Fill BG first and then All Sprites on top.
    """
    # FOR DRAWING LAYERS
    _background.fill(black)

    # print(_bulletRect)
    # Player Craft Draw
    _background.blit(_craftP1,_craftP1Rect)
    # print(_craftP1Rect)


    speed = 1,0
    _bulletRect = _bulletRect.move(speed)
    _bulletPos = _bulletRect[0], _bulletRect[1]+7


    screen.blit(_background,(0,0))
    pygame.display.update()   # without this the screen turns black

# ballrect = ball.get_rect()





# Gameloop
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()
