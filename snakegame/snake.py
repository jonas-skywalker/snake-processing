import random


class Snake:
    def __init__(self, wwidth, wheight, foodsize_x, foodsize_y):
        self.x, self.y = random.randint(0, (wwidth/foodsize_x) - 1), random.randint(0, (wheight/foodsize_y) - 1)
        self.foodsize_x, self.foodsize_y = foodsize_x, foodsize_y
        self.body = [{"x": self.x, "y": self.y}, {"x": self.x - 1, "y": self.y}]
        self.x_vel = 1
        self.y_vel = 0
        self.wwidth, self.wheight = wwidth, wheight
        
    def show(self):
        push()
        for element in self.body:
            fill(255)
            rect(element["x"] * self.foodsize_x, element["y"] * self.foodsize_y, self.foodsize_x, self.foodsize_y)
        pop()
    
    def update(self):
        for i in range(1, len(self.body), 1):
            if (self.body[0]["x"] == self.body[i]["x"]) and (self.body[0]["y"] == self.body[i]["y"]) or (self.body[0]["x"] < 0) or (self.body[0]["x"] > ((self.wwidth/self.foodsize_x) - 1)) or (self.body[0]["y"] < 0) or (self.body[0]["y"] > ((self.wheight/self.foodsize_y) - 1)):
                # del(self.body[2:len(self.body)])
                x, y = random.randint(0, (self.wwidth/self.foodsize_x) - 1), random.randint(0, (self.wheight/self.foodsize_y) - 1)
                self.body = [{"x": x, "y": y}, {"x": x - 1, "y": y}]
                return
        
        update_x, update_y = self.body[0]["x"], self.body[0]["y"]
        self.body[0]["x"] += self.x_vel
        self.body[0]["y"] += self.y_vel

        for i in range(1, len(self.body), 1):
            update_x, self.body[i]["x"] = self.body[i]["x"], update_x
            update_y, self.body[i]["y"] = self.body[i]["y"], update_y
    
    def eat(self, food):
        if (self.body[0]["x"] == food.x) and (self.body[0]["y"] == food.y):
            self.body.append({"x": food.x - len(self.body) * self.x_vel, "y": food.y - len(self.body) * self.y_vel})
            return True
        return False
