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
    image = load_image("car.png")

    def __init__(self, size):
        super().__init__(all_sprites)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.x = 0
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.direction = 1
        self.max_x = size[0]
        all_sprites.add(self)

    def update(self, *args):
        if self.rect.right >= self.max_x:
            self.image = self.flipped_image
            self.direction = -1
        elif self.rect.left <= 0:
            self.image = Car.image
            self.direction = 1
        self.rect.x += 1 * self.direction


all_sprites = pygame.sprite.Group()


def main():
    pygame.init()
    size = 600, 95
    screen = pygame.display.set_mode(size)

    car = Car(size)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()