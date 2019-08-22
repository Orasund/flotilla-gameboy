class Slider:
  position=0
class Matrix:
  def display_image(self,image):
    pass
     
class Touch:
  one=False
  two=False
  three=False
  four=False

def get_matrix(flotilla):
   return Matrix()
def get_slider(flotilla):
  return Slider()
def get_touch(flotilla):
  return Touch()

#-------------------------------------------

class Game:

  def __init__(self,flotilla):
    self.matrix=get_matrix(flotilla)
    self.slider=get_slider(flotilla)
    self.touch=get_touch(flotilla)
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
      self.matrix.display_image("tod")
      return
    self.hunger += 5
    if self.hunger > 100:
      self.hunger = 0
      self.life-=10
    if self.hunger %20 == 0:
      self.poop += 5
    if self.poop > 0:
      self.matrix.display_image("poop")
      if (self.slide and self.slider.position == 1) or (not self.slide and self.slider.position == 0):
        self.poop -= 5
        if self.poop < 0:
          self.poop = 0
        self.slide = not self.slide
    else:
      self.matrix.display_image("face(hunger,sick)")
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
  game.slider.position=not game.slider.position
  game.print()


game=Game("flotilla")
care(game)
game.touch.one = True
care(game)
care(game)
care(game)

    
