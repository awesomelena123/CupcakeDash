# NOTE: Cupcake Dash was built for the trinket.io web based python environment,
# and will not run using the standard python interpreter.

# REFERENCE CODE (Galloping Unicorn Game): https://bit.ly/2JJtgpE

# TODO: Keep Score
# TODO: Print Score when gameOver

import time

import turtle
screen = turtle.Screen()
screen.setup(500, 500)
screen = turtle.Screen()
screen.bgpic("cupcakedashkitchen.png")

# enemy sprite ingredients

#Milk
screen.addshape("MILK.png")

#Butter
screen.addshape("BUTTER.png")

#Sugar
screen.addshape("SUGAR.png")

#Flour
screen.addshape("FLOUR.png")

#Vanilla
screen.addshape("VANILLA.png")

#Egg
screen.addshape("EGG.png")

#Salt
screen.addshape("SALT.png")

# create scoreboard
score = 0
# scoreboardpen = turtle.Turtle

# CURRENT TODO: Elena, make a dictionary, which contains the x-coordinate of each ingredient
thislist = ["obstaclex"]

class Cupcake:
    def __init__(self, x, y):
      self.cupcake = turtle.Turtle()
      self.cupcake.hideturtle()
      self.cupcake.shape("cupcake57x50.png")
      self.cupcake.penup()
      self.cupcake.speed(0)
      self.cupcake.left(90) # rotate cupcake to fix position
      self.cupcake.goto(x, y)
      self.cupcake.showturtle()
      self.jumpcount = 0
      self.isjumping = False

    # movement controls
    def jump(self):
      global score
      global gameOver
      global flour
      global sugar
      global butter
      global salt
      global vanilla
      global milk
      global egg
      pointScored = False
      if self.isjumping == False:
        self.isjumping = True
        x = self.cupcake.xcor()
        y = self.cupcake.ycor()
        # cupcake.setposition(x - )
        for i in range(50):
          if i == 0:
            # move up
            self.cupcake.setposition(x, y + 26)
            x = self.cupcake.xcor()
            y = self.cupcake.ycor()
          elif i == 1:
           #moveup
            self.cupcake.setposition(x, y + 26)
            x = self.cupcake.xcor()
            y = self.cupcake.ycor()
          elif i == 2:
            #moveup
            self.cupcake.setposition(x, y + 26)
            x = self.cupcake.xcor()
            y = self.cupcake.ycor()
          elif i == 3:
            self.cupcake.setposition(x, y)
            #pause, do nothing
            x = self.cupcake.xcor()
            y = self.cupcake.ycor()
          elif i >= 4 and i < 49:
            self.cupcake.setposition(x, y)
            #pause, do nothing
            x = self.cupcake.xcor()
            y = self.cupcake.ycor()
            # Detect Whether Cupcake is Above an Ingredient, if so, then add a point
            if flour.getx() > self.cupcake.xcor() - 25 and flour.getx() < self.cupcake.xcor() + 25:
              pointScored = True

            if sugar.getx() > self.cupcake.xcor() - 25 and sugar.getx() < self.cupcake.xcor() + 25:
              pointScored = True

            if butter.getx() > self.cupcake.xcor() - 25 and butter.getx() < self.cupcake.xcor() + 25:
              pointScored = True

            if salt.getx() > self.cupcake.xcor() - 25 and salt.getx() < self.cupcake.xcor() + 25:
              pointScored = True

            if vanilla.getx() > self.cupcake.xcor() - 25 and vanilla.getx() < self.cupcake.xcor() + 25:
              pointScored = True

            if milk.getx() > self.cupcake.xcor() - 25 and milk.getx() < self.cupcake.xcor() + 25:
              pointScored = True

            if egg.getx() > self.cupcake.xcor() - 25 and egg.getx() < self.cupcake.xcor() + 25:
              pointScored = True
          else:
            self.cupcake.setposition(x, y - 78)
            x = self.cupcake.xcor()
            y = self.cupcake.ycor()
            # DETECT COLLISION
            gameOver = flour.collision(cupcake) or gameOver
            gameOver = sugar.collision(cupcake) or gameOver
            gameOver = butter.collision(cupcake) or gameOver
            gameOver = egg.collision(cupcake) or gameOver
            gameOver =  salt.collision(cupcake) or gameOver
            gameOver =  milk.collision(cupcake) or gameOver
            gameOver = vanilla.collision(cupcake) or gameOver
            # increment score
            if gameOver == False and pointScored == True:
               score = score + 1
               print(score)
               pointScored = False # reset pointScored variable

          screen.update()
        self.isjumping = False

    def hidecupcake(self):
        self.cupcake.hideturtle()

    def showcupcake(self):
        self.cupcake.showturtle()

