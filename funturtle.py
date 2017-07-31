UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGH_ARROW = "Right"
SPACEBAR = "space"
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = DOWN

def up():
    global direction
    direction = UP
    
def down():
    
    global direction
    direction = DOWN
    
def left():
    global direction
    direction = LEFT
    
def right():
    global direction 
    direction = RIGHT
