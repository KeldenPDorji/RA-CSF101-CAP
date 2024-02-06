# Import necessary libraries and modules
import turtle  # Graphics library
import random  # For generating random numbers
import math  # Math functions
import os  # Operating system functions
from pygame import mixer  # Sound library
from player import Player  # Player class
from enemy import Enemy  # Enemy class
from bullet import Bullet  # Bullet class
from score import Score  # Score class
import pygame.time  # For time-related functions

# Constants
BULLET_SPEED = 20  # Speed of bullets
ENEMY_SPEED = 2  # Speed of enemies
ENEMY_ASCEND_DISTANCE = 25  # Distance enemies move up when reaching screen edge
ENEMY_X_LIMIT = 425  # Horizontal limit for enemy movement
GAME_DURATION = 60  # Duration of the game in seconds

# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize the mixer for sound effects
mixer.init()

# Load sound files
sound_files = {
    "laser": os.path.join(script_dir, "SpaceInvaders_laser.wav"),  # Laser sound
    "explosion": os.path.join(script_dir, "SpaceInvaders_explosion.wav"),  # Explosion sound
    "gameover": os.path.join(script_dir, "SpaceInvaders_gameover.wav")  # Game over sound
}

# Setting up the screen
scr = turtle.Screen()
scr.setup(1000, 600, 0, 0)  # Set up screen size and position
scr.bgcolor("black")  # Set background color
scr.title("Space Invader Game")  # Set window title
scr.bgpic("dp.gif")  # Set background image

# Register the missile GIF as a custom shape for the bullet
turtle.register_shape("missile.gif")

# Initialize player, enemies, bullet, and score objects
p = Player()  # Create player object
enemies = [Enemy() for _ in range(8)]  # Create enemy objects
b = Bullet()  # Create bullet object
b.shape("missile.gif")  # Set bullet shape
b.color("white")  # Set bullet color
b.setheading(90)  # Set bullet initial direction (up)
b.speed = BULLET_SPEED  # Set bullet speed
s = Score()  # Create score object

# Function to calculate distance between two objects
def calculate_distance(a, b):
    return math.sqrt(abs(math.pow((a.xcor() - b.xcor()), 2) + math.pow((a.ycor() - b.ycor()), 2)))

# Function to handle bullet firing
def fire_bullet():
    if b.state == "Ready":
        b.state = "Fire"
        mixer.Sound(sound_files["laser"]).play()  # Play laser sound
        x = p.xcor()
        y = p.ycor() + 30
        b.goto(x, y)
        b.showturtle()

# Function to display menu and handle user input
def display_menu(final_score):
    highest_score = get_highest_score()
    mixer.Sound(sound_files["gameover"]).play()  # Play game over sound
    choice = turtle.textinput("Game Over", "Press 'y' to restart or 'n' to quit. Final Score: {}\nHighest Score: {}".format(final_score, highest_score))
    if choice.lower() == 'y':
        return True
    elif choice.lower() == 'n':
        turtle.bye()  # Close window
        return False
    else:
        return display_menu(final_score)

# Function to get the highest score from a file
def get_highest_score():
    try:
        with open("highest_score.txt", "r") as file:
            highest_score = int(file.read())
    except FileNotFoundError:
        highest_score = 0
    return highest_score

# Function to update the highest score in a file
def update_highest_score(score):
    with open("highest_score.txt", "w") as file:
        file.write(str(score))

# Function to reset the game
def reset_game():
    global game_over
    game_over = False

    # Reset player position
    p.goto(0, -250)
    p.showturtle()

    # Reset enemy positions
    for i, enemy in enumerate(enemies):
        x = random.randint(-300, 300)
        y = random.randint(-200 + i * 50, -150 + i * 50)
        enemy.goto(x, y)
        enemy.showturtle()

    # Reset score
    s.ScoreValue = 0
    s.pu()
    s.goto(-400, 260)
    s.pd()
    s.clear()
    s.write("Score: {}   Time: {}s".format(s.ScoreValue, GAME_DURATION), align="left", font=("Arial", 14, "bold"))

    # Reset bullet state
    b.hideturtle()
    b.state = "Ready"

    # Reset timer
    global start_time
    start_time = pygame.time.get_ticks()

    # Check that the bullet's state has been reset correctly
    assert b.state == "Ready"

