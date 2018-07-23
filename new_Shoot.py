import os,sys,math,pygame.mixer,pygame,random

pygame.init()
pygame.font.init()


backGround = pygame.image.load('water.png')
spaceShip = pygame.image.load('alien.png')
rocket = pygame.image.load('rocket.png')
running = True
red = 250, 0, 0
white = 0, 0, 0
leftIsDown = False
rightIsDown = False
upIsDown = False
downIsDown = False
spaceIsDown = False

objects = []

bulletList = []

screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
pygame.display.set_caption("Ship Fighter 9000")


'''
Problems

Zero

'''

### Methods

def getCollision(object):
    for num in range(len(objects)):
        if type(objects[num]) == Bullet:
            if ((objects[num].x - object.x) * (objects[num].x - object.x)  + (objects[num].y - object.y) * (objects[num].y - object.y) < (objects[num].radius + object.radius) * (objects[num].radius + object.radius)):
                return True
    return False


def updater(object):
    object.update()
    object.display()


def determineQualification (obj):
    if type(obj) == Ship:
        if getCollision(obj):
            return True
        else:
            return False
    elif type(obj) == Bullet:
        if obj.y < 10:
            return True
        else:
            return False
    return False

### Ship Class

class Ship:
    def __init__(self, x, y, controllable):
        self.x = x
        self.y = y
        self.accel = 25.0
        self.radius = 35
        self.controllable = controllable
        objects.append(self)

    def display(self):
        # pygame.draw.circle(screen, red, (int(self.x), int(self.y)), 35, 0)
        screen.blit(spaceShip, ((int(self.x)-35, int(self.y)-35)))
        
        
    def update(self):
        if self.controllable:
            if leftIsDown == True:
                self.x -= self.accel
            if rightIsDown == True:
                self.x += self.accel
            if upIsDown == True:
                self.y -= self.accel
            if downIsDown == True:
                self.y += self.accel
        else:
            self.y += 1

### Bullet Class     

class Bullet:
    def __init__(self):
        self.x = player.x
        self.y = (player.y - 20)
        self.radius = 5
        objects.append(self)
        
    def display(self):
        # pygame.draw.circle(screen, red, (int(self.x), int(self.y)), 5, 0)
        screen.blit(rocket, ((int(self.x)-15, int(self.y)-15)))
    def update(self):
        self.y -= 30
       

### Creating Objects

for num in range(0, 10):
    
    objects.append(Ship(random.randint(10, 500), 100, False))

player = Ship(300, 600, True)

### While Loop

while running:
    clock.tick(144)
    pygame.time.delay(25)

    ### Key Inputs

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftIsDown = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                rightIsDown = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                upIsDown = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                downIsDown = True
            elif event.key == pygame.K_SPACE:
                Bullet()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftIsDown = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                rightIsDown = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                upIsDown = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                downIsDown = False
    
    ### Creating Game
    
    screen.fill(white)
    screen.blit(backGround, (0, 0))
    
    ### Calls The Updater

    for num in range(len(objects)):
        updater(objects[num])
       
    ### Checks Collision

    objects = [x for x in objects if not determineQualification (x)]

    pygame.display.flip()