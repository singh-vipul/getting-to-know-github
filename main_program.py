# Count total prime numbers in a given range
from primality_test import is_prime_number
import pickle


def load_primes_from_cache():
	prime_numbers = set()
	try:
		with open('cached.pickle', 'rb') as fp:
			prime_numbers = pickle.load(fp)
	except:
		pass
	return prime_numbers


prime_numbers = load_primes_from_cache()

input_number = int(input('Enter a number: '))

if input_number in prime_numbers:
  print(str(input_number) + ' is a Prime Number')
elif is_prime_number(input_number):
  print(str(input_number) + ' is a Prime Number')
  prime_numbers.add(input_number)
  with open('cached.pickle', 'wb') as fp:
    pickle.dump(prime_numbers, fp)
else:
  print(str(input_number) + ' is a Composite Number')
