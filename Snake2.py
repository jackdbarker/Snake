import pygame
import random
import time

pygame.init()

#defining clock, screen and general font
screen_height = 400
screen_length = 500
clock = pygame.time.Clock()
screen = pygame.display.set_mode([screen_length, screen_height])
pygame.display.set_caption('Snake by Jack Barker')
font = pygame.font.SysFont("Arial", 30)

#defining colours
GREEN = (0, 255, 0)
LIGHTGREEN = (50, 205, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#size of the snake
snake_block_size = 10 

#speed of the snake
speed = (10) 

#function for displaying score
def Score(score):
    num = font.render("Score: " + str(score), True, WHITE)
    screen.blit(num, [0, 0])

#function for when player loses
def end_screen(msg,colours):
    lost = font.render(msg, True, colours)
    screen.blit(lost,[200,200])

#function for snakes body behind the head
def snake_body(snake_block_size, snakelist):
    for x in snakelist:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block_size, snake_block_size])

#main loop of the game
def main():
    running = True
   
    x1_change = 0
    y1_change = 0

    x1 = screen_length/2
    y1 = screen_height/2

    pellety = round(random.randrange(0, screen_height - snake_block_size) /10.00) * 10.00
    pelletx = round(random.randrange(0, screen_length - snake_block_size) / 10.00) * 10.00

    snakelist = []
    snake_length = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
       
        x1 += x1_change
        y1 += y1_change

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [pelletx, pellety, snake_block_size, snake_block_size])
        pygame.draw.rect(screen, BLACK, [x1, y1, snake_block_size, snake_block_size])
       
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snakelist.append(snake_head)
        if len(snakelist) > snake_length:
            del snakelist[0]
        
        for x in snakelist[:-1]:
            if x == snake_head:
                end_screen("You Lose!", RED)
                pygame.display.update()
                time.sleep(2)
                running = False


        snake_body(snake_block_size, snakelist)
        Score(snake_length - 1)

        pygame.display.update()

        if x1 >= screen_length or x1 < 0 or y1>= screen_height or y1 <0:
            end_screen("You Lose!", RED)
            pygame.display.update()
            time.sleep(2)
            running = False
        
        if x1 == pelletx and y1 == pellety:
            pellety = round(random.randrange(0, screen_height - snake_block_size) /10.00) * 10.00
            pelletx = round(random.randrange(0, screen_length - snake_block_size) / 10.00) * 10.00
            snake_length += 1
        clock.tick(speed)

    pygame.quit()
    quit()

main()
