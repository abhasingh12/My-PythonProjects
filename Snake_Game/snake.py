from turtle import Screen, Turtle
positions = [(0,0), (-20,0), (-40,0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments= []
        self.create_snake()
        self.head = self.segments[0]
#create Snake
    def create_snake(self):
        for pos in positions:
            self.add_segment(pos)

    def add_segment(self,pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].pos())


#move snake
    def move(self):
        for seg in range(len(self.segments)-1, 0, -1 ):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(move_distance)


#control snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)



