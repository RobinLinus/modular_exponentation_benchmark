# -*- coding: utf-8 -*-


def phi_p(p):
	# Compute the square root of 5 mod p
	sqrt5 = pow(5, (p+1)/4, p)

	# Compute the inverse of 2 mod p
	inv2 = (p-1)/2+1

	# Compute the golden ratio mod p
	phi = (1+sqrt5) * inv2 % p

	return phi

def phi_inv_p(p):
	return ( 1 - phi_p(p) ) % p

#
# Checks if the golden ratio exists in the field F_p
#
def is_golden_prime(p, print_error = False):
	# Assert p mod 5 ≡ ±1 
	if not (p % 5 == 1 or p % 5 == 4):
		if print_error:
			print Exception("sqrt(5) doesn't exist mod "+str(p))
		return False

	# Assert p mod 4 ≡ 3
	if not p % 4 == 3:
		if print_error:
			print Exception("Use a different square root algorithm")
		return False

	# Compute sqrt(5) mod p
	sqrt5 = pow(5, (p+1)/4, p)

	# Compute 1/2 mod p
	inv2 = (p-1)/2+1

	# Compute golden ratio mod p
	phi = (1+sqrt5) * inv2 % p

	# Check the characteristic equation of the golden ratio
	# 𝜑² ≡ 𝜑 + 1
	return ( phi * phi ) % p == ( phi + 1 ) % p

#
# Computes the n-th Fibonacci number mod p, 
# using Binet's formula (https://en.wikipedia.org/wiki/Fibonacci_number#Binet's_formula)
#
from basics import modinv
def mod_fib(n, p):
	# Check if p is a golden prime 
	if not is_golden_prime(p):
		raise Exception("p="+str(p)+" is not a golden prime number")

	# Compute the square root of 5 mod p
	sqrt5 = pow(5, (p+1)/4, p)

	# Compute the inverse of 2 mod p
	inv2 = (p-1)/2+1

	# Compute the golden ratio mod p
	phi = (1+sqrt5) * inv2 % p

	# Compute the inverse golden ratio mod p
	phi_inv = (1-phi) % p

	# Compute the inverse of sqrt(5) mod p
	inv_sqrt5 = modinv(sqrt5, p)

	# Compute n-th Fibonacci number using Binet's formula
	fib_n = ( pow(phi, n, p) - pow(phi_inv, n, p) ) * inv_sqrt5 % p

	return fib_n


def mod_luc(n, p):
	# Check if p is a golden prime 
	if not is_golden_prime(p):
		raise Exception("p="+str(p)+" is not a golden prime number")

	# Compute the square root of 5 mod p
	sqrt5 = pow(5, (p+1)/4, p)

	# Compute the inverse of 2 mod p
	inv2 = (p-1)/2+1

	# Compute the golden ratio mod p
	phi = (1+sqrt5) * inv2 % p

	# Compute n-th Fibonacci number using Binet's formula
	luc_n = ( pow(phi, n, p) + pow(1-phi, n, p) ) % p

	return luc_n

def is_lucas_probable_prime(p):
	# https://en.wikipedia.org/wiki/Lucas_number#Congruence_relations
	return mod_luc(p,p) == 1

def is_square(x, p):
	return pow(x,(p-1)/2,p) == 1

def is_fib(x,p):
	return is_square(5 * x * x + 4,p) or is_square(5 * x * x - 4,p) 



#
# Golden Prime Tests 
#
p = 599
phi = 25
N = 1000
# 𝜑^(n+2) ≡ 𝜑^(n+1) + 𝜑^n
assert ( pow(phi, N, p) + pow(phi, N+1, p) ) % p == pow(phi, N+2, p)

from is_prime import is_prime

print 
print "The 'Golden Primes' up to N=1000"
print "N","phi"
for N in range(1000):
	if is_golden_prime(N) and is_prime(N):
		print N, phi_p(N)

print
print
print


print "The 'Pseudo Golden Primes': List of false positives up to 2'000'000"
print "N","phi", "is_Lucas_Prime"
for N in range(2000000):
	if is_golden_prime(N) and not is_prime(N):
		print N, phi_p(N), is_lucas_probable_prime(N)


print
print
print "List of 'Safe Golden Primes' up to 2903"
print "# ","N","phi"
safe_primes = [5,7,11,23,47,59,83,107,167,179,227,263,347,359,383,467,479,503,563,587,719,839,863,887,983,1019,1187,1283,1307,1319,1367,1439,1487,1523,1619,1823,1907,2027,2039,2063,2099,2207,2447,2459,2579,2819,2879,2903]

i = 0
for p in safe_primes:
	if(is_golden_prime(p)):
		print i,p,phi_p(p)
	i+=1



"""
	Side Notes: "About the golden primes"
		Conjecture 1: The last decimal digit of golden primes is "1" or "9" 
			True because p mod 5 ≡ ±1 <=> p mod 10 ≡ ±1 ( or p mod 10 ≡ 5 ±1 => not prime ) 
		Conjecture 2: The last 2 digits of golden primes are often a prime number
			True because numbers ending with 1 or 9 are more likely to be prime than random numbers 
			because ( prime mod 10 ≡ {1,3,7,9} )

	Side Notes: "About the pseudo golden primes"
		Conjecture 1: If p is a pseudo golden prime, then p-1 consists of only small prime factors. ( p-1 is smooth )
		Conjecture 2: Pseudo golden primes' last digit is disproportionately often "1"

"""



#
# Fibonacci Tests 
#
print
print
print
print
print
print "Fibonacci Numbers mod p"
print
print

# p = 59
p = 31
print "Fibonacci Numbers mod " + str(p)
for n in range(2*p):
	print n, mod_fib(n,p)

p = 599
N = 1000
assert ( mod_fib(N, p) + mod_fib(N+1, p) ) % p == mod_fib(N+2,p)



#
# Lucas Numbers Tests 
#
print
print
print
print
print
print "Lucas Numbers mod p"
print
print

# p = 59
p = 31
print "Lucas Numbers mod " + str(p)
for n in range(2*p):
	print n, mod_luc(n,p)

p = 599
N = 100
assert ( mod_luc(N, p) + mod_luc(N+1, p) ) % p == mod_luc(N+2,p)

assert is_lucas_probable_prime(p)

print ( mod_luc(N, p) - mod_luc(N-4, p) ) % p % 5


