import pygame


def main():
    pygame.init()
    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)

    mouse_img = pygame.image.load('data/arrow.png')
    arrow_sprite = pygame.sprite.Sprite()
    arrow_sprite.image = mouse_img
    pygame.mouse.set_visible(False)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_focused():
            screen.blit(arrow_sprite.image, pygame.mouse.get_pos())
        pygame.display.flip()


if __name__ == '__main__':
    main()