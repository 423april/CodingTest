import sys
n, m = map(int, input().split())
max_val = 0
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split(" ")))
    max_val = max(max_val, min(line)) # 굳이 리스트에 넣어서 max 연산할 필요 없이, 매번 max 비교 해주면 max_val 구할 수 있다
print(max_val)
