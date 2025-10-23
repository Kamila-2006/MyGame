import pygame
import sys


pygame.init()

window_size = (700, 700)
pygame.display.set_caption("MyGame")
screen = pygame.display.set_mode(window_size)

background = pygame.image.load("main_menu.png")
background = pygame.transform.scale(background, window_size)

DARK_TEAL = (37, 68, 68)
DEEP_STEEL = (57, 85, 96)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
LIGHT_BLUE = (100, 160, 255)
BLACK = (0, 0, 0)

title_font = pygame.font.Font(None, 90)
font = pygame.font.Font(None, 50)

title_text = "MyGame"
subtitle_text = "главное меню"
buttons = ["Новая игра", "Настройки", "Альбом", "Выход"]

def draw_title(surface):
    text_surf = title_font.render(title_text, True, DARK_TEAL)
    title_rect = text_surf.get_rect(center=(surface.get_width() // 2, 80))
    surface.blit(text_surf, title_rect)

def draw_subtitle(surface):
    text_surf = font.render(subtitle_text, True, DEEP_STEEL)
    subtitle_rect = text_surf.get_rect(center=(surface.get_width() // 2, 140))
    surface.blit(text_surf, subtitle_rect)

button_rects = []
start_y = 300
for i, text in enumerate(buttons):
    rect = pygame.Rect(250, start_y + i * 90, 200, 60)
    button_rects.append(rect)

running = True
while running:
    screen.blit(background, (0, 0))

    draw_title(screen)
    draw_subtitle(screen)

    mouse_pos = pygame.mouse.get_pos()
    for i, rect in enumerate(button_rects):
        color = GRAY if rect.collidepoint(mouse_pos) else LIGHT_BLUE
        pygame.draw.rect(screen, color, rect, border_radius=10)

        text_surface = font.render(buttons[i], True, LIGHT_BLUE) if rect.collidepoint(mouse_pos) \
            else font.render(buttons[i], True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_pos):
                    if buttons[i] == "Выход":
                        pygame.quit()
                        sys.exit()
                    else:
                        print(f"Нажата кнопка: {buttons[i]}")

    pygame.display.flip()