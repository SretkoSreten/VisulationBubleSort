import pygame
import random

WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Buble Sort")

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rows = 70
padding_left = 0
height_max = 200
height_min = 20
padding = 4
w = 5


def get_array():
    array = []
    for i in range(rows):
        x = i * (w + padding) + padding_left
        y = 0
        h = random.randint(height_min, height_max)
        array.append(h)

    return array

array = get_array()


def line1(win, i):
    x = i * (w + padding) + padding_left
    y = 0
    pygame.draw.rect(win, (255, 0, 0), (x, y, w, array[i]))

def line2(win, j):
    x = j * (w + padding) + padding_left
    y = 0
    pygame.draw.rect(win, (0, 0, 255), (x, y, w, array[j]))

def draw(win, array):
    for p in range(len(array)):
        x = p * (w + padding) + padding_left
        y = 0
        pygame.draw.rect(win, WHITE, (x, y, w, array[p]))

def swap(array, j):
    if array[j]>array[j+1]:  
        temp = array[j]  
        array[j] = array[j+1]  
        array[j+1] = temp  

def main():
    run = True
    i = 0
    j = 0
    clock = pygame.time.Clock()
    frames = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        win.fill(BLACK)

        swap(array, j)
        draw(win, array)
        line1(win, i)
        line2(win, j)


        if i < len(array) - 1:
            j += 1
            if j >= len(array) - 1 - i:
                j = 0
                i += 1

        else:
            print('Done')
            pygame.time.delay(2000)
            break
        
        pygame.display.update()

    pygame.quit()

main()