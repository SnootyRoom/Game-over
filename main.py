import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Car(pygame.sprite.Sprite):
    image = load_image("")
    def __init__(self, pos_x, pos_y):




def main():
    pygame.init()
    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)

    mouse_img = pygame.image.load('data/arrow.png')
    arrow_sprite = pygame.sprite.Sprite()
    arrow_sprite.image = mouse_img

    running = True
    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_focused():
            screen.blit(arrow_sprite.image, pygame.mouse.get_pos())
        pygame.display.flip()


if __name__ == '__main__':
    main()