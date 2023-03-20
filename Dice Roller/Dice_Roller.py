
# Dice Rolling Program: Up to but not including task 4

import random # Imports the module for generating random numbers
# Class below not needed
# class diceRoller(object):
#   def __init__(self, iDiceResults, iDiceMin, iDiceMax, iDiceTotal):
#     self.iDiceResults = iDiceResults
#     self.iDiceMin = iDiceMin
#     self.iDiceMax = iDiceMax
#     self.iDiceTotal = iDiceTotal

def LineBreak():
  print("\n--------------------------\n")

LineBreak()

print("Welcome to my dice rolling program!\n")

bContinue = True

while bContinue: # While bContinue is true, loop the program

  print("1: Roll some dice")
  print("2: Exit the program")
  sUserInput = input("Please select an option: ") # Prints a user menu and asks the user tor an input

  if sUserInput == "1": # If the input is "1", do this

    LineBreak()

    sTypeOfDice = input("""Enter what type dice you would like to roll in the following format: 
d3, d4, d6, d8, d10, d12, d20, d100: """) # Asks the user what type of dice they want to roll
        
    sDiceToRoll = input("\nPlease enter the number of dice you would like to roll: ") # Asks the user for the number of dice they want to roll
  
    if sDiceToRoll.isdigit() == True: # If sDiceToRoll is a digit, do this
      
      iSideOfDice = int(sTypeOfDice.replace('d', '')) # removes the d from the string and converts it to an integer
      j = int(sDiceToRoll) # Assigns j to the integer value of sDiceToRoll
      i_DiceResults = [] # Creates an empty list
      
      for i in range(j): # For j number of times, loop
        iResult = random.randrange(1, (iSideOfDice + 1)) # Random number between 1 and 6
        i_DiceResults.append(iResult) # Add the result to the list

      print("The results are: ")
      print(*i_DiceResults, sep = ', ' ) # Unpack the list and print it with ',' between them

      LineBreak()
      
      sExtraInfo = input("Do you want to see the total, the number of 1s rolled and the number of times " + str(iSideOfDice) + " was rolled? y/n: ") # Asks the user if they want to see extra information

      if sExtraInfo == "y":
        print("\nThe total is: " + str(sum(i_DiceResults))) # Total the results
        print("The number of 1s rolled is: " + str(i_DiceResults.count(1))) # Prints the number of 1s rolled
        print("The number of times " + str(iSideOfDice) + " was rolled is: " + str(i_DiceResults.count(iSideOfDice)))
# Prints the number of times the maximum value was rolled
      elif sExtraInfo == "n":
        continue
      
      LineBreak()
        
    elif sDiceToRoll.isdigit() == False: # If sDiceToRoll isn't a digit, do this
      print("\nThe number of dice you entered is invald, please enter a whole number.")
      LineBreak()
      continue # Go back to beginning of loop

  elif sUserInput == "2": # If the input is "2", do this
    print("\nThank for using the program")
    bContinue = False # Set bContinue to False, exiting the program
