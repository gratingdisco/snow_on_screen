import pygame
import random

# Инициализация Pygame
pygame.init()

# Получение разрешения экрана
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Создание окна с размером экрана
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Snowfall")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Класс для снежинок
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(-screen_height, 0)
        self.speed = random.randint(1, 3)
        self.size = random.randint(2, 5)

    def fall(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, screen_width)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

# Список для хранения снежинок
snowflakes = [Snowflake() for _ in range(200)]

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Заполнение экрана черным цветом
    screen.fill(BLACK)

    # Обновление положения снежинок и их отрисовка
    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()

    # Обновление дисплея
    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.Clock().tick(30)

# Завершение работы Pygame
pygame.quit()
