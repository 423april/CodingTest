import sys
n, m = map(int, input().split())
lines = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split(" ")))
    lines.append(min(line))
print(max(lines))
