import pyinputplus as pyip
'''     
Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.'''


cheeseType = ['cheddar', 'Swiss', 'mozzarella']
breadChoice = ['wheat', 'white', 'sourdough']
proteinChoice = ['chicken', 'turkey', 'ham', 'tofu']

print('Greetings, Welcome to Sandwich Maker!')

user_breadchoice = pyip.inputMenu(
    breadChoice, prompt="Which bread would you like? \n")
user_proteinChoice = pyip.inputMenu(
    proteinChoice, prompt=" What do you want as your protein? \n")

cheeseChoice = pyip.inputYesNo("Do you want cheese? \n")
if cheeseChoice == True:
    user_cheeseChoice = pyip.inputMenu(
        cheeseChoice, prompt=" Which cheese would you like? \n")

stuffing = ['mayo', 'mustard', 'lettuce', 'tomato']

for choice in stuffing:
    pyip.inputYesNo(f'Do you want {choice}? \n')

numbersOfSandwich = pyip.inputInt(
    'How many sandwich would you like? \n', min=1)

# TODO: make a price list
