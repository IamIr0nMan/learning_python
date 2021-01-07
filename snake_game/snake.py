import turtle as t
import time

screen = t.Screen()
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for pos in START_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        tim = t.Turtle("square")
        tim.up()
        tim.color("white")
        tim.goto(pos)
        self.segments.append(tim)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
