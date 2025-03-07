import sys
import heapq
input = sys.stdin.readline

N = int(input())
deadlines = []
candidates = []


# 핵심 아이디어 : 이득이 큰 일을 데드라인 맞춰서 처리할수록 이득 -> N일차에 deadline이 N일차랑 같거나 큰 애들 중에서 profit이 가장 큰 것을 선택하도록 코드를 구성
for i in range(N):
    deadline, profit = map(int, input().split())
    heapq.heappush(deadlines, (-deadline, profit)) # 모든 일을 deadline기준 내림차순으로 정렬하여 담은 heapq 생성

ans = 0
while N: # 날짜를 역순으로 처리하는 이유는 N일차에 처리할 수 있는 일이 deadline이 N이상인 일들이기 때문이다
    while deadlines: # deadline이 N일차인 애들을 candidates heapq로 넣고, profit에 대해 내림차순 정렬
        d, p = heapq.heappop(deadlines) 
        d = -d

        if d == N:
            heapq.heappush(candidates, -p)
        else:
            heapq.heappush(deadlines, (-d, p))
            break
    
    if candidates: # N일차에 대해서 deadline이 N이랑 같거나 큰 애들만 candidates에 담겨있으므로 단순히 이익이 가장 큰 숙제를 선택하기만하면 된다
        ans += -heapq.heappop(candidates)
    N -= 1

print(ans)