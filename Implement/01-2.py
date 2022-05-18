n = int(input())

c1 = 0
c2 = 0
st = time.time()
# 내 풀이
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if h // 10 == 3 or h % 10 == 3 or m // 10 == 3 or m % 10 == 3 or s // 10 == 3 or s % 10 == 3:
                c1 += 1
en = time.time()
print(c1)
print(en-st)

st = time.time()
# 교재 풀이
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                c2 += 1
en = time.time()
print(c2)
print(en-st)

# 시간은 내 풀이가 더 빠름
# 하지만 이후에 비슷한 문제 풀 때 자릿수가 너무 많거나 문제 조건이 복잡하거나 하면 문자열에 존재하는지 in 을 써서 확인하는게 더 좋을 것 같기도. 기억해두기!
