n, k = map(int, input().split(" "))
n1, k1 = n, k
count = 0

# 내 풀이
while n > 1:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n = n - 1
        count += 1
print(count)

# 교재 풀이
result = 0
while True:
    target = (n1//k1) * k1
    result += n1 - target
    n1 = target
    if n1 < k1:
        break
    result += 1
    n1 //= k1
result += n1-1
print(result)
