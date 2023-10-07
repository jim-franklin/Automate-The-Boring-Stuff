def collatz(integer):
    # Check if even
    if integer % 2 == 0:
        return integer // 2
    # Check if odd
    elif integer % 2 == 1:
        return 3 * integer + 1


print('Enter number:')
number = input()    # ask user for input
number = int(number)    # convert user input (sting value) to integer

# the while loop breaks out when number = 1
while number > 1:
    # the collatz function is called and its return value assigned to the variable, number
    number = collatz(number)    
    print(number)
    