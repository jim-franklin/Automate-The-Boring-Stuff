def collatz(integer):
    # Check if even
    if integer % 2 == 0:
        return integer // 2
    # Check if odd
    elif integer % 2 == 1:
        return 3 * integer + 1


print('Enter number:')
try:
    user_number = input()    # ask user for input
    user_number = int(user_number)    # convert user input (sting value) to integer
    print(user_number)
    
    # the while loop breaks out when number = 1
    while number != 1:
        # the collatz function is called and its return value assigned to the variable, number
        number = collatz(number)    
        print(number) 
        
except ValueError:
    print('Error: You must Enter an integer.')
