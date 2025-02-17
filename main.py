import pygame

display_width = 900 #25
display_height = 660 #20
screen = pygame.display.set_mode((display_width, display_height))

moving=True
direction=0

pygame.init()
pygame.display.set_caption('Neural Network')

button_1=False

car=pygame.image.load('images/car.png')

start_car_x=50
start_car_y=17
carX=50
carY=17
car_angle=0
car_speed=1
road=pygame.image.load('images/road_2.png')
road2=pygame.image.load('images/road.png')
background=pygame.image.load('images/background.jpg')
mask_map=pygame.image.load('images/mask_map.png')
house1=pygame.image.load('images/house.png')
bank=pygame.image.load('images/bank.png')
stone=pygame.image.load('images/stone.png')
forbiden=pygame.image.load('images/forbiden.png')
forbiden2=pygame.image.load('images/forbiden2.png')
forbiden3=pygame.image.load('images/forbiden3.png')
forbiden4=pygame.image.load('images/forbiden4.png')
start_2=pygame.image.load('images/start_2.png')





MAP_MATRIX = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 2, 2, 2, 0, 4, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 2, 2, 2, 2, 0],
    [0, 1, 2, 2, 2, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 4, 2, 2, 2, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 0],
    [4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],

]




def carr(x,y,angle):
    rotated_car = pygame.transform.rotate(car, angle)
    car_rect = rotated_car.get_rect(center=(x, y))
    screen.blit(rotated_car, car_rect.topleft)





def roadd():
    for row in range(len(MAP_MATRIX)):
        for col in range(len(MAP_MATRIX[row])):
            x, y = col * 33, row * 33

            if MAP_MATRIX[row][col] == 1:
                screen.blit(road2, (x, y))
            if MAP_MATRIX[row][col] == 2:
                screen.blit(road, (x, y))
            if MAP_MATRIX[row][col] == 3:
                rotated_bank = pygame.transform.rotate(bank, 90)
                screen.blit(rotated_bank, (x, y))
            if MAP_MATRIX[row][col] == 4:
                screen.blit(house1,(x,y))


green_color = (0, 255, 0)

def isOnRoad(x,y):
    x=int(x/33)
    y=int (y/33)
    if MAP_MATRIX[y][x] == 0:
        return True
    return False
# Funcție pentru verificarea dacă mașina este pe drum


def button(x,y):
    if x>815 and x<879 and y>36 and y<68:
        return 1
    else:
        if x > 815 and x < 879 and y > 100 and y < 132:
            return 2
        else:
            if x > 815 and x < 879 and y > 164 and y < 196:
                return 3
            else:
                if x > 815 and x < 879 and y > 228 and y < 260:
                    return 4
                else:
                    if x > 815 and x < 879 and y > 292 and y < 324:
                        return 5
                    return 0


def mov_down(x,y,moving,car_angle,type):
    if moving and type==1:
        y+=car_speed
    if moving and type==2:
        x+=car_speed
        car_angle=90

    if moving and type==3:
        y-=car_speed
        car_angle=180
    if moving and type==4:
        x-=car_speed
        car_angle=-90
    return x,y,not moving,car_angle


def moving_car(x,y,car_angle):
    x_index = int(x / 33)
    y_index= int(y / 33)
    if MAP_MATRIX[y_index+1][x_index] == 1:
        car_angle=0
        return x,y+car_speed,car_angle
    if MAP_MATRIX[y_index][x_index+1] == 2 or MAP_MATRIX[y_index][x_index+1] == 1 and car_angle!=-90:
        car_angle=90
        return x+car_speed,y,car_angle
    if MAP_MATRIX[y_index][x_index-1] == 1 or MAP_MATRIX[y_index][x_index-1] == 2:
        car_angle=-90
        return x-car_speed,y,car_angle
    return x,y,car_angle

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    tempX = carX
    tempY = carY
    if event.type == pygame.MOUSEBUTTONDOWN :
        mouse_x,mouse_y=event.pos
        if button(mouse_x,mouse_y)==1:
            button_1=True
        if button(mouse_x,mouse_y)==2:
            button_1=False
        if button(mouse_x,mouse_y)==3:
            print ('3')
        if button(mouse_x,mouse_y)==4:
            print ('4')
        if button(mouse_x,mouse_y)==5:
            print ('5')
        if button(mouse_x,mouse_y)==0:
            print("0")



    if button_1==False:    # Resetează variabila când butonul de mouse este eliberat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and carX >= 0:
                tempX -= car_speed
                car_angle = 90
            if event.key == pygame.K_RIGHT and carX < display_width - 32:
                tempX += car_speed
                car_angle = -90
            if event.key == pygame.K_UP and carY >= 0:
                tempY -= car_speed
                car_angle = 0
            if event.key == pygame.K_DOWN and carY < display_height - 32:
                tempY += car_speed
                car_angle = 180
            if isOnRoad(tempX,tempY)==True:
                tempX = start_car_x
                tempY = start_car_y
            carX = tempX
            carY = tempY
    roadd()
    if button_1==True:
        carX,carY,car_angle=moving_car(tempX,tempY,car_angle)
    carr(carX, carY, car_angle)
    screen.blit(start_2,(815,20))
    screen.blit(start_2, (815, 84))
    screen.blit(start_2, (815, 148))
    screen.blit(start_2, (815, 212))
    screen.blit(start_2, (815, 276))
    moving=True


    pygame.display.update()

    '''
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    tempX=carX
    tempY=carY
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and carX>=0 :
            tempX-=car_speed
            car_angle = 90

        if event.key == pygame.K_RIGHT and carX<display_width - 32:
            tempX+=car_speed
            car_angle = -90
        if event.key == pygame.K_UP and carY>=0:
            tempY-=car_speed
            car_angle = 0
        if event.key == pygame.K_DOWN and carY<display_height-32:
            tempY+=car_speed
            car_angle = 180
        carX=tempX
        carY=tempY
        '''


