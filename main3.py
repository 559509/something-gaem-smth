import turtle as t

def f():
  t.fd(5)
def l():
  t.lt(5)
def r():
  t.rt(5)
#def b():
  #t.bd(5)

wn = t.Screen()
wn.onkey(f, "Up")
wn.onkey(l, "Left")
wn.onkey(r, "Right")
#wn.onkey(b, "Down")
wn.listen()
wn.mainloop()