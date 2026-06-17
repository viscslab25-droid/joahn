""" Crystal Growth

Start with a seed.

Particles:

Random walk.
Stick when touching crystal.

This is called Diffusion-Limited Aggregation (DLA).

Produces snowflake-like structures."""
import random, math,turtle,time
random.seed(1)
turtle.bgcolor("black")
turtle.tracer(0,0)
class Particle(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.scale = 1
        self.is_stone = False
        self.stone_rad = 10
        self.strength = 1e-1
        self.penup()    
        self.goto(x,y)
        self.shapesize(0.075,0.075)
        self.shape("circle")
        self.color("blue")
    
    def brownian(self,other:"Particle"):
        if not self.is_stone:
            if random.random() > 0.005 and other.is_stone:
                dx = other.x - self.x
                dy = other.y - self.y
                hyp = max(math.hypot(dx,dy),0.1)
                ux = dx/hyp
                uy = dy/hyp
                self.x += ux * self.strength * (1 - 1/hyp)
                self.y += uy * self.strength * (1 - 1/hyp)
            nx = random.choice([-1,0,1]) * self.scale
            ny = random.choice([-1,0,1]) * self.scale
            self.x = self.x + nx
            self.y = self.y + ny
            self.goto(self.x ,self.y )

    def crystal(self,other:"Particle"):
        if other.is_stone:
            dx = other.x - self.x
            dy = other.y - self.y
            hyp = math.hypot(dx,dy)
            if hyp < self.stone_rad:
                self.is_stone = True


turt:list[Particle] = []

for _ in range(10):
    if _ == 0:
        p = Particle(0,0)
        p.is_stone = True
        turt.append(p)

    p = Particle(random.randint(-500,500),random.randint(-500,500))
    turt.append(p)

max_len = len(turt)
c = cu = 0
t = time.time()
colors = ["blue","red","green","yellow","orange","purple","white"]
while True:
    num_turts = sum([1 for p in turt if not p.is_stone])
    if c % 500 == 0:
        cu += 1
    if num_turts < max_len:
        c+=10
        side = (100 + c)% 1000
        p = Particle(random.randint(-side,side),random.randint(-side,side))
        p.color(colors[(cu//10)%len(colors)])
        turt.append(p)
    for p in turt:
        p.clear()
        for o in turt:
            if p != o:

                p.brownian(o)
                p.crystal(o)
    if time.time() - t > 10:
        t = time.time()
    turtle.update()

turtle.done()