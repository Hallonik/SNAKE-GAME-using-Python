# Building Snake Game using pygame and random Packages
#Prototype model

import pygame #import the game creation package for python
import random # to implement randomness in code


pygame.init()#initialize the pygame instance

#Setting up the game window

window_width=900 #width of the game window
window_height= 700 #height of the game window
window = pygame.display.set_mode((window_width,window_height)) # to create the window fo the game
pygame.display.set_caption("Snake Game") #to set the caption of the window


white = (255,255,255) #setting the RGB values for white colour of the snake
black = (0,0,0)
red = (255,0,0)

game_over = False # to determine if the game is running or not

score = 0 #initializing the score board

# making the coordinates of the dynamic so it can be changed  
x1=window_width/2 
y1=window_height/2

#to set the change in position of snake we want
x1_change=0
y1_change=0 

snake_body = []#creating a list for storing the snakes body

length_of_snake = 1#initializing the lenght of the snake


# setting randomness to the food position
foodx= round(random.randrange(0,window_width-10)/10)*10.0
foody= round(random.randrange(0,window_height-10)/10)*10.0


clock= pygame.time.Clock() #to set the frame rate


while not game_over: # loop is  implemented to keep the window running
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            game_over = True
        
        #Check for arrow key pressed
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: # func. for left arrow key
                x1_change =-10
                y1_change =0
            
            elif event.key == pygame.K_RIGHT: #func. for right arrow key
                x1_change=10
                y1_change=0

            elif event.key == pygame.K_UP: #func. for up arrow key
                x1_change=0
                y1_change=-10

            elif event.key == pygame.K_DOWN: #func. for down arrow key
                x1_change=0
                y1_change=10

    x1=x1 + x1_change
    y1= y1 + y1_change
   


    #to set the boundary conditions to quit the game
    if x1>=window_width or x1<0 or y1>=window_height or y1<0:
        game_over=True


    window.fill(black)# to refill the previous position of the snake with black colour

    snake_head = [] #initializing empty snake head
    snake_head.append(x1)
    snake_head.append(y1)

    snake_body.append(snake_head)#adding snake head to the body

    if len(snake_body)>length_of_snake: #to keep only one coordinate inn snake_bdy lost
        del snake_body[0]

    #checking if snake hitting its own body
    for segment in snake_body[:-1]:#reversing the items in snake body list 
        if segment==snake_head:
            game_over=True

    

    #displaying the score
    font_style = pygame.font.SysFont(None,50) #Setting the font to display score
    score_text=font_style.render("Score : "+str(score),True,white)
    window.blit(score_text,(10,10))
     


    if x1 == foodx and y1 == foody:#to check if the coordinates of the food and snake is same
        #after the coordinates of food and snake becomes same then change the coordiantes of the food
        foodx= round(random.randrange(0,window_width-10)/10)*10.0
        foody= round(random.randrange(0,window_height-10)/10)*10.0
        length_of_snake += 1 #incrementing the lenght of sanke
        score += 1 #increasng the score on eating the food

    pygame.draw.rect(window,red,[foodx,foody,10,10])# adding food item to the window

        #to display the snake ot the center divide the window height and width by 2
    #pygame.draw.rect(window,white,[x1,y1,10,10]) # to draw the snake on window

    for segment in snake_body: #to add snakes body
        pygame.draw.rect(window,white,[segment[0],segment[1],10,10])
    print(snake_body)
    pygame.display.update() #to update the display of the snake on window
    clock.tick(10) #sets the frame rate of the window






