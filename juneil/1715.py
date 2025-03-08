import sys
import heapq

input = sys.stdin.readline
N = int(input())
card_sets = []

# 최적인 경우는 가장 작은 두 card_Sets을 합치는 것을 card_sets이 한개 남을때까지 반복하는 것
for i in range(N):
    heapq.heappush(card_sets, int(input()))

ans = 0
while len(card_sets) > 1:
    new_sets = heapq.heappop(card_sets) + heapq.heappop(card_sets) # card_sets 2개 합치기
    ans += new_sets
    heapq.heappush(card_sets, new_sets) # 새로운 card_sets을 다시 고려 대상 card_sets에 넣는다
print(ans)