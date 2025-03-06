import sys

input = sys.stdin.readline
N = int(input())
P_list = list(map(int, input().split()))
P_list.sort(reverse=True)

ans = 0
for i, p in enumerate(P_list):
    ans += (i+1) * p
print(ans)