class Ingredient(turtle.Turtle):
  def __init__(self, image, x):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.shape(image)
    self.penup()
    self.speed(0)
    self.left(90) # rotate cupcake to fix position
    self.origin = x
    self.goto(x, -164)
    self.showturtle()

  def getx(self):
    return self.xcor()

  def collision (self, cupcake):
    obstaclex = self.xcor()
    obstacley = self.ycor()
    cupcakex = cupcake.cupcake.xcor()
    cupcakey = cupcake.cupcake.ycor()

    #if obstaclex > cupcakex - 20 and obstaclex < cupcakex + 20:
    if self.distance(cupcake.cupcake)<20:
      self.hideturtle()
      self.goto(self.xcor() + 220, self.ycor())
      endGame()
      return True
    else:
      return False

  def update(self):
    self.goto(self.xcor() - 2.2, self.ycor())
    if self.xcor()<self.origin-3538:
      self.setx(self.origin)

  def showIngredient(self):
    self.showturtle()

def playAgain():
  global screen
  global gameOver
  global flour
  global sugar
  global butter
  global egg
  global salt
  global milk
  global vanilla
  global cupcake
  global writer
  global playAgainPen
  # TODO: Replace Background Image
  # TODO: Unhide Turtles
  screen.bgpic("cupcakedashkitchen.png")
  flour.showIngredient()
  sugar.showIngredient()
  butter.showIngredient()
  egg.showIngredient()
  salt.showIngredient()
  milk.showIngredient()
  vanilla.showIngredient()
  cupcake.showcupcake()
  writer.clear()
  playAgainPen.clear()
  gameOver = False
  print("Play Again???")

def endGame():
  global gameOver
  global cupcake
  global screen
  global writer
  global playAgainPen
  global score
  writer.penup()
  writer.setposition(0, -25)
  writer.write("Game Over!", False, "center", ("Arial", 40, "bold"))
  playAgainPen.penup()
  playAgainPen.color("white")
  playAgainPen.setposition(-55, -50)
  playAgainPen.write("To play again, press enter.")
  cupcake.hidecupcake()
  screen.update()
  writer.setposition(-40, 27)
  writer.write("Score: " + str(score))
  # print("HIDE FLOUR!")
  screen.bgpic("toppings_rainbowsprinkles3.png")
  flour.hideturtle()
  sugar.hideturtle()
  butter.hideturtle()
  egg.hideturtle()
  salt.hideturtle()
  milk.hideturtle()
  vanilla.hideturtle()
  gameOver = False
  score = 0

flour = Ingredient("FLOUR.png", 225)
sugar = Ingredient("SUGAR.png", 776)
butter = Ingredient("BUTTER.png", 1428)
egg = Ingredient("EGG.png", 1680)
salt = Ingredient("SALT.png", 2032)
milk = Ingredient("MILK.png", 2484)
vanilla = Ingredient("VANILLA.png", 2836)




cupcake=Cupcake(-150, -160)
screen.addshape("cupcake57x50.png") #cupcake sprite

writer=turtle.Turtle()
writer.hideturtle()
writer.color('white')

playAgainPen=turtle.Turtle()
playAgainPen.hideturtle()

playerScore=turtle.Turtle()
playerScore.hideturtle()


screen.onkey(cupcake.jump,"space")
screen.onkey(playAgain, "enter")
screen.listen()
screen.tracer(0)
gameOver = False
while True:
  while not gameOver:
    # MOVE OBSTACLE (FLOUR)
    flour.update()
    sugar.update()
    butter.update()
    egg.update()
    salt.update()
    milk.update()
    vanilla.update()

    gameOver = flour.collision(cupcake) or gameOver
    gameOver = sugar.collision(cupcake) or gameOver
    gameOver = butter.collision(cupcake) or gameOver
    gameOver = egg.collision(cupcake) or gameOver
    gameOver =  salt.collision(cupcake) or gameOver
    gameOver =  milk.collision(cupcake) or gameOver
    gameOver = vanilla.collision(cupcake) or gameOver

    screen.update()

  '''
  writer.write("Game Over!", False, "center", ("Arial", 40, "bold"))
  playAgainPen.write("To play again, press enter.")
  cupcake.hidecupcake()
  screen.update()
  writer.write("Score:(print score")
  # print("HIDE FLOUR!")
  screen.bgpic("toppings_rainbowsprinkles3.png")
  '''
