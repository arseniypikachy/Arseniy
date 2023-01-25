w=0
s=0
def setup():
    size(600,600)
#def draw():
#    background(0)
#    if keyPressed:
#        if key == 'q':
#            text(u"q",0,300)
#        if key == 'w':
#            text(u"w",10,300)
#        if key == 'e':
#            text(u"e",20,300)
#        if key == 'r':
#            text(u"r",30,300)
#        if key == 't':
#            text(u"t",40,300)
#        if key == 'y':
#            text(u"y",50,300)
#        if key == 'u':
#            text(u"u",60,300)
#        if key == 'i':
#            text(u"i",70,300)
#        if key == 'o':
#            text(u"o",80,300)
#        if key == 'p':
#            text(u"p",90,300)
def draw():
    background(100)
    global w,s
    if keyPressed:
        if key == 'a' or key == 'A':
            w=w-2
        if key == 'd' or key == 'D':
            w=w+2
    ellipse(w,0,60,60)
