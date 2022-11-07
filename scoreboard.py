from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.csv") as data :
            self.highscore = int(data.read())
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center", font=("arial", 15, "bold"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.csv", mode= "w") as data :
                data.write(f"{self.highscore}")

        self.score = 0
        self.updatescore()

    def increase_score(self):
        self.score+=1
        self.updatescore()

