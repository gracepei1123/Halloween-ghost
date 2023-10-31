import turtle as t

# Thiết lập màn hình
t.bgcolor("purple")
t.title("Con Ma Halloween")

# Vẽ bí ngô
t.penup()
t.goto(0, -100)
t.color("orange")
t.begin_fill()
t.circle(100)
t.end_fill()

# Vẽ mắt
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

draw_eye(-35, 20)
draw_eye(35, 20)

# Vẽ miệng
t.penup()
t.goto(0, -30)
t.pendown()
t.color("black")
t.width(5)
t.right(90)
t.circle(30, 180)
t.hideturtle()

# Đóng cửa sổ khi bạn nhấn chuột
t.exitonclick()
