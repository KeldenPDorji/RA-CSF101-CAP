import turtle

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        turtle.register_shape("missile.gif")  # Register the bullet shape
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, -240)  # Position the bullet below the player
        self.speedamt = 40  # Initial speed of the bullet
        self.state = "Ready"  # State of the bullet (Ready to fire or not)

    def check_collision(self, enemy):
        """
        Check for collision between the bullet and an enemy.

        Parameters:
            enemy (Enemy): An instance of the Enemy class.

        Returns:
            bool: True if collision detected, False otherwise.
        """
        distance = self.distance(enemy)  # Calculate distance between bullet and enemy
        if distance < 20:  # Check if distance is less than the threshold
            return True  # Collision detected
        else:
            return False  # No collision
