import os
import sys
import pygame
import random

pygame.init()
pygame.display.set_caption('Boom them all')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('ls4\\data', name)
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


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image_boom
        self.rect = self.image.get_rect()
        w, h = self.rect.w, self.rect.h
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w, width - w)
        self.rect.y = random.randrange(h, height - h)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


if __name__ == '__main__':
    running = True
    for i in range(20):
        Bomb(all_sprites)
    FPS = 50
    v = 50
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        screen.fill((0, 0, 0))
        clock.tick(FPS)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
    pygame.quit()