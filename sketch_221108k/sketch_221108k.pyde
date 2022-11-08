x=0
def setup():
    size(600,600)
def draw():
    translate(270,220)
    background(100)
    fill(random(0,255))
    rotate(radians(random(0,360)))
    ellipse(x,x,160,50)
x=x+1
