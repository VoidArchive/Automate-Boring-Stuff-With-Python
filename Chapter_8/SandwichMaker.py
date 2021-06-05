import pyinputplus as pyip
'''     
Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.'''


breadChoice = ['wheat', 'white', 'sourdough']
proteinChoice = ['chicken', 'turkey', 'ham', 'tofu']
cheeseChoice = ['cheddar', 'swiss', 'mozzarella']

print('Greetings, Welcome to Sandwich Maker!')

user_breadchoice = pyip.inputMenu(
    breadChoice, prompt="Which bread would you like? \n")
user_proteinChoice = pyip.inputMenu(
    proteinChoice, prompt="What do you want as your protein? \n")

cheeseYN = pyip.inputYesNo("Do you want cheese? \n")
if cheeseYN == 'yes':
    user_cheeseChoice = pyip.inputMenu(
        cheeseChoice, prompt=" Which cheese would you like? \n")
else:
    user_cheeseChoice = 0

stuffing = ['mayo', 'mustard', 'lettuce', 'tomato']

for choice in stuffing:
    pyip.inputYesNo(f'Do you want {choice}? \n')

numbersOfSandwich = pyip.inputInt(
    'How many sandwich would you like? \n', min=1)

'''bread 'wheat' : 3, 'white': 2, 'sourdough' : 1
protein 'chicken',:6  'turkey' : 5, 'ham' : 4, 'tofu' : 3
cheese 'cheddar' : 3, 'Swiss' : 2, 'mozzarella' : 1
Rest of the stuff are Free'''


def breadPrice(bread):
    return 3 if bread == 'wheat' else 2 if bread == 'white' else 1


def proteinPrice(protein):
    return 6 if protein == 'chicken' else 5 if protein == 'turkey' else 4 if protein == 'ham' else 3


def cheesePrice(cheese):
    return 3 if cheese == 'cheddar' else 2 if cheese == 'swiss' else 1 if cheese == 'mozzarella' else 0


totalPrice = numbersOfSandwich * (breadPrice(user_breadchoice) +
                                  proteinPrice(user_proteinChoice) + cheesePrice(user_cheeseChoice))

print(f"You total price is: {totalPrice} $")
