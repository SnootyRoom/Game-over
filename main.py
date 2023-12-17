import pygame
import os
import sys
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = pygame.transform.scale(load_image("boom.png"), image.get_size())

    def __init__(self, size):
        super().__init__(all_sprites)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(500 - self.rect.right)
        self.rect.y = random.randrange(500 - self.rect.bottom)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


all_sprites = pygame.sprite.Group()


def main():
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)

    bomb = Bomb(size)
    running = True

    for _ in range(20):
        Bomb(all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update(event)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()