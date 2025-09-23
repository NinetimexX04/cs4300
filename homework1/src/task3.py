def classify_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def first_10_primes():
    primes = []
    num = 2
    while len(primes) < 10:
        if all(num % p != 0 for p in range(2, num)):
            primes.append(num)
        num += 1
    return primes

def sum_1_to_100():
    total = 0
    n = 1
    while n <= 100:
        total += n
        n += 1
    return total
