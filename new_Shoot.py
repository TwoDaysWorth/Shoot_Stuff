import os,sys,math,pygame.mixer,pygame,random

pygame.init()
pygame.font.init()

running = True
red = 250, 0, 0
white = 0, 0, 0
leftIsDown = False
rightIsDown = False
upIsDown = False
downIsDown = False
spaceIsDown = False

objects = []
# shipList = []
bulletList = []

screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
pygame.display.set_caption("Ship Fighter 9000")


'''
Problems

also just doesnt detect collision sometimes

Only detects collision if there is one bullet 

'''

### Methods

# def getCollision(object):
#     for num in range(len(bulletList)):
#         if ((bulletList[num].x - object.x) * (bulletList[num].x - object.x)  + (bulletList[num].y - object.y) * (bulletList[num].y - object.y) < (bulletList[num].radius + object.radius) * (bulletList[num].radius + object.radius)):
#             return True
#         else:
#             return False

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
        self.accel = 15.0
        self.radius = 10
        self.controllable = controllable
        objects.append(self)

    def display(self):
        pygame.draw.circle(screen, red, (int(self.x), int(self.y)), 10, 1)
        
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
        pygame.draw.circle(screen, red, (int(self.x), int(self.y)), 5, 1)
        
    def update(self):
        self.y -= 30
       

### Creating Objects

for num in range(0, 10):
    # shipList.append(Ship(random.randint(10, 500), 100, False))
    objects.append(Ship(random.randint(10, 500), 100, False))

player = Ship(300, 600, True)

### While Loop

while running:
    clock.tick(144)
    pygame.time.delay(100)

    ### Key Inputs

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftIsDown = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                rightIsDown = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                upIsDown = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                downIsDown = True
            if event.key == pygame.K_f:
                bulletList.append(Bullet())

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftIsDown = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                rightIsDown = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                upIsDown = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                downIsDown = False
    
    ### Creating Game
    
    screen.fill(white)
    
    ### Calls The Updater

    for num in range(len(objects)):
        updater(objects[num])
       
    ### Checks Collision

    objects = [x for x in objects if not determineQualification (x)]

    pygame.display.flip()