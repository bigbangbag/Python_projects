import pygame
import sys

# Initialize pygame
pygame.init()

# Dynamic screen dimension
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle and Ball Dimensions
PADDLE_WIDTH = SCREEN_WIDTH // 80
PADDLE_HEIGHT = SCREEN_HEIGHT // 6
BALL_SIZE = SCREEN_WIDTH // 40

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

# Clock to control frame rate
clock = pygame.time.Clock()

# Ball properties
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx = 5  # Ball speed in x-direction
ball_dy = 5  # Ball speed in y-direction

# Paddle properties
player1 = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(SCREEN_WIDTH - 20 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Scores
player1_score = 0
player2_score = 0

# Font for displaying scores
font = pygame.font.Font(None, SCREEN_HEIGHT // 15)

# Function to draw all elements
def draw_elements():
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the center line
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Display scores
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(player2_text, (SCREEN_WIDTH - SCREEN_WIDTH // 4, 20))

# Main game loop
def main():
    global ball, ball_dx, ball_dy, player1_score, player2_score

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Touch input for mobile devices
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if mouse_x < SCREEN_WIDTH // 2:  # Player 1's side
                    if mouse_y < player1.centery:
                        player1.y -= PADDLE_HEIGHT // 2
                    elif mouse_y > player1.centery:
                        player1.y += PADDLE_HEIGHT // 2
                else:  # Player 2's side
                    if mouse_y < player2.centery:
                        player2.y -= PADDLE_HEIGHT // 2
                    elif mouse_y > player2.centery:
                        player2.y += PADDLE_HEIGHT // 2

        # Keyboard input for PC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= 6
        if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
            player1.y += 6
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= 6
        if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
            player2.y += 6

        # Ball movement
        ball.x += ball_dx
        ball.y += ball_dy

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_dy *= -1

        # Ball collision with paddles
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dx *= -1

        # Ball goes out of bounds
        if ball.left <= 0:
            player2_score += 1
            ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
            ball_dx *= -1
        if ball.right >= SCREEN_WIDTH:
            player1_score += 1
            ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
            ball_dx *= -1

        # Draw everything
        draw_elements()

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
