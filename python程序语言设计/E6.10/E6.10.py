def isprime(num):
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

count = 0

for i in range(1,10001):
    if isprime(i):
        count += 1

print(count)