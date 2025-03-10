import math
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# 가장 최적인 경우는 낮은 index부터 이전숫자보다 작은 값을 가지면 연산을 통해 크게 만들어 나가는 것이다.
# 그러나, 실제로 2배를 여러번 수행하는 경우 길이가 50000만 되도 최악의 경우 2^50000이라는 큰 숫자를 배열에 저장해야만 한다
# 이를 해결하기 위해 각 숫자에 2를 몇번 곱했는지 저장하는 배열을 선언한다
cnt = [0 for i in range(N)]

ans = 0
for i in range(1, N):
    # 몇번 곱했는지만 알면 로그의 성질을 활용하여 2를 곱해야하는 횟수를 나타낼 수 있다
    # 이전 숫자 = lst[i-1] * (2**cnt). 현재 숫자 = lst[i] -> 2를 곱해주어야 하는 횟수 = ceil(log2(lst[i-1] * 2**cnt / lst[i])) = ceil(log2(lst[i-1] / lst[i])) + cnt
    tmp = math.ceil(math.log2(lst[i-1] / lst[i])) + cnt[i - 1]
    tmp = max(tmp, 0)
    cnt[i] = tmp
    ans += tmp

print(ans)