from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()

def foward():
    cursor.forward(10)
    
def backward():
    cursor.backward(10)
    
def left():
    cursor.left(10)
    
def right():
    cursor.right(10)
    
def Controller():
    screen.listen()
    screen.onkey(foward, "w")
    screen.onkey(backward, "s")
    screen.onkey(left, "a")
    screen.onkey(right, "d")
    
def main():
    Controller()
    screen.exitonclick()

if __name__ == "__main__":
    main()
