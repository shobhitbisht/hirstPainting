import turtle as turtle_module
import random

pika = turtle_module.Turtle()
pika.shape("turtle")
screen = turtle_module.Screen()
screen.colormode(255)
color_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93),
              (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195),
              (126, 193, 74), (85, 28, 93), (173, 36, 97), (246, 219, 44),
              (44, 172, 112), (215, 130, 165), (215, 56, 27)]

pika.hideturtle()
pika.setheading(225)
pika.penup()
pika.forward(200)
pika.setheading(0)

for i in range(10):
  
  for i in range(10):
    random_color = random.choice(color_list)
    pika.dot(15, random_color)
    pika.penup()
    pika.forward(30)
  
  for i in range(10):
    pika.backward(30)
  pika.left(90)
  pika.forward(30)
  pika.right(90)