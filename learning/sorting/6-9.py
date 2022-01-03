array = [('바난나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


# result = sorted(array, key=setting)
result = sorted(array, key=lambda x: x[1])  # 람다 이용
print(result)