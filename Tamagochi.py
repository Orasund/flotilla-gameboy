import time

import flotilla_wrapper as flotilla
from flotilla_wrapper import get_matrix, get_slider


class Touch:
  one=False
  two=False
  three=False
  four=False


#-------------------------------------------
IMG_SMILEY = [ [0,1,1,0,0,1,1,0]
             , [0,1,1,0,0,1,1,0]
             , [0,1,1,0,0,1,1,0]
             , [0,0,0,0,0,0,0,0]
             , [1,1,1,1,1,1,1,1]
             , [1,0,0,0,0,0,0,1]
             , [0,1,0,0,0,0,1,0]
             , [0,0,1,1,1,1,0,0]
        ]

IMG_POOP = [ [0,0,0,1,1,0,0,0]
           , [0,0,1,0,1,1,0,0]
           , [0,0,1,1,1,1,0,0]
           , [0,0,0,1,1,0,0,0]
           , [0,0,0,1,1,0,0,0]
           , [0,0,0,1,1,0,0,0]
           , [0,0,1,1,1,1,0,0]
           , [0,1,1,1,1,1,1,0]
        ]

IMG_DEAD = [ [0,0,0,1,1,0,0,0]
        , [0,0,0,1,1,0,0,0]
        , [0,0,0,0,1,0,0,0]
        , [0,0,1,1,0,0,0,0]
        , [0,1,0,1,0,1,0,0]
        , [0,0,0,1,1,0,1,0]
        , [0,0,0,1,1,0,0,0]
        , [0,0,1,0,1,0,0,0]
    ]


class Game:

  def __init__(self, dock):
    self.matrix=get_matrix(dock)
    self.slider=get_slider(dock)
    self.touch=flotilla.get_touch(dock)
    self.life=100
    self.hunger=0
    self.poop=5
    self.slide=False
    
  def print(self):
    print("life: ",self.life)
    print("hunger: ",self.hunger)
    print("poop: ",self.poop)
    print("slide:",self.slide)
    print("-------------------")
    
  def tick(self):
    if self.life==0:
      self.matrix.display_image(IMG_DEAD)
      return
    self.hunger += 5
    if self.hunger > 100:
      self.hunger = 0
      self.life-=10
    if self.hunger %20 == 0:
      self.poop += 5
    if self.poop > 5:
      self.matrix.display_image(IMG_POOP)
      if (self.slide and self.slider.position == 1) or (not self.slide and self.slider.position == 0):
        self.poop -= 5
        if self.poop < 0:
          self.poop = 0
        self.slide = not self.slide
    else:
      self.matrix.display_image(IMG_SMILEY)
      if self.touch.one:
        self.life += 5
        self.hunger -= 20
        if self.hunger < 0:
          self.hunger = 0
        self.poop += 1
    if self.life > 100:
      self.life = 100
    if self.hunger < 0:
      self.hunger += 1

def care(game):
  game.tick()
##  game.slider.position=not game.slider.position
  game.print()



if __name__ == '__main__':
    flotilla_instance = flotilla.get_flotilla()
    game=Game(flotilla_instance)
    try:
        while True:
            care(game)
            print("slider:", game.slider.position)
            time.sleep(1)
    except KeyboardInterrupt:
        print('stopping flotilla...')
        flotilla_instance.stop()
        
##    game.touch.one = True
##    care(game)
##    care(game)
##    care(game)
