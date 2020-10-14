import time
import random
import pygame
import sys


def T_square(side, screen, x_center, y_center, index, colors):
    if side >= 1:
        (x_top_left, y_top_left) = (x_center - side // 2, y_center - side // 2)
        (x_top_right, y_top_right) = (x_center + side // 2, y_center - side // 2)
        (x_bottom_left, y_bottom_left) = (x_center - side // 2, y_center + side // 2)
        (x_bottom_right, y_bottom_right) = (x_center + side // 2, y_center + side // 2)

        T_square(side // 2, screen, x_top_left, y_top_left, (index + 1) % len(colors), colors)
        T_square(side // 2, screen, x_top_right, y_top_right, (index + 1) % len(colors), colors)
        T_square(side // 2, screen, x_bottom_left, y_bottom_left, (index + 1) % len(colors), colors)
        T_square(side // 2, screen, x_bottom_right, y_bottom_right, (index + 1) % len(colors), colors)

        pygame.draw.rect(screen, colors[index], (x_center - side // 2, y_center - side // 2, side, side))
        pygame.display.update()


def main():
    pygame.init()

    screen_width = 800
    screen_height = 800

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("T_square")

    # Red, Orange, Yellow, Green, Blue, Indigo and Violet.

    black = (0, 0, 0)

    red = (255, 0, 0)
    orange = (255, 128, 0)
    yellow = (253, 201, 17)

    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    indigo = (75, 0, 130)
    violet = (238, 130, 238)

    x = screen_width // 2
    y = screen_height // 2
    side = 400

    colors = [red, orange, yellow, green, blue, indigo, violet]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)

        T_square(side, screen, x, y, random.randint(0, len(colors) - 1), colors)

        time.sleep(3)


if __name__ == '__main__':
    main()