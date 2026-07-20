import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

num = 1_00
nx, ny = 0, 0  # Center of the screen
def point_to_origin(x, y):
    return nx - x, ny - y
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
}
matrix = {
    c2: {
        c1: random.randint(-1, 1) for c1 in colors.values()
    } for c2 in colors.values()
}
x_arr = [random.randint(-WIDTH//2, WIDTH//2) for _ in range(num)]
y_arr = [random.randint(-HEIGHT//2, HEIGHT//2) for _ in range(num)]
colors = [random.choice(list(colors.values())) for _ in range(num)]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        nx, ny = mx - WIDTH // 2, my - HEIGHT // 2
    else:
        ...
        # if random.random() > 0.99:
        #     angle = random.uniform(0, 2 * math.pi)
        #     nx = int(math.cos(angle) * 100)
        #     ny = int(math.sin(angle) * 100)

    screen.fill((0, 0, 0))

    for i in range(num):
        for j in range(num):
            if i != j:
                dx = x_arr[i] - x_arr[j]
                dy = y_arr[i] - y_arr[j]
                distance = math.hypot(dx, dy)
                if distance < 100 and distance > 0.01:
                    ux = dx / distance
                    uy = dy / distance
                    force = matrix[colors[i]][colors[j]] / (distance + 1)
                    x_arr[i] += force * ux
                    y_arr[i] += force * uy
                    x, y = point_to_origin(x_arr[i], y_arr[i])
                    x_arr[i] += max(10,((x/(1+math.hypot(x, y)))/10))
                    y_arr[i] += max(10,((y/(1+math.hypot(x, y)))/10))
            # x_arr[i] += random.randint(-1, 1)
            # y_arr[i] += random.randint(-1, 1)
            
    for i in range(num):
        pygame.draw.circle(
            screen,
            colors[i],
            (int(x_arr[i] + WIDTH//2), int(y_arr[i] + HEIGHT//2)),
            2
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()