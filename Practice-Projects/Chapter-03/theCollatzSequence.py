def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


print('Enter number:')
try:
    number = int(input())
    print('Collatz Sequence:')
    print(number)
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('Error: You must Enter an integer.')
