import pygame
import sys


pygame.init()
clock = pygame.time.Clock()

window_size = (700, 700)
pygame.display.set_caption("MyGame")
screen = pygame.display.set_mode(window_size)

background = pygame.image.load("main_menu.png")
background = pygame.transform.scale(background, window_size)

confirm_exit = False

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

    if confirm_exit:
        exit_window = pygame.draw.rect(screen, (240, 240, 240), (200, 250, 300, 200), border_radius=15)
        exit_text = font.render("Точно выйти?", True, BLACK)
        exit_rect = exit_text.get_rect(center=(350, 300))
        screen.blit(exit_text, exit_rect)

        yes_rect = pygame.Rect(230, 370, 100, 50)
        pygame.draw.rect(screen, LIGHT_BLUE if yes_rect.collidepoint(mouse_pos) else GRAY, yes_rect, border_radius=10)
        yes_text = font.render("Да", True, BLACK)
        yes_text_rect = yes_text.get_rect(center=yes_rect.center)
        screen.blit(yes_text, yes_text_rect)

        no_rect = pygame.Rect(370, 370, 100, 50)
        pygame.draw.rect(screen, LIGHT_BLUE if no_rect.collidepoint(mouse_pos) else GRAY, no_rect, border_radius=10)
        no_text = font.render("Нет", True, BLACK)
        no_text_rect = no_text.get_rect(center=no_rect.center)
        screen.blit(no_text, no_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_pos):
                    if buttons[i] == "Выход":
                        confirm_exit = True
                    else:
                        print(f"Нажата кнопка: {buttons[i]}")

    pygame.display.flip()
    clock.tick(60)