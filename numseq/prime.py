def primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

    
def is_prime(a):
    x = True 
    for i in range(2, a):
       if a%i == 0:
           x = False
           break
    return x