# 큰 수의 법칙
n, m, k = map(int, input().split(" "))
data = list(map(int, input().split(" ")))
data.sort(reverse=True)
answer = 0
# 풀이방법 1
# for 문을 이용한 방식은 M의 크기가 10억을 넘어가면 시간초과
for i in range(m):
    if i % (k+1) < k:
        answer += data[0]
    else:
        answer += data[1]
print(answer)

# 풀이방법 2
# 간단한 수식으로 M의 크기에 상관없이 빠른 시간 안에 답을 구할 수 있다
q = m // (k+1)
r = m % (k+1)
answer = q * (k * data[0] + data[1]) + r * data[0]
print(answer)
