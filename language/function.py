def add(a, b):
    return a + b

print(add(3, 7))


def add(a, b):
    print('함수의 결과: ', a + b)

add(3, 7)


def add(a, b):
    print('함수의 결과: ', a + b)

add(b = 3, a = 7)


a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)


def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))