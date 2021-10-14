from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.increase_score_board()

    def increase_score_board(self):
        self.write(f"Score: {self.score}", align = ALLIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.increase_score_board()
    def final(self):
        self.clear()
        self.write(f"Final Score: {self.score}", align=ALLIGNMENT, font=FONT)