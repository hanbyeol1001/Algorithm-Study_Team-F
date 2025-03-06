N = int(input())
info = list(map(int, input().split()))
ans = [0 for i in range(N)]

for i in range(N):
    place = 0

    zero_cnt = 0
    while zero_cnt != info[i]:
        if ans[place] == 0:
            zero_cnt += 1
        place += 1
    
    while ans[place] != 0:
        place += 1
    ans[place] = i+1
print(*ans)