# import colorgram
import turtle as turtle_module
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

turtle_module.colormode(255)
Timmy = turtle_module.Turtle()
Timmy.speed("fastest")
Timmy.penup()
Timmy.hideturtle()
color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44),
              (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32),
              (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176),
              (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

Timmy.setheading(225)
Timmy.forward(300)
Timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    Timmy.dot(20, random.choice(color_list))
    Timmy.forward(50)

    if dot_count % 10 == 0:
        Timmy.setheading(90)
        Timmy.forward(50)
        Timmy.setheading(180)
        Timmy.forward(500)
        Timmy.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
