import pygame
import sys

pygame.init()

# Screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
DARK_BLUE = (0, 0, 150)
DARK_GREEN = (0, 150, 0)
DARK_RED = (150, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 48)

# Function to draw button
def show_button(rect, text, color=BLUE, text_color=WHITE):
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

# Quiz questions
quiz = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": 0},
    {"question": "Which is a programming language?", "options": ["Python", "Snake", "Elephant", "Lion"], "answer": 0},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "Which planet is known as Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": 1},
    {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": 2},
]

# Option buttons
option_buttons = [pygame.Rect(100, 150 + i*60, 400, 50) for i in range(4)]

# Control buttons
play_button = pygame.Rect(150, 250, 120, 60)
quit_button = pygame.Rect(330, 250, 120, 60)

play_text = font.render("PLAY", True, WHITE)
try_again_text = font.render("Try Again", True, WHITE)
quit_text = font.render("QUIT", True, WHITE)

# Game variables
game_started = False
current_question = 0
score = 0
quiz_over = False

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # --- Check buttons in order: quiz_over first ---
            if quiz_over:
                # Try Again
                if play_button.collidepoint(event.pos):
                    quiz_over = False
                    game_started = True
                    current_question = 0
                    score = 0
                # Quit
                if quit_button.collidepoint(event.pos):
                    running = False

            elif not game_started:
                # PLAY button at start
                if play_button.collidepoint(event.pos):
                    game_started = True
                    current_question = 0
                    score = 0
                # Quit
                if quit_button.collidepoint(event.pos):
                    running = False

            elif game_started:
                # Check answer buttons
                for i, btn in enumerate(option_buttons):
                    if btn.collidepoint(event.pos):
                        if i == quiz[current_question]["answer"]:
                            score += 1
                        current_question += 1
                        if current_question >= len(quiz):
                            game_started = False
                            quiz_over = True

    # --- Draw UI ---
    if quiz_over:
        # Display final score
        result_text = title_font.render(f"Score: {score}/{len(quiz)}", True, BLACK)
        screen.blit(result_text, result_text.get_rect(center=(300, 150)))

        # Draw Try Again button
        pygame.draw.rect(screen, DARK_GREEN, play_button)
        screen.blit(try_again_text, try_again_text.get_rect(center=play_button.center))

        # Draw Quit button
        pygame.draw.rect(screen, DARK_RED, quit_button)
        screen.blit(quit_text, quit_text.get_rect(center=quit_button.center))

    elif not game_started:
        # Draw PLAY button at start
        pygame.draw.rect(screen, DARK_BLUE, play_button)
        screen.blit(play_text, play_text.get_rect(center=play_button.center))

        # Draw Quit button
        pygame.draw.rect(screen, DARK_RED, quit_button)
        screen.blit(quit_text, quit_text.get_rect(center=quit_button.center))

    elif game_started:
        # Display question
        question_text = font.render(quiz[current_question]["question"], True, BLACK)
        screen.blit(question_text, (50, 50))

        # Display options
        for i, option in enumerate(quiz[current_question]["options"]):
            show_button(option_buttons[i], option)

    pygame.display.flip()

pygame.quit()
sys.exit()
