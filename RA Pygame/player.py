import turtle
from bullet import Bullet  # Import the Bullet class

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        turtle.register_shape("player.gif")  # Register the player shape
        self.color("blue")  # Set player color
        self.speed(0)  # Set player speed
        self.shape("player.gif")  # Set player shape
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, -250)  # Initial position of the player
        self.bullet = None  # Initialize bullet attribute to None
        self.playerspeed = 40  # Player movement speed

    def move_left(self):
        """
        Move the player left by a fixed amount.

        Checks if the player reaches the left boundary before moving.

        """
        x = self.xcor()  # Get current x-coordinate
        x -= self.playerspeed  # Move left by player speed
        if x < -450:  # Check if player reaches left boundary
            x = -450  # Set x-coordinate to left boundary
        self.setx(x)  # Update player position

    def move_right(self):
        """
        Move the player right by a fixed amount.

        Checks if the player reaches the right boundary before moving.

        """
        x = self.xcor()  # Get current x-coordinate
        x += self.playerspeed  # Move right by player speed
        if x > 450:  # Check if player reaches right boundary
            x = 450  # Set x-coordinate to right boundary
        self.setx(x)  # Update player position

    def fire_bullet(self):
        """
        Create and fire a new bullet from the player's position.

        Returns:
            Bullet: Instance of the Bullet class representing the fired bullet.

        """
        new_bullet = Bullet()  # Create a new bullet object
        new_bullet.goto(self.xcor(), self.ycor() + 30)  # Position the bullet above the player
        new_bullet.state = "Fire"  # Set bullet state to "Fire"
        return new_bullet  # Return the new bullet object
