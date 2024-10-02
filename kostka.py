import random

def random_odd():
    odd_numbers = [i for i in range(1, 12) if i % 2 != 0]
    return random.choice(odd_numbers)

def random_even():
    even_numbers = [i for i in range(1, 12) if i % 2 == 0]
    return random.choice(even_numbers)

def random_power_of_two():
    powers_of_two = [2**i for i in range(1, 5) if 2**i <= 12]
    return random.choice(powers_of_two)

print(random_even())
print(random_power_of_two())