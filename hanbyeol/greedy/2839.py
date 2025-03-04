# 상근이는 설탕을 정확하게 Nkg 배달해야 한다.
# 설탕 봉지는 3kg, 5kg 두 가지가 있다.
# input: 배달해야 하는 설탕의 무게 N(kg)
# output: 최대한 적은 봉지로 배달할 경우 배달하는 봉지 개수

n = int(input())
answer = 0
while n > 0:
    if n % 5 == 0:
        answer += n // 5
        n -= n
        break
    elif n % 3 == 0:
        if n//3 > 5:
            answer += 3
            n -= 3*5
            continue
        answer += n // 3
        n -= n
        break
    else:
        if n > 5:
            answer += 1
            n -= 5
        else:
            answer += 1
            n -= 3
if n == 0:
    print(answer)
else:
    print(-1)