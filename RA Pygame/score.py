import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.color("white")  # Set color of the score display
        self.speed(0)  # Set speed of the turtle animation
        self.ScoreValue = 0  # Initialize score value
        self.penup()  # Lift the pen to avoid drawing lines
        self.setposition(-350, 250)  # Set initial position of the score display
        self.write("Score: {}".format(self.ScoreValue), align="left", font=("Arial", 14, "bold"))  # Display initial score
        self.hideturtle()  # Hide the turtle pointer

    def update_score(self):
        """
        Update the score display with the current score value.
        """
        self.clear()  # Clear the previous score display
        self.write("Score: {}".format(self.ScoreValue), align="left", font=("Arial", 14, "bold"))  # Write the updated score

    def increase_score(self, points):
        """
        Increase the score by the given points and update the score display.

        Parameters:
            points (int): The number of points to increase the score by.
        """
        self.ScoreValue += points  # Increase the score by the given points
        self.update_score()  # Update the score display with the new score value
