import turtle as t
t.speed(40)
t.up()
t.goto(0,250)
t.down()
for i in range(100):# цикл от 0 до 4
    if i%2!=0:
        t.right(60)    
        t.forward(20)
        t.left(60)    
        t.forward(20)
        t.right(60)
    else:
        t.left(10)
        t.forward(20)
        t.left(60)    
        t.forward(20)
        t.right(60)
    t.down()
