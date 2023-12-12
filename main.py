import pygame


def main():
    pygame.init()
    size = width, height = 300, 300
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
        pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_DOWN:
                    down = True
                if event.key == pygame.K_UP:
                    up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_DOWN:
                    down = False
                if event.key == pygame.K_UP:
                    up = False
        if down:
            y += v
        if up:
            y -= v
        if left:
            x -= v
        if right:
            x += v
        screen.blit(player_sprite.image, (x, y))
        pygame.display.flip()


if __name__ == '__main__':
    main()