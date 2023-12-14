import os
import sys
import pygame

pygame.init()
pygame.key.set_repeat(200, 70)

FPS = 50
WIDTH = 400
HEIGHT = 300
STEP = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    # С‡РёС‚Р°РµРј СѓСЂРѕРІРµРЅСЊ, СѓР±РёСЂР°СЏ СЃРёРјРІРѕР»С‹ РїРµСЂРµРІРѕРґР° СЃС‚СЂРѕРєРё
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # Рё РїРѕРґСЃС‡РёС‚С‹РІР°РµРј РјР°РєСЃРёРјР°Р»СЊРЅСѓСЋ РґР»РёРЅСѓ
    max_width = max(map(len, level_map))

    # РґРѕРїРѕР»РЅСЏРµРј РєР°Р¶РґСѓСЋ СЃС‚СЂРѕРєСѓ РїСѓСЃС‚С‹РјРё РєР»РµС‚РєР°РјРё ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # РІРµСЂРЅРµРј РёРіСЂРѕРєР°, Р° С‚Р°РєР¶Рµ СЂР°Р·РјРµСЂ РїРѕР»СЏ РІ РєР»РµС‚РєР°С…
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Р—РђРЎРўРђР’РљРђ", "",
                  "РџСЂР°РІРёР»Р° РёРіСЂС‹",
                  "Р•СЃР»Рё РІ РїСЂР°РІРёР»Р°С… РЅРµСЃРєРѕР»СЊРєРѕ СЃС‚СЂРѕРє,",
                  "РїСЂРёС…РѕРґРёС‚СЃСЏ РІС‹РІРѕРґРёС‚СЊ РёС… РїРѕСЃС‚СЂРѕС‡РЅРѕ"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # РЅР°С‡РёРЅР°РµРј РёРіСЂСѓ
        pygame.display.flip()
        clock.tick(FPS)


tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}
player_image = load_image('mario.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)


class Camera:
    # Р·Р°РґР°РґРёРј РЅР°С‡Р°Р»СЊРЅС‹Р№ СЃРґРІРёРі РєР°РјРµСЂС‹ Рё СЂР°Р·РјРµСЂ РїРѕР»СЏ РґР»СЏ РІРѕР·РјРѕР¶РЅРѕСЃС‚Рё СЂРµР°Р»РёР·Р°С†РёРё С†РёРєР»РёС‡РµСЃРєРѕРіРѕ СЃРґРІРёРіР°
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size

    # СЃРґРІРёРЅСѓС‚СЊ РѕР±СЉРµРєС‚ obj РЅР° СЃРјРµС‰РµРЅРёРµ РєР°РјРµСЂС‹
    def apply(self, obj):
        obj.rect.x += self.dx
        # РІС‹С‡РёСЃР»РёРј РєРѕРѕСЂРґРёРЅР°С‚Сѓ РєР»РёС‚РєРё, РµСЃР»Рё РѕРЅР° СѓРµС…Р°Р»Р° РІР»РµРІРѕ Р·Р° РіСЂР°РЅРёС†Сѓ СЌРєСЂР°РЅР°
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * obj.rect.width
        # РІС‹С‡РёСЃР»РёРј РєРѕРѕСЂРґРёРЅР°С‚Сѓ РєР»РёС‚РєРё, РµСЃР»Рё РѕРЅР° СѓРµС…Р°Р»Р° РІРїСЂР°РІРѕ Р·Р° РіСЂР°РЅРёС†Сѓ СЌРєСЂР°РЅР°
        if obj.rect.x >= (self.field_size[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
        obj.rect.y += self.dy
        # РІС‹С‡РёСЃР»РёРј РєРѕРѕСЂРґРёРЅР°С‚Сѓ РєР»РёС‚РєРё, РµСЃР»Рё РѕРЅР° СѓРµС…Р°Р»Р° РІРІРµСЂС… Р·Р° РіСЂР°РЅРёС†Сѓ СЌРєСЂР°РЅР°
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * obj.rect.height
        # РІС‹С‡РёСЃР»РёРј РєРѕРѕСЂРґРёРЅР°С‚Сѓ РєР»РёС‚РєРё, РµСЃР»Рё РѕРЅР° СѓРµС…Р°Р»Р° РІРЅРёР· Р·Р° РіСЂР°РЅРёС†Сѓ СЌРєСЂР°РЅР°
        if obj.rect.y >= (self.field_size[1]) * obj.rect.height:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

    # РїРѕР·РёС†РёРѕРЅРёСЂРѕРІР°С‚СЊ РєР°РјРµСЂСѓ РЅР° РѕР±СЉРµРєС‚Рµ target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


start_screen()

player, level_x, level_y = generate_level(load_level("levelex.txt"))
camera = Camera((level_x, level_y))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= STEP
            if event.key == pygame.K_RIGHT:
                player.rect.x += STEP
            if event.key == pygame.K_UP:
                player.rect.y -= STEP
            if event.key == pygame.K_DOWN:
                player.rect.y += STEP

    camera.update(player)

    for sprite in all_sprites:
        camera.apply(sprite)

    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

terminate()