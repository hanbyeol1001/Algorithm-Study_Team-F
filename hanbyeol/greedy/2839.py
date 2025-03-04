# 상근이는 설탕을 정확하게 Nkg 배달해야 한다.
# 설탕 봉지는 3kg, 5kg 두 가지가 있다.
# input: 배달해야 하는 설탕의 무게 N(kg)
# output: 최대한 적은 봉지로 배달할 경우 배달하는 봉지 개수

n = int(input())

bags = 0

while n >= 0:
    if n % 5 == 0:  # 5kg 봉지로 나누어떨어지면 그걸로 최대한 채우기
        bags += n // 5
        print(bags)
        break
    n -= 3  # 5kg로 나누어떨어지지 않으면 3kg 봉지를 하나 사용
    bags += 1
if n < 0:
    print(-1)  # 3kg로도 나누어떨어지지 않는 경우