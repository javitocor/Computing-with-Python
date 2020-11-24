from copy import deepcopy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.contents = list()
        for key, value in kwargs.items():
            for x in range(value):
                self.contents.append(key)
  def draw(self, numberOfBalls):
    draw = list()
    if numberOfBalls >= len(self.contents):
      draw = self.contents
      return draw
    draw = random.sample(self.contents, numberOfBalls)
    for item in draw:
      self.contents.remove(item)
    return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  index = 0
  success = list()
  while index < num_experiments :
    new_hat = deepcopy(hat)
    draw = new_hat.draw(num_balls_drawn)
    expected = list()
    for k,v in expected_balls.items() :
      for x in range(v):
        expected.append(k)
    
    if set(draw) == set(expected) :
      success.append(1)
    else :
      success.append(0)
    index += 1
  m = float(success.count(1))
  n = float(len(success))
  return m/n