x = int(input())

d = [0] * 30001

'''

d[2] = 1
d[3] = 1
d[5] = 1

d[4] = d[4/2] + 1 or d[3] + 1
d[6] = d[5] + 1 or d[2] + 1 or d[3] + 1
d[7] = d[6] + 1
d[8] = d[7] + 1
d[9] 3 
d[10] 2
d[11] 3
d[12] 3
d[13] 4
d[14] 

'''
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])