import random


class Food:
    def __init__(self, wwidth, wheight, foodsize_x, foodsize_y):
        self.x, self.y = random.randint(0, (wwidth/foodsize_x) - 1), random.randint(0, (wheight/foodsize_y) - 1)
        self.foodsize_x, self.foodsize_y = foodsize_x, foodsize_y
        self.wwidth, self.wheight = wwidth, wheight
    
    def show(self):
        push()
        stroke(255)
        fill(255, 0, 0)
        rect(self.x * self.foodsize_x, self.y * self.foodsize_y, self.foodsize_x, self.foodsize_y)
        pop()
    
    def new_pos(self):
        self.x, self.y = random.randint(0, (self.wwidth/self.foodsize_x) - 1), random.randint(0, (self.wheight/self.foodsize_y) - 1)
