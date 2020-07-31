# Checks if a number is prime

def is_prime_number(number):
  i = 2
  while i * i <= number:
    if number % i == 0:
      return False
    i += 1
  return number >= 2
