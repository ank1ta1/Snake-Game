from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def move(self):
        for sq_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[sq_num - 1].xcor()
            new_y = self.snakes[sq_num - 1].ycor()
            self.snakes[sq_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def add_segment(self, position):
        square = Turtle("square")
        square.penup()
        square.color("white")
        square.goto(position)
        self.snakes.append(square)

    def extend(self):
        self.add_segment(self.snakes[-1].position())


