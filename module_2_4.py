numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] #Primes: [2, 3, 5, 7, 11, 13]
not_primes = [] #Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        continue
    else:
        for a in range(2, n):
            if n % a == 0:
                is_prime = False
                break
        if not (is_prime):
            not_primes.append(n)
        else:
            primes.append(n)
print('Primes: ', primes)
print('Not primes: ', not_primes)



