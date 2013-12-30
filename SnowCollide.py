
# Import a library of functions called 'pygame'
import pygame
import random

# Initialize the game engine
pygame.init()

black = [ 0, 0, 0]
white = [255, 255, 255]
green = [0, 255, 0]
red   = [255, 0 , 0]
yellow = [255, 255,0]
magenta = [255, 0, 255]
cornflower = [100, 149, 237]
carrot = [237, 145, 33]

# Set the height and width of the screen
size = [1400, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snowflake with rectangle collision")

# Create an empty array
snow_list = []

# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 1400)
    y = random.randrange(0, 1400)
    snow_list.append([x, y])

clock = pygame.time.Clock()

rect_x = 20
rect_y = 20

rect_a = 700
rect_b = 400

rect_m = 1000
rect_n = 600

rect_change_x = 10
rect_change_y = 10

rect_change_a = 20
rect_change_b = 20

rect_change_m = 30
rect_change_n = 30

#Loop until the user clicks the close button.
done = False
while done == False:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
# Set the screen background
    screen.fill(black)
    
# Process each snow flake in the list
    for i in range(len(snow_list)):

# Draw the snow flake
        pygame.draw.circle(screen, white, snow_list[i], 10)
        
# Move the snow flake down one pixel
        snow_list[i][1] += 1
        
# If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 1400:
           
# Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
# Give it a new x position
            x = random.randrange(0, 1400)
            snow_list[i][0] = x

    pygame.draw.rect(screen, green, [rect_x, rect_y, 30, 30])
    pygame.draw.rect(screen, red, [rect_x + 5, rect_y + 10, 10, 10])
    
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_x == rect_a and rect_y == rect_b:
        rect_x += 20
        rect_y += 20

    if rect_x == rect_m and rect_y == rect_n:
        rect_x -= 20
        rect_y -= 20

               # Bounce the rectangle if needed
    if rect_y > 780 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 1380 or rect_x < 0:
        rect_change_x = rect_change_x * -1
        
    pygame.draw.rect(screen, yellow, [rect_a, rect_b, 30, 30])
    pygame.draw.rect(screen, magenta, [rect_a + 10, rect_b + 5, 10, 10])
    
    rect_a += rect_change_a
    rect_b += rect_change_b

    if rect_m == rect_a and rect_n == rect_b:
        rect_x += 20
        rect_y += 20

    if rect_x == rect_m and rect_y == rect_n:
        rect_x -= 20
        rect_y -= 20    

   # Bounce the rectangle if needed
    if rect_b > 780 or rect_b < 0:
        rect_change_b = rect_change_b * -1
    if rect_a > 1380 or rect_a < 0:
        rect_change_a = rect_change_a * -1

    pygame.draw.rect(screen, carrot, [rect_m, rect_n, 30, 30])
    pygame.draw.rect(screen, cornflower, [rect_m + 10, rect_n + 10, 10, 10])
    
    rect_m += rect_change_m
    rect_n += rect_change_n

    if rect_m == rect_x and rect_n == rect_y:
        rect_m += 20
        rect_m += 20

    if rect_m == rect_a and rect_n == rect_b:
        rect_m -= 20
        rect_m -= 20

   # Bounce the rectangle if needed
    if rect_n > 780 or rect_n < 0:
        rect_change_n = rect_change_n * -1
    if rect_m > 1380 or rect_m < 0:
        rect_change_m = rect_change_m * -1

# Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(30)
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
