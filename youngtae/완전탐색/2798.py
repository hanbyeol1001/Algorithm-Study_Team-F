# N, M 이 주어짐
# M과 가장 가까운 카드 3장의 합 출력

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_num = 0
for card in combinations(cards, 3): # 3개의 카드로 이루어진 모든 경우의 수 확인
    if sum(card) <= M:              # M보다 작거나 같은 조건 충족 시
        max_num = max(max_num, sum(card)) # 기존의 최댓값보다 클 시에 새로운 값 저장

print(max_num)