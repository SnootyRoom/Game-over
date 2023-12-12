import pygame


def main():
    pygame.init()
    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)

    player_img = pygame.image.load('data/creature.png')
    player_sprite = pygame.sprite.Sprite()
    player_sprite.image = player_img
    down = False
    up = False
    right = False
    left = False
    running = True
    x, y = 0, 0
    v = 10
    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                down = True
            if event.type == pygame.KEYUP:
                up = True
            if event.type == pygame.K_LEFT:
                left = True
            if event.type == pygame.K_RIGHT:
                right = True
        if down:
            down = False
            screen.blit(player_sprite.image, (x, y + v))
        if up:
            up = False
            screen.blit(player_sprite.image, (x, y - v))
        if left:
            left = False
            screen.blit(player_sprite.image, (x - v, y))
        if right:
            right = False
            screen.blit(player_sprite.image, (x + v, y))
        pygame.display.flip()


if __name__ == '__main__':
    main()