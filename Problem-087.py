from Euler import prime_sieve
primes = prime_sieve(500)
print primes
def num(x,y,z):
    return x**2+y**3+z**4

print num(2,2,2)
print num(3,2,2)
print num(5,2,2)
print num(2,3,2)
print num(3,3,2)
print num(5,3,2)
print num(7,2,2)
print num(2,2,3)
print num(3,2,3)
print num(2,3,3)

sum=[]

for x in prime_sieve(7072):
    for y in prime_sieve(369):
        for z in prime_sieve(90):
            if(num(x,y,z)<50000001):
                sum.append(num(x,y,z))

sum.sort()
print len(sum)
print len(set(sum))