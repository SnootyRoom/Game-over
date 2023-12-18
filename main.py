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


class GameOver(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, size):
        super().__init__(all_sprites)
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.rect.right = -600
        self.max_x = size[0]

    def update(self, *args):
        if self.rect.right < self.max_x:
            self.rect.right += 20


all_sprites = pygame.sprite.Group()


def main():
    pygame.init()
    size = 600, 300
    screen = pygame.display.set_mode(size)

    gameover = GameOver(size)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((0, 0, 255))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(100)

    pygame.quit()


if __name__ == '__main__':
    main()