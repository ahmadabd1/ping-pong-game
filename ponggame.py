import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Set up the clock to control the game's frame rate
clock = pygame.time.Clock()

# Set up the initial position and velocity of the paddles and ball
paddle_width, paddle_height = 10, 60
paddle_speed = 5
paddle_left_pos = (height - paddle_height) // 2
paddle_right_pos = (height - paddle_height) // 2
ball_pos = [width // 2, height // 2]
ball_vel = [random.choice([-2, 2]), random.choice([-2, 2])]

# Set up the initial score
score_left = 0
score_right = 0

# Function to display the score on the screen
def show_score():
    font = pygame.font.SysFont("monospace", 36)
    score_text = font.render(
        str(score_left) + "   " + str(score_right), True, white)
    window.blit(score_text, (width // 2 - 18, 10))

# Main game loop
game_over = False
while not game_over:
    # Handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_left_pos > 0:
        paddle_left_pos -= paddle_speed
    if keys[pygame.K_s] and paddle_left_pos < height - paddle_height:
        paddle_left_pos += paddle_speed
    if keys[pygame.K_UP] and paddle_right_pos > 0:
        paddle_right_pos -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_right_pos < height - paddle_height:
        paddle_right_pos += paddle_speed

    # Update the ball's position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Check if the ball hits the top or bottom walls
    if ball_pos[1] >= height - 10 or ball_pos[1] <= 0:
        ball_vel[1] = -ball_vel[1]

    # Check if the ball hits the paddles
    if (paddle_left_pos <= ball_pos[1] <= paddle_left_pos + paddle_height and
            ball_pos[0] <= 20):
        ball_vel[0] = -ball_vel[0]
    if (paddle_right_pos <= ball_pos[1] <= paddle_right_pos + paddle_height and
            ball_pos[0] >= width - 30):
        ball_vel[0] = -ball_vel[0]

    # Check if the ball goes out of bounds
    if ball_pos[0] <= 0:
        score_right += 1
        ball_pos = [width // 2, height // 2]
    if ball_pos[0] >= width - 10:
        score_left += 1
        ball_pos = [width // 2, height // 2]

    # Fill the window with black color
    window.fill(black)

    # Draw the paddles and ball
    pygame.draw.rect(window, white, pygame.Rect(
        10, paddle_left_pos, paddle_width, paddle_height))
    pygame.draw.rect(window, white, pygame.Rect(
        width - paddle_width - 10, paddle_right_pos, paddle_width, paddle_height))
    pygame.draw.ellipse(window, white, pygame.Rect(
        ball_pos[0], ball_pos[1], 10, 10))
    pygame.draw.ellipse(window, white, pygame.Rect(
        ball_pos[0], ball_pos[1], 10, 10))

    # Update the game screen
    show_score()
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
