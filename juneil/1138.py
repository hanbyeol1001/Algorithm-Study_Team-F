N = int(input())
info = list(map(int, input().split()))
ans = [0 for i in range(N)]

for i in range(N):
    place = 0 # 배열의 시작위치부터 들어갈 후보위치 탐색
    
    zero_cnt = 0
    # 키가 작은 친구부터 들어갈 위치를 확인한다
    # 그렇기 때문에 현재 0으로 표시된 위치는 '반드시' 현재 자리를 결정하려는 사람보다 더 키가 큰 사람이 들어오게 된다
    # 즉, 0의 갯수를 세면 나보다 키가 큰 사람이 왼쪽에 몇명 있는지 확인할 수 있다.
    while zero_cnt != info[i]:
        if ans[place] == 0:
            zero_cnt += 1
        place += 1
    
    # 이렇게 들어갈 수 있는 최소 위치가 결정된 후에는 이미 자리를 잡은 사람을 피해서 자리를 배치시켜주면 된다.
    while ans[place] != 0:
        place += 1
    ans[place] = i+1
print(*ans)