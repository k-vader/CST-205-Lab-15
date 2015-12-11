# Ken Vader
# Chris Pina
# Ngoan Nguyen
# CST-205
# 12/11/2015
# Lab 15

import random
import datetime
import calendar

# Problem 1
# Craps Game

# Dice object		
class Dice(object):
  # Initialization requires sides and currentValue as integers
  def __init__(self, sides, currentValue):
    self.sides = sides
    self.currentValue = currentValue
  # For extensibility, we can set the number of sides on the dice	
  def setSides(self, num):
    self.sides = num
  # Method for simulating a dice roll	
  def doRoll(self):
    self.currentValue = random.randint(1, self.sides)

# Player object
class Player(object):
  # Give the player 2 dice objects to simulate rolling 2 dice
  die1 = Dice(6, 0)
  die2 = Dice(6, 0)
  # Initialization requires name as a string, money and wager as integers
  def __init__(self, name, money, wager):
    self.name = name
    self.money = money
    self.wager = wager
  # Method for getting the players name  
  def setName(self):
    self.name = requestString("Enter your name:")
    
    if len(self.name) == 0:
      return self.setName()
  # Check to see if the player can wager the amount they are attempting to wager
  # Returns true if they can wager, false otherwise		
  def canWager(self, amount):
    if self.money <= 0 or self.money < amount:
      return False
    else:
      return True
  # Method for placing a wager, has input validation to ensure an integer
  # is entered, the player can wager the amount, and also allows for entering
  # 0 to exit the game    
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
  # Displays players current amount of money	
  def displayBankroll(self):
    showInformation(self.name + " has $" + str(self.money) + " in the bank.")
  # Simulates rolling the 2 dice objects owned by the player 
  def throwDice(self):
    roll1 = self.die1.doRoll()
    roll2 = self.die2.doRoll()
    showInformation("You rolled a " + str(self.die1.currentValue) + " and a " + str(self.die2.currentValue) + ".\nThat totals to " + str(self.die1.currentValue + self.die2.currentValue))

# Main method of program, contains created player objects and game logic
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
        
  # Upon exit, show the player how they did by displaying how much money they had left     
  if bettor.money <= 0:
    showInformation("Tough luck! You went broke, better luck next time, " + bettor.name + ".")
  else:
    showInformation("You are quitting with $" + str(bettor.money) + " in the bank. Great job, " + bettor.name + ".")
      	
	
craps()


#Problem 2
#Print birthday calendar
def birthdayCalendar():
  year = int(requestString("Enter your birth year (as an integer):"))
  month = int(requestString("Enter your birth month (as an integer):"))
  
  print "Here is a calendar of the month you were born: \n"
  print calendar.month(year, month)

def daysUntilBirthday():
  #Set current date
  today = datetime.date.today()
  
  #Get birthday as integers
  month = int(requestString("Enter your birth month (as an integer from 1-12)"))
  day = int(requestString("Enter your birth day (as an integer):"))
  birthday = datetime.date(today.year, month, day)
  
  #Check if birthday is in the past, today or coming up this year
  if birthday == today:
    showInformation("Yay! Today is your birthday!")
  elif birthday < today:
    year = today.year + 1
    birthday = datetime.date(year, month, day)
    daysUntilBirthday = abs(birthday - today)
    showInformation("Your birthday already passed! There are %d days until your next birthday." % daysUntilBirthday.days)
  else:
    daysUntilBirthday = abs(birthday - today)
    showInformation("Your birthday is coming up. There are %d days until your next birthday." % daysUntilBirthday.days)

#Ask for the date the declaration of independence was signed and display the day of the week
def dayOfIndepedence():
  year = int(requestString("Enter the year the Declaration of Independence was ratified:"))
  month = int(requestString("Enter the month the Declaration of Independence was ratified:"))
  day = int(requestString("Enter the day the Declaration of Independence was ratified:"))
  declarationDate = datetime.date(year, month, day)
  
  showInformation("The declaration of independence was signed on a " + declarationDate.strftime("%A"))