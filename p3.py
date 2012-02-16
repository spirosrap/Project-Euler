def prime_factors(n):
    """ Return the prime factors of the given number. """
    factors = []
    lastresult = n
    
    # 1 is a special case
    if n == 1:
        return [1]
    
    while 1:
        if lastresult == 1:
            break
        
        c = 2
        
        while 1:
            if lastresult % c == 0:
                break
            
            c += 1
        
        factors.append(c)
        lastresult /= c
    
    return factors

print prime_factors(600851475143);