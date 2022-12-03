import pygame


pygame.init()

FPS = 60
clock = pygame.time.Clock()

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode(
    (SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN)
)

pygame.display.set_caption("Level Editor")


# load images
pine1_img = pygame.image.load("img_level_editor/Background/pine1.png").convert_alpha()
pine2_img = pygame.image.load("img_level_editor/Background/pine2.png").convert_alpha()
mountain_img = pygame.image.load(
    "img_level_editor/Background/mountain.png"
).convert_alpha()
sky_img = pygame.image.load("img_level_editor/Background/sky_cloud.png").convert_alpha()

bg_1 = pygame.image.load("img_level_editor/Background/bg_1.png").convert_alpha()
bg_2 = pygame.image.load("img_level_editor/Background/bg_2.png").convert_alpha()
bg_3 = pygame.image.load("img_level_editor/Background/bg_3.png").convert_alpha()
bg_4 = pygame.image.load("img_level_editor/Background/bg_4.png").convert_alpha()
bg_5 = pygame.image.load("img_level_editor/Background/bg_5.png").convert_alpha()
bg_6 = pygame.image.load("img_level_editor/Background/bg_6.png").convert_alpha()


# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 25, 25)

# define game variables
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


# function for drawing background
def draw_bg():
    screen.fill(BLACK)
    width = bg_1.get_width()
    for x in range(4):
        screen.blit(bg_6, ((x * width) - scroll * 0.5, 0))
        screen.blit(bg_5, ((x * width) - scroll * 0.6, -5))
        screen.blit(bg_4, ((x * width) - scroll * 0.7, -2))
        screen.blit(bg_2, ((x * width) - scroll * 0.8, -7))


run = True
while run:
    clock.tick(FPS)

    draw_bg()

    # scroll the map
    if scroll_left is True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right is True:
        scroll += 5 * scroll_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

    pygame.display.update()
