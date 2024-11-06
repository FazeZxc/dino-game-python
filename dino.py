# dino run
#
# Released under the GNU General Public License
VERSION = "0.1"

try:
    import sys
    import pygame
    import os
    import math
    
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

def load_png(name):
    fullname = os.path.join("data", name)
    try: 
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()


pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("dino run")
clock = pygame.time.Clock()
running = True

class Dino(object):
    def __init__(self, color, y, width, height):
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.color = color
        self.jumpCount = 10


    def draw(self, screen):
        if self.jumpCount + 1 >= 27:
            self.jumpCount = 0
        pygame.draw.circle(screen, self.color, (300, self.y), 5)
        
def redrawGameWindow():
    screen.fill("blue")
    dino.draw(screen)
    pygame.display.update()


dino = Dino("red",600, 64, 64)
run = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    
    if not(dino.isJump):
        if keys[pygame.K_UP]:
            dino.isJump = True
            
    else:
        if dino.jumpCount >= -10:
            neg = 1
            
            if dino.jumpCount < 0:
                neg = -1
                
            dino.y -= (dino.jumpCount ** 2) * 0.5 * neg 
            dino.jumpCount -= 1
        
        else:
            dino.isJump = False
            dino.jumpCount = 10 
    
    redrawGameWindow()
    
pygame.quit()