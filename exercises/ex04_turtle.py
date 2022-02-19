"""This program displays the infamous buidlings of UNC using turtle and loads of code."""

__author__ = "730398535"

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.showturtle


def bell_tower(x: float, y: float) -> None:
    """Drawing the Infamous belltower of UNC."""
    # bottem step 1
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.forward(345)
    leo.left(90)
    leo.forward(15)
    leo.left(90)
    leo.forward(345)
    leo.left(90)
    leo.forward(15)
    # bottem step 2 
    leo.penup()
    leo.goto(15, -305)
    leo.pendown()
    leo.seth(0)
    leo.forward(315)
    leo.left(90)
    leo.forward(15)
    leo.left(90)
    leo.forward(315)
    leo.left(90)
    leo.forward(15)
    # bottem step 3
    leo.penup()
    leo.goto(30, -290)
    leo.pendown()
    leo.seth(0)
    leo.forward(285)
    leo.left(90)
    leo.forward(15)
    leo.left(90)
    leo.forward(285)
    leo.left(90)
    leo.forward(15)
    

def bell_tower_2(x: float, y: float) -> None:
    """Part 2 of the infamous Bell tower of UNC."""
    # main building 
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.seth(0)
    leo.color("tan")
    leo.forward(225)
    leo.left(90)
    leo.forward(120)
    leo.left(90)
    leo.forward(225)
    leo.left(90)
    leo.forward(120)
    

def tower_structure(x: float, y: float) -> None:    
   """Building the tower"""
    # tower building
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.seth(0)
    leo.forward(125)
    leo.left(90)
    leo.forward(330)
    leo.left(90)
    leo.forward(125)
    leo.left(90)
    leo.forward(330)


def bell_tower_crown(x: float, y: float) -> None:  
    """The Crown for the infamous bell tower."""
    i: int = 0
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.seth(0)
    while i < 3:
        leo.forward(155)
        leo.left(120)
        i += 1


def kenan_labs(x: float, y: float) -> None:
    """Drawing the most beautiful building at UNC."""
    i: int = 0
    # main building
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.seth(180)
    leo.color("grey")
    while i < 4:
        leo.forward(215)
        leo.right(90)
        i += 1
    # elevator tower
    leo.penup()
    leo.goto(-275, -65)
    leo.pendown()
    leo.seth(180)
    leo.forward(30)
    leo.right(90)
    leo.forward(230)
    leo.right(90)
    leo.forward(90)
    leo.right(90)
    leo.forward(45)
    # secondary tower
    leo.penup()
    leo.goto(-60, -35)
    leo.pendown()
    leo.seth(0)
    leo.forward(30)
    leo.left(90)
    leo.forward(170)
    leo.left(90)
    leo.forward(90)
    leo.left(90)
    leo.forward(15)
    # faux building 
    leo.penup()
    leo.goto(-215, 145)
    leo.pendown()
    leo.seth(0)
    leo.forward(145)
    leo.right(90)
    leo.forward(10)
    # billboard
    leo.penup()
    leo.goto(-300, 140)
    leo.pendown()
    style = ('Courier', 20, 'italic')
    leo.write('Kenan', font=style)


def fine_details(x: float, y: float) -> None:
    """Adding the finishing touches to my masterpeice."""
    leo.color("black")
    leo.penup()
    leo.goto(133, 117)
    leo.pendown()
    leo.fillcolor(75, 156, 211)
    leo.begin_fill()
    r = 40
    leo.circle(r)
    leo.end_fill()
    # windows para tower
    leo.penup()
    leo.goto(133, 47)
    leo.pendown()
    leo.color("black")
    i: int = 0
    while i < 4:
        leo.forward(18)
        leo.left(90)
        i += 1
    leo.penup()
    leo.goto(133, -27)
    leo.pendown()
    leo.seth(0)
    i = 0
    while i < 4:
        leo.forward(18)
        leo.left(90)
        i += 1
    leo.penup()
    leo.goto(133, -87)
    leo.pendown()
    leo.seth(0)
    i = 0
    while i < 4:
        leo.forward(18)
        leo.left(90)
        i += 1
    # windows opposite side
    leo.penup()
    leo.goto(193, 29)
    leo.pendown()
    i = 0
    while i < 4:
        leo.forward(18)
        leo.left(90)
        i += 1
    leo.penup()
    leo.goto(193, -27)
    leo.pendown()
    leo.seth(0)
    i = 0
    while i < 4:
        leo.forward(18)
        leo.left(90)
        i += 1
    leo.penup()
    leo.goto(193, -87)
    leo.pendown()
    leo.seth(0)
    i = 0
    while i < 4:
        leo.forward(18)
        leo.left(90)
        i += 1


def south_rd(x: float, y: float) -> None:
    """Drawing the highway for campus."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.seth(0)
    leo.forward(470)
    leo.penup()
    leo.forward(125)
    leo.pendown()
    leo.forward(120)
    leo.right(90)
    leo.forward(115)
    leo.right(90)
    leo.forward(70)
    leo.penup()
    leo.forward(225)
    leo.pendown()
    leo.forward(470)

       
def main() -> None:
    """...Picaso, I like it!"""
    bell_tower(0, -320)
    bell_tower_2(60, -275)
    tower_structure(110, -155)
    bell_tower_crown(95, 175)
    kenan_labs(-60, -95)
    fine_details(117, 87)
    south_rd(-360, -125)
    done()
    

if __name__ == "__main__":
    print("")

