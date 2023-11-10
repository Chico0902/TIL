n = int(input())

def hap(n):
    if n //10 == 0:
        return n

    return hap(n//10) + n % 10

result = hap(n)
print(result)