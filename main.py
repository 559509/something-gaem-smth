#import

import turtle as t
wn = t.Screen()

#setup
t.speed(5)
detail = 5
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
colours = ["red", "blue", "green", "orange", "yellow", "purple", "black"]
thickness = 1

#functions

def det():
  global detail
  detail = int(input("pixels: "))
  return(detail)

def f():
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x, y + detail)

def l():
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x - detail, y)

def r():
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x + detail, y)

def b():
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x, y - detail)


def col():
  colour = input("colour: ")
  t.pencolor(colour)

def stop():
  temp = input("clear? (clears the screen and stops the program) y/n: ")
  if temp == "y":
    wn.clear()

def keybinds():
  print("Arrow keys to move \ndetail level: m \ncolour: n \npenup: b \npendown: v \nquit: p \nkeybinds: k \npen size: t")

def thickness():
  t.pensize(int(input("thickness: ")))
#executions
keybinds()
wn.onkey(f, "Up")
wn.onkey(l, "Left")
wn.onkey(r, "Right")
wn.onkey(b, "Down")
wn.onkey(det, "m")
wn.onkey(col, "n")
wn.onkey(t.penup, "b")
wn.onkey(t.pendown, "v")
wn.onkey(stop, "p")
wn.onkey(keybinds, "k")
wn.onkey(thickness, "t")

wn.listen()
wn.mainloop()