import sys

input = sys.stdin.readline
N = int(input())

result = -1

for count in range(N//5, -1, -1): # 5키로를 최대한 많이 활용하는것부터 0개까지의 범위
    current = N - 5 * count
    if current % 3 == 0:
        result = count + current // 3
        break  # 무게맞춘 순간 break

print(result) # 무게 맞췄으면 개수가 출력되고 for문 다 돌아도 못찾은경우 -1 출력

