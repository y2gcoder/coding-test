'''
입력 조건
첫째 줄에 N, M이 주어진다(1 <= N <= 100, 1 <= M <= 10,000)
이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

출력 조건
첫째 줄에는 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
불가능할 때는 -1 을 출력한다.
'''

n, m = map(int, input().split())

currencies = []
for _ in range(n):
    currencies.append(int(input()))


d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(currencies[i], m + 1):
        if d[j - currencies[i]] != 10001:
            d[j] = min(d[j], d[j - currencies[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

