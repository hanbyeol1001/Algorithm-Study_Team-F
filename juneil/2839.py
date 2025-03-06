import sys

input = sys.stdin.readline
N = int(input())
MAX_CNT = 2000

ans = MAX_CNT

for i in range(N//5, -1, -1): # 5가 가장 많은 경우가 최적이므로 거꾸로 순회
    if (N-i*5)%3: # 만드는 것이 가능한 경우만 정답이 될 수 있음
        continue
    ans = min(ans, i + (N-i*5)//3)

if ans == MAX_CNT: # 가능한 경우가 없으면 -1출력
    print(-1)
else:
    print(ans)