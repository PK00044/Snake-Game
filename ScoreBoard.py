from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open('data.txt') as file:
            self.hs = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.hs}", align=ALIGNMENT, font=FONT)

    def highscore(self):
        if self.score > self.hs:
            self.hs = self.score

            with open('data.txt', mode='w') as data:
                data.write(f"{self.hs}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
    #     self.hs = self.score

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
