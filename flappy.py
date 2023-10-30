import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# Game variables
gravity = 0.25
bird_movement = 0
score = 0
game_active = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
background_img = pygame.image.load("C:/Users/calma/OneDrive/Desktop/comms py/Imagesforvscode/pxfuel.jpg").convert()
bird_img = pygame.image.load("C:/Users/calma/OneDrive/Desktop/comms py/Imagesforvscode/wing.png").convert_alpha()
pipe_img = pygame.image.load("C:/Users/calma/OneDrive/Desktop/comms py/Imagesforvscode/pipes.png").convert_alpha()
#resize
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
bird_img = pygame.transform.scale(bird_img, (50, 50))
pipe_img = pygame.transform.scale(pipe_img, (80, 400))

# Bird rectangle
bird_rect = bird_img.get_rect(center=(50, HEIGHT // 2))

# Pipe variables
pipe_gap = 200
pipe_heights = [200, 300, 400]
pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)

# Game over text
game_over_img = pygame.image.load("/Users/calma/OneDrive/Desktop/comms py/Imagesforvscode/g0ver.png").convert_alpha()
game_over_rect = game_over_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#resize
game_over_img = pygame.transform.scale(game_over_img, (500, 200))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipes.clear()
                bird_rect.center = (50, HEIGHT // 2)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_height = random.choice(pipe_heights)
            bottom_pipe = pipe_img.get_rect(midtop=(WIDTH + 100, pipe_height))
            top_pipe = pipe_img.get_rect(midbottom=(WIDTH + 100, pipe_height - pipe_gap))
            pipes.append(bottom_pipe)
            pipes.append(top_pipe)

    # Update bird movement
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # Draw background
    screen.blit(background_img, (0, 0))

    if game_active:
        # Draw bird
        screen.blit(bird_img, bird_rect)

        # Update pipe positions
        pipes = [pipe for pipe in pipes if pipe.right > -50]
        for pipe in pipes:
            pipe.centerx -= 2

        # Draw pipes
        for pipe in pipes:
            if pipe.bottom >= HEIGHT:
                screen.blit(pipe_img, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_img, False, True)
                screen.blit(flip_pipe, pipe)

        # Collision detection
        if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
            game_active = False

        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                game_active = False

        # Score display
        for pipe in pipes:
            if pipe.centerx == bird_rect.centerx:
                score += 0.5
                break

        score_surface = pygame.font.Font(None, 40).render(str(int(score)), True, WHITE)
        score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)
    else:
        # Game over display
        screen.blit(game_over_img, game_over_rect)

    pygame.display.update()
    clock.tick(FPS)
#C:/Users/calma/OneDrive/Desktop/comms py/Imagesforvscode/Scape.jpg

#C:/Users/calma/OneDrive/Desktop/comms py/Imagesforvscode/Scape.png