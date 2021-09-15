class Shape:
    def __init__(self, turtle, x, y, color='black', fill=False):
        raise NotImplementedError("Shape must be subclassed")
    def _draw(self, x, y):
        raise NotImplementedError("Shape must be subclassed")
def goto(turtle, x, y):
    turtle.up()
    turtle.setx(x)
    turtle.sety(y)
    turtle.down()
class Rect(Shape):
    def __init__(self, turtle, x,y,width, height, color='black', fill=False):
        self.x = x
        self.fill=fill
        self.y = y
        self.width = width
        self.height = height
        self.t = turtle
        self.color = color
        self.t.color(self.color)
        self._draw(x,y, width, height)
    def _draw(self, x,y, width, height):
        goto(self.t, x, y)
        if self.fill: self.t.begin_fill()
        for i in range(2):
            self.t.fd(self.width)
            self.t.rt(90)
            self.t.fd(self.height)
            self.t.rt(90)
        self.t.end_fill()
class Circle(Shape):
    def __init__(self, turtle, x, y, radius, color, fill=False):
        self.x = x
        self.fill=fill
        self.y = y
        self.t = turtle
        self.color = color
        self.t.color(self.color)
        self.radius = radius
        self._draw(self.x, self.y, self.radius)
    def _draw(self, x, y, radius):
        goto(self.t, x, y)
        if self.fill:self.t.begin_fill()
        self.t.circle(radius)
        self.t.end_fill()
