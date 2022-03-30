s = list(input())

alphabets = []
numbers = 0

for i in s:
    if i.isdigit():
        numbers += int(i)
    else:
        alphabets.append(i)

alphabets.sort()
print(''.join(alphabets) + str(numbers))
