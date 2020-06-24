import turtle
import random

wn=turtle.Screen()
wn.tracer(0)
wn.setup(width=800, height=400)



def board_setup():
    global in_game
    in_game=False
    arr=[2, 3, 4, 4, 5]
    board=[[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]
    ship_counter=0
    counter=0

    while ship_counter!=5:
        direction_num=random.randint(1, 2)
        if direction_num==1:
            column=random.randint(0, 9)
            row=random.randint(0, 10-(arr[counter]))
        else:
            column=random.randint(0, 10-(arr[counter]))
            row=random.randint(0, 9)
        
        for i in range(arr[counter]):
            if direction_num==1:
                if board[column][row+i]==0:
                    board[column][row+i]=arr[counter]
                else:
                    ship_counter-=1
                    counter-=1
                    break


            else:
                if board[column+i][row]==0:
                    board[column+i][row]=arr[counter]
                else:
                    ship_counter-=1
                    counter-=1
                    break
        counter+=1
        ship_counter+=1
        for i in board:
            print (i)
        print ("")

    for i in board:
        print (i)
            
board_setup()

k=0
colors=["red", "green", "blue", "orange", "purple"]
class Ship (turtle.Turtle):
    def __init__(self):
        global k
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color(colors[k])
        self.speed(0)
        k+=1



ships_o=[]
ships_e=[]
ship1=Ship()
ship1.shapesize(stretch_wid=4, stretch_len=2)
ships_e.append(ship1)
ship2=Ship()
ship2.shapesize(stretch_wid=6, stretch_len=2)
ships_o.append(ship2)
ship3=Ship()
ship3.shapesize(stretch_wid=8, stretch_len=2)
ships_e.append(ship3)
ship4=Ship()
ship4.shapesize(stretch_wid=8, stretch_len=2)
ships_e.append(ship4)
ship5=Ship()
ship5.shapesize(stretch_wid=10, stretch_len=2)
ships_o.append(ship5)


checkbox=turtle.Turtle()
checkbox.shape("square")
checkbox.color("green")
checkbox.goto(0, 180)

class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.pendown()
        self.shape("triangle")
        self.color("black")
        self.speed(0)
        self.hideturtle()
    

pen=Pen()
pen.width(3)
pen.goto(0, -200)
pen.goto(0, 200)
grid=Pen()
grid.penup()
grid.goto(-400, 200)
grid.pendown()
for i in range (5):
    grid.forward(800)
    grid.right(90)
    grid.forward(40)
    grid.right(90)
    grid.forward(800)
    grid.left(90)
    grid.forward(40)
    grid.left(90)
grid.forward(800)
grid.left(90)
for i in range (10):
    grid.forward(400)
    grid.left(90)
    grid.forward(40)
    grid.left(90)
    grid.forward(400)
    grid.right(90)
    grid.forward(40)
    grid.right(90)
grid.forward(400)

def p(x, y):
    ok_positions=True
    global in_game
    in_game=True
    
    for ship in ships_o:
        x=ship.xcor()+20
        x=(int(round(x/40.0)*40)-20)
        y=ship.ycor()+20
        y=(int(round(y/40.0)*40)-20)
        ship.goto(x, y)
        print (ship.shapesize()[0])#
        
    for ship in ships_e:
        x=ship.xcor()+20
        x=(int(round(x/40.0)*40)-20)
        y=ship.ycor()
        y=(int(round(y/40.0)*40))
        ship.goto(x, y)
        print (ship.shapesize()[0])#
    
    checkbox.goto(1000, 1000)
    for ship in ships_e:
        ship.stamp()
        ship.goto(1000, 1000)
    for ship in ships_o:
        ship.stamp()
        ship.goto(1000, 1000)


if in_game==False:
    wn.listen()
    ship5.ondrag(ship5.goto)
    ship4.ondrag(ship4.goto)
    ship3.ondrag(ship3.goto)
    ship2.ondrag(ship2.goto)
    ship1.ondrag(ship1.goto)
    checkbox.onclick(p)


        
while True:
    wn.update()














    
