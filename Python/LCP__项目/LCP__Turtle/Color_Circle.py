import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red","yellow","blue","green","pink","orange","purple"]
for x in range(100):
    t.color(colors[x%7])
    t.circle(x)
    t.left(60)















turtle.mainloop()