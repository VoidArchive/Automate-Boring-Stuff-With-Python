
def collatz(number):
    # Even number
    if (number % 2) == 0:
        result = number // 2
        print(result)
        return result
    # Odd number
    else:
        result = 3 * number + 1
        print(result)
        return result

    # return result


try:
    user_input = int(input("Write a integer: "))
except ValueError:
    print("Type an integer")

# Loop until input is 1
while user_input != 1:
    user_input = collatz(user_input)
