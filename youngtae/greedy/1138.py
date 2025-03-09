 # 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만 기억
# 키가 1인 사람부터 왼쪽에 자기보다 키 큰 사람이 몇명있는지 주어짐

import sys
input = sys.stdin.readline

N = int(input())
count_big_man = list(map(int, input().split())) 
answer = []
current = N                     # 현재 삽입하려는 사람의 키
for num in count_big_man[::-1]: # 키 큰 순부터 insert
    answer.insert(num, current) 
    current -= 1                # 다음 키 큰 사람

print(" ".join(map(str, answer)))
