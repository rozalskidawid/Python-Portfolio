import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snek")

snake_pos = [[100, 50], [90, 50], [80, 50]]
food_pos = [400, 300]
direction = "RIGHT"

clock = pygame.time.Clock()

def collision_with_body(snake_pos):
    head = snake_pos[0]
    if head in snake_pos[1:]:
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    new_head = [snake_pos[0][0], snake_pos[0][1]]
    if direction == "RIGHT":
        new_head[0] += 10
    elif direction == "LEFT":
        new_head[0] -= 10
    elif direction == "UP":
        new_head[1] -= 10
    elif direction == "DOWN":
        new_head[1] += 10

    snake_pos.insert(0, new_head)

    if collision_with_body(snake_pos):
        running = False

    if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
        food_pos = [random.randrange(1, screen_width//10) * 10, random.randrange(1, screen_height//10) * 10]
    else:
        snake_pos.pop()

    if snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height:
        running = False

    screen.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    pygame.display.flip()

    clock.tick(15)

pygame.quit()
