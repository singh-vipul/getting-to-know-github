# Count total prime numbers in a given range
import primality_test


input_number = input('Enter a number: ')

if is_prime_number(input_number):
  print(str(input_number) + ' is a Prime Number')
else:
  print(str(input_number) + ' is a Composite Number')
