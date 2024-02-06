import turtle
import random

class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        turtle.register_shape("/home/keldenpdrac/Desktop/space/enemy.gif")  # Register the enemy shape
        self.color("red")  # Set color of the enemy
        self.shape("/home/keldenpdrac/Desktop/space/enemy.gif")  # Set shape of the enemy
        self.penup()  # Lift the pen to avoid drawing lines
        x = random.randint(-450, 450)  # Generate random x-coordinate
        y = random.randint(180, 250)  # Generate random y-coordinate
        self.goto(x, y)  # Move enemy to random position
        self.speedamt = 5  # Set speed of the enemy

    def move_left(self):
        """
        Move the enemy to the left by its speed amount.
        """
        self.setx(self.xcor() - self.speedamt)  # Update x-coordinate to move left

    def move_right(self):
        """
        Move the enemy to the right by its speed amount.
        """
        self.setx(self.xcor() + self.speedamt)  # Update x-coordinate to move right

    def check_collision(self, bullet):
        """
        Check for collision between the enemy and a bullet.

        Parameters:
            bullet (Bullet): An instance of the Bullet class representing the bullet.

        Returns:
            bool: True if collision detected, False otherwise.
        """
        distance = self.distance(bullet)  # Calculate distance between enemy and bullet
        if distance < 20:  # Check if distance is less than the threshold
            return True  # Collision detected
        else:
            return False  # No collision
