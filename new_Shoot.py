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

#
shipList = []
bulletList = []

screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
pygame.display.set_caption("Shoot Stuff")

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.accel = 15.0
        self.radius = 10

    def display(self):
        pygame.draw.circle(screen, red, (int(self.x), int(self.y)), 10, 1)
        
    def updateXY(self):
        
        if leftIsDown == True:
            self.x -= self.accel
        if rightIsDown == True:
            self.x += self.accel
        if upIsDown == True:
            self.y -= self.accel
        if downIsDown == True:
            self.y += self.accel
        
for num in range(0, 10):
    shipList.append(Ship(random.randint(10, 500), 100))

player = Ship(300, 600)
    
class Bullet:
    def __init__(self):
        self.x = player.x
        self.y = (player.y - 20)
        self.radius = 5
        
    def displayBull(self):
        pygame.draw.circle(screen, red, (int(self.x), int(self.y)), 5, 1)
        
    def updateY(self):
        self.y -= 30
       
def getCollision(object):
    for num in range(0, len(bulletList)):
        
        if ((bulletList[num].x - object.x) * (bulletList[num].x - object.x)  + (bulletList[num].y - object.y) * (bulletList[num].y - object.y) < (bulletList[num].radius + object.radius) * (bulletList[num].radius + object.radius)):
            del bulletList[num]
            return True
        else:
            return False
        

while running:
    clock.tick(144)
    pygame.time.delay(100)

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
    
    screen.fill(white) 

    for num in range(0, 10):
        shipList[num].display()
        

    player.display()
    player.updateXY()
    

    for num in range(0, len(bulletList)):
        bulletList[num].displayBull()
        bulletList[num].updateY()
       
    # for num in range(0, len(shipList)):
    #     print('checking a circle')
    #     if getCollision(shipList[num]):
    #         print('deleteing a circle')
    #         del shipList[num]
    #         shipList.append(Ship(random.randint(10, 500), 100))
    #         break

    for count,each in enumerate(shipList, start=0):
        if getCollision(shipList[count]):
            print('deleteing a circle')
            del shipList[count]
            shipList.append(Ship(random.randint(10, 500), 100))
            break

    for num in range(0, len(bulletList)):
        if bulletList[num].y < 50:
            print('bullet out of bounds')
            del bulletList[num]
            
            
    pygame.display.flip()      

