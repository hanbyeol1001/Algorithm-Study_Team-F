# N의 분해합은 N과 N을 이루는 각 자리수의 합
# 이때 M의 분해합이 N의 경우 M을 N의 생성자라고 함
# 245 => 245 + 2 + 4 + 5 = 256 따라서 245는 256의 생성자
# N이 주어졌을 때, N의 가장 작은 생성자 구해내기
# 최대자리수가 9이므로 입력 N의 최고자리수 - 1 + 9 * 나머지 자리수 부터 성립하는지 확인하면 됨

import sys
input = sys.stdin.readline

N_list = list(map(int, input().strip())) # N의 각자리수 list로 저장
N = int(''.join(map(str, N_list))) # 다시 원래대로 정수형태로 N에 저장
max_sum = N_list[0] - 1 + (len(N_list)-1) * 9 # N보다 작은 각자리수 최대합을 구함
answer = 0

for sang in range(N-max_sum, N + 1): # for문 돌면서 만족하는거 발견하면 바로 stop
    if sang + sum(list(map(int, str(sang)))) == N:
        answer = sang
        break

print(answer)