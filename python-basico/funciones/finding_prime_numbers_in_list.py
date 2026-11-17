
def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def find_primes(numbers):
    prime_numbers = []

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


my_list = [1, 4, 6, 7, 13, 9, 67]

print(find_primes(my_list))
