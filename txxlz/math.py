#math.py
# TODO: Document code
from itertools import combinations
from functools import reduce


def find_factors(n, start=2):
	factors = []
	factor=start #use 1 just in case you need it

	while factor < n:
		res = n % factor
		if res > (n // 2): break
		if res == 0:
			factors.append(factor)
		factor +=1

	return factors

def fibon(n):
    
	a = b = 1

	for i in range(n):
		yield a
		a, b = b, a + b

def product_factors(n_com, product):

	valid_combinations = []
	list_of_factors = find_factors(product)
	#print(f"Found {list_of_factors}")
	comns = combinations(list_of_factors, n_com)

	try:
		while True: #to exhaust all options
			factors = list(next(comns))
			product_factors = reduce((lambda x, y : x*y), factors)
			#print(valid_combinations)
			if product_factors == product:
				#using yield can turn this into generator !!Experiment
				valid_combinations.append(factors)
	except StopIteration:
		#print("StopIteration")
		return valid_combinations
