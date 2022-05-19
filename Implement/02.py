locstr = input()
cols = dict()

# my solution
for i in range(8):
    ch = ord('a') + i
    cols[chr(ch)] = i

loc = [int(locstr[1])-1, cols[locstr[0]]]
result1 = 0

for i in [2, -2]:
    for j in [1,-1]:
        #print(loc[0]+i, loc[0]+j)
        if 0 <= loc[0]+i < 8 and 0 <= loc[1] + j < 8:
            #print("yes")
            result1 += 1
        #print(loc[0] + j, loc[0] + i)
        if 0 <= loc[0]+j < 8 and 0 <= loc[1] + i < 8:
            #print("yes")
            result1 += 1
print("my solution: {}".format(result1))



# book solution
input_data = locstr
row = int(input_data[1])
column = int(ord(input_data[0]) - ord('a')) + 1

steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)]

result2 = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result2 += 1
print("book solution: {}".format(result2))


# 책 풀이도 좋긴한데 steps 다 쓰는게 귀찮다. 내 풀이가 나은듯
# 딱히 시간 차이도 많이 안 날 것 같음
