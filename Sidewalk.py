def draw_square():
    for i in range(4):
        forward(50)
        left(90)
    
speed(50)    
penup()
setposition(-200,-200)
pendown()
for i in range(8):
   draw_square()
   forward(50)
   
for i in range(3):
    left(90)
    for i in range(8):
       draw_square()
       forward(50)
