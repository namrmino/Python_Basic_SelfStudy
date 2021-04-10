# if, elif, else 모두 사용
x = input()
if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# 숫자 범위와 증가 폭 지정
for i in range(5, 12):
    print('Hello, world!', i)

for i in range(0, 10, 2): # 0부터 8까지 2씩 증가
    print(i) # = 0 2 4 6 8

for i in range(10, 0, -1):
    print('Hello, world!', i)
    # 10 9 8 ~ 1

# 팩토리얼 구하기
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# 입력한 횟수대로 반복
count = int(input('반복할 횟수를 입력하세요: '))

i = 1
while i <= count:
    print('Hello, world! %d' % i)
    i += 1

# break 로 반복문 끝내기
i = 0
while True:
    i += 1
    print(i)
    if i == 100:
        break

for i in range(1, 101):
    if i % 2 != 0:
        continue
    print(i)

#3과 5의 공배수 처리
for i in range(1, 101):              # 1부터 100까지 100번 반복
    if i % 3 == 0 and i % 5 == 0:    # 3과 5의 공배수일 때
        print('FizzBuzz')            # FizzBuzz 출력
    if i % 3 == 0:                   # 3의 배수일 때
        print('Fizz')                # Fizz 출력
    elif i % 5 == 0:                 # 5의 배수일 때
        print('Buzz')                # Buzz 출력
    else:
        print(i)

# 논리 연산자를 사용하지 않고 3과 5의 공배수 처리
for i in range(1, 101):      # 1부터 100까지 100번 반복
    if i % 15 == 0:          # 15의 배수(3과 5의 공배수)일 때
        print('FizzBuzz')    # FizzBuzz 출력
    if i % 3 == 0:           # 3의 배수일 때
        print('Fizz')        # Fizz 출력
    elif i % 5 == 0:         # 5의 배수일 때
        print('Buzz')        # Buzz 출력
    else:
        print(i)

#------------------------------------------------------        

# 2차원 리스트와 튜플 사용
a = [[10, 20], [30, 40], [50, 60]]

# for 반복문 한 번만 사용
for x, y in a:
    print(x, y)

# for 반복문 두 번 사용
for i in a:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 값을 하나씩 꺼냄
        print(j, end=' ')
    print()

# for range 이용 2차원 리스트 요소 인덱스로 접근
for i in range(len(a)):            # 세로 크기
    for j in range(len(a[i])):     # 가로 크기
        print(a[i][j], end=' ')
    print()

# while 반복문을 사용 2차원 리스트 요소 출력
i = 0
while i < len(a):    # 반복할 때 리스트의 크기 활용(세로 크기)
    x, y = a[i]
    print(x, y)
    i += 1           # 인덱스를 1 증가시킴

# while 반복문 두 번 사용
i = 0
while i < len(a):           # 가로 크기
    j = 0
    while j < len(a[i]):    # 세로 크기
        print(a[i][j], end=' ')
        j += 1              # 가로 인덱스를 1 증가시킴
    print()
    i += 1                  # 세로 인덱스를 1 증가시킴

# 반복문으로 2차원 리스트 만들기
a = []    # 빈 리스트 생성

for i in range(3):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가

print(a)

