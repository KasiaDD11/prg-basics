

def f(n):
    prime=[2]
    i=3
    while len(prime) < n:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(i)

        i += 1
    return prime

print(f(5))
        
        