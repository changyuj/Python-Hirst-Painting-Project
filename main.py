###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import os
import turtle as t
import random as rand

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "image.jpg")

rgb_colors = []
colors = colorgram.extract(image_path, 30)
for color in colors:
    rgb_colors.append(color.rgb)
    
print(rgb_colors)

my_turtle = t.Turtle()
my_turtle.shape("turtle")

my_turtle.up()
my_turtle.hideturtle()

t.colormode(255)

my_turtle.speed("fastest")

def place_dot(gap_size):
    for _ in range(10):
        my_turtle.dot(20, rand.choice(rgb_colors) )
        my_turtle.forward(gap_size)
        

for i in range(10):
    my_turtle.teleport(-300, (i * 50)-300)
    place_dot(50)
    


screen = t.Screen()
screen.exitonclick()