import pygame
import sys
import random
import os

pygame.init()

# --- Resource Path Fix for PyInstaller ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")

# Colors
LIGHT_GRAY = (211, 211, 211)
BLACK = (50, 30, 20)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (76, 187, 23)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)

# Fonts
font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 48)
big_title_font = pygame.font.SysFont(None, 60)   # for "IT'S QUIZ TIME"
about_font = pygame.font.SysFont(None, 28)

# Function to draw button
def draw_button(rect, text, color, hover_color=None, text_color=WHITE):
    mouse_pos = pygame.mouse.get_pos()
    if hover_color and rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, rect)
    else:
        pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

# Quiz questions (10)
quiz = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": 0},
    {"question": "Which is a programming language?", "options": ["Python", "Snake", "Elephant", "Lion"], "answer": 0},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "Which planet is known as Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": 1},
    {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": 2},
    {"question": "Which country is known for sushi?", "options": ["Japan", "China", "Korea", "Thailand"], "answer": 0},
    {"question": "What is H2O?", "options": ["Water", "Oxygen", "Hydrogen", "Helium"], "answer": 0},
    {"question": "Which gas do plants need?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": 1},
    {"question": "Which is a mammal?", "options": ["Shark", "Dolphin", "Octopus", "Penguin"], "answer": 1},
    {"question": "Which is a fruit?", "options": ["Carrot", "Apple", "Lettuce", "Potato"], "answer": 1},
]

# --- Shuffle options inside each question ---
for q in quiz:
    options = q["options"]
    answer_index = q["answer"]
    correct_answer = options[answer_index]

    random.shuffle(options)  # shuffle order
    q["answer"] = options.index(correct_answer)  # fix correct answer index

# Option buttons
option_buttons = [pygame.Rect(200, 150 + i*60, 500, 50) for i in range(4)]

# Control buttons
back_button = pygame.Rect(50, 500, 120, 50)
submit_button = pygame.Rect(330, 500, 120, 50)
quit_button = pygame.Rect(610, 500, 120, 50)
play_button = pygame.Rect(340, 370, 120, 50)
try_button = pygame.Rect(340, 400, 120, 50)

# --- NEW buttons for About screen ---
about_button = pygame.Rect(85, 500, 120, 50)
about_back_button = pygame.Rect(340, 500, 120, 50)

# Game variables
game_started = False
current_question = 0
score = 0
quiz_over = False
selected_option = None
user_answers = [None]*len(quiz)
show_about = False   # <--- NEW state

# --- Load GIF for welcome screen (first frame only for now) ---
welcome_gif = pygame.image.load(resource_path("gif_frames/frame_0.gif")).convert_alpha()
welcome_gif = pygame.transform.scale(welcome_gif, (200, 200))  # resize if needed

running = True
while running:
    screen.fill(LIGHT_GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quiz_over:
                if try_button.collidepoint(event.pos):
                    quiz_over = False
                    game_started = True
                    current_question = 0
                    score = 0
                    user_answers = [None]*len(quiz)
                    random.shuffle(quiz)  # shuffle quiz
                if quit_button.collidepoint(event.pos):
                    running = False

            elif not game_started and not show_about:
                if play_button.collidepoint(event.pos):
                    game_started = True
                    current_question = 0
                    score = 0
                    user_answers = [None]*len(quiz)
                    random.shuffle(quiz)  # shuffle quiz
                if quit_button.collidepoint(event.pos):
                    running = False
                if about_button.collidepoint(event.pos):
                    show_about = True   # go to about screen

            elif show_about:
                if about_back_button.collidepoint(event.pos):
                    show_about = False  # back to main menu

            elif game_started:
                # Option selection via circles
                for i, btn in enumerate(option_buttons):
                    circle_center = (btn.x + 20, btn.y + btn.height // 2)
                    circle_rect = pygame.Rect(circle_center[0]-15, circle_center[1]-15, 30, 30)
                    if circle_rect.collidepoint(event.pos):
                        selected_option = i
                        user_answers[current_question] = i

                # Submit button
                if submit_button.collidepoint(event.pos) and selected_option is not None:
                    if user_answers[current_question] == quiz[current_question]["answer"]:
                        score += 1
                    selected_option = None
                    current_question += 1
                    if current_question >= len(quiz):
                        game_started = False
                        quiz_over = True
              
                # Back button
                if back_button.collidepoint(event.pos):
                    if current_question > 0:
                        current_question -= 1
                        if user_answers[current_question] == quiz[current_question]["answer"]:
                            score -= 1
                        selected_option = user_answers[current_question]

                # Quit button
                if quit_button.collidepoint(event.pos):
                   running = False

    # Draw UI
    if quiz_over:
        result_text = title_font.render(f"Score: {score}/{len(quiz)}", True, BLACK)
        screen.blit(result_text, result_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50)))
        
        got_score = (score / len(quiz)) * 100
        if got_score < 70:
            message = "Sorry, you didn't pass"
            message_color = RED
        else:
            message = "Congrats, you passed"
            message_color = BLUE

        message_surface = font.render(message, True, message_color)
        message_rect = message_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
        screen.blit(message_surface, message_rect)

        draw_button(try_button, "Try Again", BLUE, LIGHT_BLUE)
        draw_button(quit_button, "QUIT", RED, LIGHT_BLUE)

    elif not game_started and not show_about:
        # Title text above GIF
        title_text = big_title_font.render("IT'S QUIZ TIME", True, BLUE)
        screen.blit(title_text, title_text.get_rect(center=(WIDTH//2, 80)))

        # Show welcome GIF (first frame)
        screen.blit(welcome_gif, (WIDTH//2 - 100, 150))

        draw_button(play_button, "PLAY", BLUE, LIGHT_BLUE, WHITE)
        draw_button(about_button, "ABOUT", GREEN, LIGHT_BLUE, WHITE)
        draw_button(quit_button, "QUIT", RED , LIGHT_BLUE, WHITE)

    elif show_about:
        about_lines = [
             "Welcome to the Quiz Game!",
             "This game will test your knowledge with fun questions.",
             "You’ll be given four options for each question.",
             "Try to get at least 70% to pass the quiz.",
             "Good luck and enjoy playing!",
             "Developed by: Daryl Hans Ocao"
        ]
        y = 150
        for line in about_lines:
            text = about_font.render(line, True, BLACK)
            screen.blit(text, (80, y))
            y += 50

        draw_button(about_back_button, "BACK", BLUE, LIGHT_BLUE, WHITE)

    elif game_started:
        # Display question
        question_text = font.render(quiz[current_question]["question"], True, BLACK)
        screen.blit(question_text, (50, 50))

        # Display options with small circles
        for i, option in enumerate(quiz[current_question]["options"]):
            btn = option_buttons[i]
            pygame.draw.rect(screen, GRAY, btn, border_radius=5)
            circle_center = (btn.x + 20, btn.y + btn.height // 2)
            pygame.draw.circle(screen, BLUE if selected_option == i else WHITE, circle_center, 12)
            pygame.draw.circle(screen, BLACK, circle_center, 12, 2)
            text_surf = font.render(option, True, BLACK)
            screen.blit(text_surf, (btn.x + 50, btn.y + btn.height//2 - text_surf.get_height()//2))

        draw_button(back_button, "BACK", BLUE, LIGHT_BLUE)
        draw_button(submit_button, "SUBMIT", GREEN, LIGHT_BLUE)
        draw_button(quit_button, "QUIT", RED, LIGHT_BLUE)

    pygame.display.flip()

pygame.quit()
sys.exit()
