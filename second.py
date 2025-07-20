import random


def get_numbers_ticket(min, max, quantity):
    if min < 0 or max > 1000 or quantity < min or quantity > max or min > max:
        print('Некоректні вхідні данні')
        return
    
    numbers = []
    while len(numbers) < quantity:
        num = random.randint(min, max)
        if num not in numbers:
            numbers.append(num)

    numbers.sort()

    return numbers


lottery_numbers = get_numbers_ticket(100, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
