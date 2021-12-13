# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)


a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)    # 합집합
print(a & b)    # 교집합
print(a - b)    # 차집합


data = {1, 2, 3}
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 트정한 값을 갖는 원소 삭제
data.remove(3)
print(data)