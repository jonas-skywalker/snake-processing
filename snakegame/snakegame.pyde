from food import Food
from snake import Snake


size_x = 0
size_y = 0
food = None
snake = None

def setup():
    #fullScreen()
    size(700, 700)
    global size_x
    size_x = width/20.0
    global size_y
    size_y = height/20.0
    
    global food
    food = Food(width, height, size_x, size_y)
    global snake
    snake = Snake(width, height, size_x, size_y)


def draw():
    frameRate(8)
    background(51)
    draw_grid()
    food.show()
    snake.update()
    snake.show()
    if snake.eat(food):
        # print("NOM")
        food.new_pos()
    
    
def draw_grid():
    push()
    stroke(255)
    for i in range(20):
        line(size_x * i, 0, size_x * i, height)
    for i in range(20):
        line(0, size_y * i, width, size_y * i)
    pop()
    
    
def keyPressed():
    if keyCode == UP:
        snake.y_vel = -1
        snake.x_vel = 0
    elif keyCode == DOWN:
        snake.y_vel = 1
        snake.x_vel = 0
    elif keyCode == LEFT:
        snake.y_vel = 0
        snake.x_vel = -1
    elif keyCode == RIGHT:
        snake.y_vel = 0
        snake.x_vel = 1
