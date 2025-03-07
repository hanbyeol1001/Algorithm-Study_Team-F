import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 최적인 경우가 가장 작은 것 2개를 더해서 다시 push하는 경우임을 고려하여 priority queue 사용
hq = []
for num in cards:
    heapq.heappush(hq, num)

for i in range(m):
    # 가장 작은 수 2개를 뽑는 조작
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)

    # 뽑은 카드의 합을 다시 덮어쓰는 조작
    s = num1+num2
    heapq.heappush(hq, s)
    heapq.heappush(hq, s)

# 총 m번 조작 후 합을 출력
print(sum(hq))