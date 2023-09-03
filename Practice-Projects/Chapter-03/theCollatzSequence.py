def collatz(integer):
    if integer % 2 == 0:
        return integer // 2
    # elif integer % 2 == 1:
    return 3 * integer + 1


print('Enter number:')
print('jim')
try:
    number = int(input())
    print('Collatz Sequence:')
    print(number)
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('Error: You must Enter an integer.')
