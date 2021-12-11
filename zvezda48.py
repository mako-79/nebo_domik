import turtle as t
t.speed(40)
t.up()
t.goto(0,250)
t.down()
t.begin_fill()# заливка начало
t.color("#aaaa00","yellow")# объявляем цвет звезд
for i in range(48):# цикл от 0 до 4
    t.right(60)    
    t.forward(10)
    t.left(60)    
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.left(60)
    t.forward(10)
    if i%2==0 or i==3 or i==11 or i==19 or i==27 or i==35 or i==43:
        t.left(120)
    else:
       t.right(60)
    t.down()
t.end_fill()#заливка конец
