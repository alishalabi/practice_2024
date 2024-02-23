"""
Create an alogithm to determine all prime numbers up to a certain value.
"""

def prime_numbers(target):
    if target < 1:
        return "Error - target must be a positive whole"
    if target % 1 != 0:
        return "Error - target not a whole number"

    primes = []

    for number in range(2, target + 1):
        is_prime = True
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes

print(prime_numbers(10101))
