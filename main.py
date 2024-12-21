import os
import sys
import random
import pygame

pygame.init()
pygame.display.set_caption('survival')
size = width, height = 1280, 720
pixsel = height // 720
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
pygame.font.init()
path = pygame.font.match_font("arial")
Font = pygame.font.Font(path, 25)


def load_image(name, puth, colorkey=None): ##Загрузка изображений
    fullname = os.path.join(f'files\\world{puth}', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображение "{fullname}" отсутствует')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Map:
    def __init__(self):
        self.x = 5000
        self.y = 5000

class Player(pygame.sprite.Sprite): ##Класс игрока
    image = load_image("forester.png", "\\player")

    def __init__(self, *group):
        super().__init__(*group)
        global pixsel
        self.image = Player.image
        self.image = pygame.transform.scale(self.image, (60 * pixsel, 60 * pixsel))
        self.rect = self.image.get_rect()
        self.run = [0, 0, 0, 0]
        self.x, self.y = 0, 0
        self.rect.x = width // 2
        self.rect.y = height // 2

    def update(self, *args):
        if args and args[0].type == pygame.KEYUP and pygame.key.name(args[0].key) == 'w':
            self.run[0] = 0
        if args and args[0].type == pygame.KEYDOWN and pygame.key.name(args[0].key) == 'w':
            self.run[0] = 1
        if args and args[0].type == pygame.KEYUP and pygame.key.name(args[0].key) == 's':
            self.run[1] = 0
        if args and args[0].type == pygame.KEYDOWN and pygame.key.name(args[0].key) == 's':
            self.run[1] = 1
        if args and args[0].type == pygame.KEYUP and pygame.key.name(args[0].key) == 'd':
            self.run[2] = 0
        if args and args[0].type == pygame.KEYDOWN and pygame.key.name(args[0].key) == 'd':
            self.run[2] = 1
        if args and args[0].type == pygame.KEYUP and pygame.key.name(args[0].key) == 'a':
            self.run[3] = 0
        if args and args[0].type == pygame.KEYDOWN and pygame.key.name(args[0].key) == 'a':
            self.run[3] = 1
        if self.run[0] == 1:
            self.y -= v // FPS
        if self.run[1] == 1:
            self.y += v // FPS
        if self.run[2] == 1:
            self.x += v // FPS
        if self.run[3] == 1:
            self.x -= v // FPS


class Blocks(pygame.sprite.Sprite): ## класс блока - елки
    image = load_image("tree.png", "\\blocks\\tree")
    image2 = load_image("stump.png", "\\blocks\\tree")

    def __init__(self, *group):
        super().__init__(*group)
        global pixsel
        self.image = Blocks.image
        self.image = pygame.transform.scale(self.image, (200 * pixsel, 200 * pixsel))
        self.rect = self.image.get_rect()
        w, h = self.rect.w, self.rect.h
        self.x = random.randrange(int(-0.5 * map.x), int(0.5 * map.x))
        self.y = random.randrange(int(-0.5 * map.y), int(0.5 * map.y))

    def update(self, *args):
        self.rect.x = self.x - player.x + 300 * pixsel
        self.rect.y = self.y - player.y - 200 * pixsel
        #if (self.rect.x + self.rect.w < 0 or self.rect.x - self.rect.w > 1280 * pixsel or
                #self.rect.y + self.rect.h < 0 or self.rect.y - self.rect.h > 720 * pixsel):
        if abs(self.rect.x - 640 * pixsel + 50) < 30 * pixsel and abs(self.rect.y - 360 * pixsel + 100) < 30 * pixsel:
            self.image = Blocks.image2
            self.image = pygame.transform.scale(self.image, (200 * pixsel, 200 * pixsel))



if __name__ == '__main__': ## Начало работы программы
    running = True
    map = Map()
    for i in range(800):
        Blocks(all_sprites)
    player = Player(all_sprites)
    FPS = 100
    v = 500
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
            if event.type == pygame.KEYDOWN:
                all_sprites.update(event)
            if event.type == pygame.KEYUP:
                all_sprites.update(event)
        screen.fill((100, 100, 100))
        clock.tick(FPS)
        all_sprites.draw(screen)
        all_sprites.update()
        screen.blit(Font.render(f'x: {player.x} y: {player.y}', 1, (255, 255, 255)), (10, 10))
        pygame.display.flip()
    pygame.quit()