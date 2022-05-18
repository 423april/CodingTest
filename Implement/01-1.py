n = int(input())
dir = list(input().split())
data = dict()
data['L'] = [0,-1]
data['R'] = [0,1]
data['U'] = [-1,0]
data['D'] = [1,0]
cur = [1,1]

# 내 풀이
for i in range(len(dir)):
    cur = [cur[j]+data[dir[i]][j] for j in range(2)]
    #print(cur)
    if cur[0] <= 0 or cur[0] > n:
        cur = [cur[j]-data[dir[i]][j] for j in range(2)]
    elif cur[1] <= 0 or cur[1] > n:
        cur = [cur[j] - data[dir[i]][j] for j in range(2)]
    #print(cur)
print("{} {}".format(cur[0], cur[1]))

# 교재 풀이
x, y = 1,1
plans = dir
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']
st = time.time()
for plan in plans:
    for i in range(len(move_types)):
        nx, ny = 0, 0
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
# 답은 같게 나오고 N=100인 상황에선 둘 다 시간연산이 0.0으로 나올 정도로 빠르다
# N = 10000 정도로 높였더니 내 풀이가 미세하게 더 빠르다.
# 어느 쪽을 써도 크게 상관 없을듯
