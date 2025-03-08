def func(N, info):
    possible = []
    for i in range(1, N-1):
        l, r = info[i-1], info[i+1]
        if l > 0 and r > 0:
            min_t = min(l, r)
            possible.append(info[i] + min_t)
    
    if possible and max(possible) > max(info):
        return max(possible)
    return max(info)


if __name__ == '__main__':
    n = int(input())
    towers = list(map(int, input().split()))

    answer = func(n, towers)

    print(answer)