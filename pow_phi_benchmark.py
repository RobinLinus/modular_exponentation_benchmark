# Benchmark modular exponentiation base golden ratio 

# Calculate the golden ratio in the finite field F_p
def calculate_phi(p):
	# check if F_p is golden
    assert p % 5 == 1 or p % 5 == 4

    # check if we can easily compute square roots
    assert p % 4 == 3

    sqrt5 = pow(5, (p+1)/4, p)
    inv2 = (p-1)/2 + 1
    phi = (1+sqrt5) * inv2 % p 

    # check if phi is a generator 
    if pow(phi, (p-1)/2, p) == p-1:
        return phi 
    else:
    	# complement of phi must be the generator 
        phi2 = (1-phi) % p
        return phi2



# openssl dhparam 128 -text
# p = 0x00c67e1ca9b4705e6988674bab035c6d53

# openssl dhparam 512 -text
# p = 0x00cc49978de95bdd07cbedfe90e58d05ca4d3766728e3abe900a30dbf0830c7831328c6d67878dae07e211898dccba6b4274857a09b648e6361c4c4e8faddb698b

# openssl dhparam 1028 -text
p = 0x008e0df764fcff125f781ad372056e07e211bf411d9b8dec4ab4d49eb10a6fecfa37e142c16c1052be4e3d03062af969f073d45c687e855545ce1f62320adff9f00ca2359593ea1e36e3129445cf9243b2839386b9822a50835d05f700a1f4ace558dd9a3fa2bbc06ba91b01df3638aa9fb926a36dd62ace5cb07e82aa5c148733


phi = calculate_phi(p)



# benchmark pow base phi

import time

N = 3*1000000
n = 3000


print 
print('Calculating '+str(N)+' values of phi^n with addition')
start = time.time()

a1 = pow(phi,n,p)
a = a1 * phi % p
for i in range(N):
	a, a1 = (a+a1) % p, a

end = time.time()
print 'took '+str(end - start)+' seconds'


print 
print('Calculating '+str(N)+' values of phi^n with multiplication')
start = time.time()

a = pow(phi,n+1,p)
for i in range(N):
	a = (a*phi) % p

end = time.time()
print 'took '+str(end - start)+' seconds'
print
