n = int(input())
dir = list(input().split())
data = dict()
data['L'] = [0,-1]
data['R'] = [0,1]
data['U'] = [-1,0]
data['D'] = [1,0]
cur = [1,1]

for i in range(len(dir)):
    cur = [cur[j]+data[dir[i]][j] for j in range(2)]
    #print(cur)
    if cur[0] <= 0 or cur[0] > n:
        cur = [cur[j]-data[dir[i]][j] for j in range(2)]
    elif cur[1] <= 0 or cur[1] > n:
        cur = [cur[j] - data[dir[i]][j] for j in range(2)]
    #print(cur)
print("{} {}".format(cur[0], cur[1]))