# Function to restart the game
def restart_game():
    reset_game()
    turtle.listen()
    turtle.onkey(p.move_left, "Left")
    turtle.onkey(p.move_right, "Right")
    turtle.onkey(fire_bullet, "space")
    turtle.onkey(restart_game, "y")

# Check if this script is being run directly
if __name__ == "__main__":
    # Keybindings
    turtle.listen()
    turtle.onkey(p.move_left, "Left")
    turtle.onkey(p.move_right, "Right")
    turtle.onkey(fire_bullet, "space")
    turtle.onkey(restart_game, "y")

    # Game over flag
    game_over = False

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        restart_game()
        while not game_over:
            clock.tick(60)  # Set frame rate to 60 FPS

            # Calculate elapsed time in seconds
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

            # Display score and timer
            turtle.tracer(0, 0)  # Turn off animation updates
            s.clear()
            s.write("Score: {}   Time: {}s".format(s.ScoreValue, GAME_DURATION - elapsed_time),
                    align="left", font=("Arial", 14, "bold"))
            turtle.update()  # Update screen
            turtle.tracer(1, 10)  # Turn on animation updates

            # Enemy movement and collision detection
            for enemy in enemies:
                x = enemy.xcor()
                x += enemy.speedamt
                enemy.setx(x)

                if enemy.xcor() > ENEMY_X_LIMIT or enemy.xcor() < -ENEMY_X_LIMIT:
                    for j in enemies:
                        y = j.ycor()
                        y += ENEMY_ASCEND_DISTANCE
                        j.sety(y)
                    enemy.speedamt *= -1

                if calculate_distance(b, enemy) < 20:
                    b.hideturtle()
                    b.state = "Ready"
                    mixer.Sound(sound_files["explosion"]).play()
                    b.setposition(0, -400)
                    x = random.randint(-300, 300)
                    y = random.randint(-200, -150)
                    enemy.setposition(x, y)
                    s.ScoreValue += 10

                if calculate_distance(p, enemy) < 25:
                    for e in enemies:
                        e.hideturtle()
                    p.hideturtle()
                    highest_score = get_highest_score()
                    if s.ScoreValue > highest_score:
                        update_highest_score(s.ScoreValue)
                    s.pu()
                    s.goto(0, 0)
                    s.pd()
                    s.write("Game Over!   Final Score: {}   Highest Score: {}".format(s.ScoreValue, highest_score),
                            align="left", font=("Arial", 14, "bold"))
                    game_over = True
                    break

                if enemy.ycor() <= -200:
                    mixer.Sound(sound_files["gameover"]).play()
                    for j in enemies:
                        j.hideturtle()
                    p.hideturtle()
                    highest_score = get_highest_score()
                    if s.ScoreValue > highest_score:
                        update_highest_score(s.ScoreValue)
                    s.pu()
                    s.goto(0, 0)
                    s.pd()
                    s.write("Game Over!   Final Score: {}   Highest Score: {}".format(s.ScoreValue, highest_score),
                            align="left", font=("Arial", 14, "bold"))
                    game_over = True
                    break

            # Bullet movement
            if b.state == "Fire":
                y = b.ycor()
                y += b.speedamt
                b.sety(y)
                if b.ycor() > 300:
                    b.hideturtle()
                    b.state = "Ready"

            # Check if game time has reached 0 seconds
            if elapsed_time >= GAME_DURATION:
                highest_score = get_highest_score()
                if s.ScoreValue > highest_score:
                    update_highest_score(s.ScoreValue)
                s.pu()
                s.goto(0, 0)
                s.pd()
                s.write("Game Over!   Final Score: {}   Highest Score: {}".format(s.ScoreValue, highest_score),
                        align="left", font=("Arial", 14, "bold"))
                game_over = True

        # Display menu and handle user input
        if not display_menu(s.ScoreValue):
            break

    turtle.done()  # Finish and exit turtle graphics
