import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    print(f"{hat1.contents}")

# experiment()

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(f"{hat1.contents}")
