# Lab 15

import random

# Problem 1
class Player(object):
  
  die1 = Dice(6, 0)
  die2 = Dice(6, 0)
  
  def __init__(self, name, money, wager):
    self.name = name
    self.money = money
    self.wager = wager
    
  def setName(self):
    self.name = requestString("Enter your name:")
    
    if len(self.name) == 0:
      return self.setName()
		
  def canWager(self, amount):
    if self.money <= 0 or self.money < amount:
      return False
    else:
      return True
      
  def doWager(self):
    self.wager = requestString("Enter an amount to bet:")
    if len(self.wager) == 0:
      return self.doWager()
    
    if not self.wager.isnumeric():
      showInformation("Please enter your wager as an integer.")
      return self.doWager()
    elif not self.canWager(int(self.wager)):
      showInformation("You do not have enough money to place that bet.")
      return self.doWager()
    elif int(self.wager) == 0:
      self.wager = int(self.wager)
    elif int(self.wager) < 0:
      showInformation("You cannot wager negative values.")
      return self.doWager()
    else:
      self.wager = int(self.wager)
      showInformation("You are betting $" + str(self.wager) + ". Ready to roll?")               
		
  def displayBankroll(self):
    showInformation(self.name + " has $" + str(self.money) + " in the bank.")
    
  def throwDice(self):
    roll1 = self.die1.doRoll()
    roll2 = self.die2.doRoll()
    showInformation("You rolled a " + str(self.die1.currentValue) + " and a " + str(self.die2.currentValue) + ".\nThat totals to " + str(self.die1.currentValue + self.die2.currentValue))
		
class Dice(object):
  def __init__(self, sides, currentValue):
    self.sides = sides
    self.currentValue = currentValue
		
  def setSides(self, num):
    self.sides = num
		
  def doRoll(self):
    self.currentValue = random.randint(1, self.sides)

def craps():
  # Welcome message
  showInformation("Welcome to Craps-tron 5000\nStart by entering your name. Place bets by typing in a number. The game ends when you run out of money or you place a bet for 0 dollars.")
  
  # Create a player, get their name, and show them how much money they have
  bettor = Player("", 500, 0)
  bettor.setName()
  bettor.displayBankroll()
  
  point = 0
  initialRoll = True
  
  # Prompt for initial wager and enter game loop
  bettor.doWager()
  while bettor.money > 0 and bettor.wager != 0:
    # Throw dice and put result into point
    bettor.throwDice()
    currentThrow = bettor.die1.currentValue + bettor.die2.currentValue
    
    # Game logic
    if (currentThrow == 7 or currentThrow == 11) and initialRoll:
      showInformation("You rolled " + str(currentThrow) + " on the come out roll. You win!")
      bettor.money += bettor.wager
      bettor.displayBankroll()
      bettor.doWager()
      continue
    elif (currentThrow == 2 or currentThrow == 3 or currentThrow == 12) and initialRoll:
      showInformation("You rolled " + str(currentThrow) + " on the come out roll. Sorry, you lose.")
      bettor.money -= bettor.wager
      bettor.displayBankroll()
      bettor.doWager()
      continue
    elif initialRoll:
      showInformation("You rolled " + str(currentThrow) + " on the come out roll. " + str(currentThrow) + " is now the point.")
      point = currentThrow
      initialRoll = False
      continue
    elif currentThrow == 7 and not initialRoll:
      showInformation("Oh, so sad. You crapped out by rolling a 7. You lose.")
      bettor.money -= bettor.wager
      bettor.displayBankroll()
      bettor.doWager()
      initialRoll = True
      continue
    elif currentThrow == point and not initialRoll:
      showInformation("You hit the point! You rolled a " + str(point) + "! Winner, winner, chicken dinner!")
      bettor.money += bettor.wager
      bettor.displayBankroll()
      bettor.doWager()
      initialRoll = True
      continue
    else:
        showInformation("You rolled a " + str(currentThrow) + ". Roll again.")
        continue
        
        
  if bettor.money <= 0:
    showInformation("Tough luck! You went broke, better luck next time, " + bettor.name + ".")
  else:
    showInformation("You are quitting with $" + str(bettor.money) + " in the bank. Great job, " + bettor.name + ".")
      	
	
	
	
	
craps()
