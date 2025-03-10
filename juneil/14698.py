import sys
import heapq
input = sys.stdin.readline
MOD = 1000000007

T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    hq = []
    for num in lst:
        heapq.heappush(hq, num)

    ans = 1
    while len(hq) > 1:
        syn = heapq.heappop(hq) * heapq.heappop(hq) # 가장 작은 숫자 2개가 곱해지는 것이 최적
        ans = (ans * syn) % MOD
        heapq.heappush(hq, syn)
    
    print(ans % MOD)