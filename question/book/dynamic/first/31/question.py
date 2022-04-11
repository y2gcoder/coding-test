for _ in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    rt = []
    index = 0
    for i in range(n):
        rt.append(array[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = rt[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = rt[i + 1][j - 1]
            left = rt[i][j - 1]
            rt[i][j] = rt[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, rt[i][m - 1])

    print(result)