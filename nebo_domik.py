import turtle as t
import random as r

#НЕБО

t.speed(150)# скорость
t.goto(-340,280)# идем в верхний левый угол
t.begin_fill()# заливка начало
t.color("","#003366")# цвет темный синий
# рисуем квадрат
t.goto(340,280)
t.goto(340,-280)
t.goto(-340,-280)
t.goto(-340,280) 
t.end_fill()# заливка конец

# ЗВЕЗДЫ 1

t.color("gold","gold")# объявляем цвет звезд
for j in range(7):
    t.up()#поднимаем кисть
    x=r.randint(-320,320) # выбираем область для случайных точек
    y=r.randint(-260,260)
    t.goto(x,y)# идем к ним
    t.down()#опускаем кисть
    t.begin_fill()# заливка начало
    for i in range(5):# цикл от 0 до 4
        t.forward(20)# линия 20
        t.right(144)# поворот на 144 град
    t.end_fill()#заливка конец
t.up()#поднимаем кисть

# ЗВЕЗДЫ 2

t.color("gold","gold")# объявляем цвет звезд
for j in range(10):
    t.up()#поднимаем кисть
    x=r.randint(-320,320) # выбираем область для случайных точек
    y=r.randint(-260,260)
    t.goto(x,y)# идем к ним
    t.down()#опускаем кисть
    t.begin_fill()# заливка начало
    for i in range(5):# цикл от 0 до 4
        t.forward(10)# линия 20
        t.right(144)# поворот на 144 град
    t.end_fill()#заливка конец
t.up()#поднимаем кисть


# ЛУНА (два круга желтый и синий)

t.goto(200,140)# идем в правый верхний угол
t.down()#опускаем кисть
t.begin_fill()# заливка начало
t.circle(60)# рисуем круг
t.end_fill()#заливка конец
t.color("","#003366")
t.up()
t.goto(180,170)
t.down()
t.begin_fill()# заливка начало
t.circle(45)# рисуем круг
t.end_fill()#заливка конец
t.up()

# ТРАВА

t.goto(-340,-240)# в нижний левый угол
t.down()
t.begin_fill()# начать заливку
t.color("green","green") # зелёный
# прямоугольник
t.goto(340,-240)
t.goto(340,-280)
t.goto(-340,-280)
t.goto(-340,-240)
t.end_fill()# конец залики
t.up()

# ДОМ

# идем в правый нижний угол но не до конца
t.goto(150,-140)
t.down()
t.begin_fill()# начать заливку
t.color("#454545","#9f9f9f") # зелёный
# квадрат
t.goto(150,-240)
t.goto(250,-240)
t.goto(250,-140)
t.goto(150,-140)
t.end_fill()# конец залики

# крИша
t.begin_fill()
t.color("black","#8B0000")
t.goto(200,-90) # крИша по диагонали вверх
t.goto(250,-140) # крИша по диагонали вниз
t.end_fill()
# подняли кЫсть
t.up()
t.goto(175,-165)
t.down()
# окно
t.begin_fill()
t.color("steel blue","#87CEFA")
t.goto(225,-165)
t.goto(225,-215)
t.goto(175,-215)
t.goto(175,-165)
t.end_fill()
# подняли кЫсть
t.up()
t.goto(200,-165)
t.down()
# рама
t.goto(200,-215)
t.goto(200,-190)
t.goto(175,-190)
# подняли кЫсть
t.up()
t.goto(217,-107) # к тРуБе линия вверх
t.down()
# труба
t.begin_fill()
t.color("saddle brown","#A0522D")
t.goto(217,-80)
t.goto(214,-80)
t.goto(214,-75)
t.goto(240,-75)
t.goto(240,-80)
t.goto(237,-80)
t.goto(237,-127)
t.end_fill()
# подняли кЫсть
t.up()
t.goto(150,-215)
t.down()
t.begin_fill()
t.color("saddle brown","#A0522D")
t.goto(130,-215)
t.goto(130,-223)
t.goto(110,-223)
t.goto(110,-231)
t.goto(90,-231)
t.goto(90,-239)
t.end_fill()
t.mainloop()

