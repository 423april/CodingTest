from collections import deque

def print_map(gamemap):
    print()
    for i in range(len(gamemap)):
        for j in range(len(gamemap[0])):
            print(gamemap[i][j], end=' ')
        print()

n, m = map(int, input().split(" "))
a, b, d = map(int, input().split(" "))
gamemap = [[0]*m for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split(" ")))
    for j in range(m):
        gamemap[i][j] = line[j]

directions = deque([0,1,2,3])
index = directions.index(d)
directions.rotate(-index)
move = [(-1,0), (0,-1), (1,0), (0,1)]
count = 0
while True:
    alldirs = True
    gamemap[a][b] = 1
    count += 1
    #print_map(gamemap)
    #print("count: {}".format(count))
    for dir in directions:
        #print(a+move[dir][0],b+move[dir][1] )
        if a+move[dir][0] <0 or a+move[dir][0] >= n or b+move[dir][1] < 0 or b+move[dir][1] >= m:
            continue
        if gamemap[a+move[dir][0]][b+move[dir][1]] == 0:
            directions.rotate(d-dir)
            d = dir
            # gamemap[a + move[dir][0]][b + move[dir][1]] = 1
            a = a + move[dir][0]
            b = b + move[dir][1]
            alldirs = False
            break
    if alldirs:
        if gamemap[a - move[dir][0]][b - move[dir][1]] == 1:
            break
        a = a - move[dir][0]
        b = b - move[dir][1]

print(count)

# 교재 코드는 어째...index out of bound 체크를 안해줘서 다음 칸으로 전진했을 때 지도 바깥에 있다면 그대로 오류가 나버린다.
# 그래서 정답 비교는 못했는데 내 코드 틀린거같진 않음
# deque 함수 새로 배움
