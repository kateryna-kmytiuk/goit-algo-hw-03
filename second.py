import random


def get_numbers_ticket(min, max, quantity):
    if not 0 <= min <= max <= 1000 or (max-min) <= quantity or quantity <= 0:
        print('Некоректні вхідні данні')
        return []
    
    numbers = []
    while len(numbers) < quantity:
        num = random.randint(min, max)
        if num not in numbers:
            numbers.append(num)

    numbers.sort()

    return numbers


lottery_numbers = get_numbers_ticket(10, 20, 5)
print("Ваші лотерейні числа:", lottery_numbers)
