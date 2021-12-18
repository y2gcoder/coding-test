n, m = map(int, input().split())
input_list = []
for _ in range(n):
    input_item = list(map(int, input().split()))
    input_item.sort()
    input_list.append(input_item)

min_data = []
for i in range(n):
    min_data.append(min(input_list[i]))

print(max(min_data))
