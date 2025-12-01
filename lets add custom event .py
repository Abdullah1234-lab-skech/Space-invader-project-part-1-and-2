import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Two Sprites with Custom Event")
WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
    def change_color(self):
        new_color = random.choice(colors)
        self.image.fill(new_color)
sprite1 = MySprite((255, 0, 0), 200, 200)
sprite2 = MySprite((0, 0, 255), 400, 200)
all_sprites = pygame.sprite.Group(sprite1, sprite2)
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
