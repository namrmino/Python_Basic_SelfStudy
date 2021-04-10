# 리스트 생성
a = list(range(10))
b = list(range(10, 0, -1))
c = list(range(10, 20, 2))
list('Hello') # ['H', 'e', 'l' ,'l', 'o']

# 리스트 조작
a = [10, 20] # a[0] = 10 / a[1] = 20
a.append(30) # a = [10, 20, 30]
a.append([50, 60]) # a = [10, 20, [50, 60]]
a.extend([20, 30]) # a = [10, 20, 30]
a.insert(2, 500) # a = [10, 20, 500]
a.remove(20) # a = [10]
a.pop() # = 30 / a = [10] # 마지막 값 반환, 삭제
a.index(20) # = 1
a.count(10) # = 1 리스트의 특정 값 개수 반환
a.reverse() # = [20, 10]
a.sort() # 작은 순서(오름차순) 정렬
a.sort(reverse=True) # 큰 순서(내림 차순) 정렬
a.clear() # 리스트의 모든 값 삭제

a = [10, 20, 30]
del a[1] # a = [10, 30]
del a[1:2] # a = [10, 30]
del a[:] # a = []

# 리스트 복사
a = [0, 0, 0]
b = a.copy() # a is b = False

# 리스트 연산
a = [10, 20]
b = [1, 2]
c = a + b # [10, 20, 1, 2]
c = a * 2 # [10, 20, 10, 20]

# for에서 인덱스와 요소의 값 동시 출력
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)
    
i = 0
while i < len(a):
    print(a[i])
    i += 1

# 리스트 특정 값 확인
21 in a # True
21 not in a # False

# 리스트(튜플)의 가장 큰 수, 가장 작은 수 구하기
a = [38, 19, 53, 62]
min(a) # = 19
max(a) # = 62

# 리스트 표현식 사용
a = [i for i in range(10)] # = [0, ~9]
b = list(i for i in range(10)) # = [0, ~9]
c = [i + 5 for i in range(10)] # = [5, 6 ~14]
d = [i * 2 for i in range(10)] # = [0, 2, 18]

a = [i for i in range(10) if i % 2 ==0] # [0, 2, 4, 6, 8]
b = [i + 5 for i in range(10) if i % 2 == 1] # 6, 8, 10, 12, 14]

a= [i* j for j in range(2, 10)
         for i in range(1,10)] # [2, 4, 6//3, 6, 9//~81]

# 리스트에 map 함수 사용
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))
a = [1.2, 2.5, 3.7]
a = list(map(int, a)) # = [1, 2, 3]
a = list(map(str, a)) # = ['1', '2', '3']

# 튜플의 정보 연산
a = (10, 20, 30, 20, 40)
a.count(20) # 2
a = (10, 20, 30)
b = (1, 2, 3)
c = a + b # (10, 20, 30, 1, 2, 3)
d = a * 3 # (10, 20, 30, 10, 20 ~30)

a = (38, 21, 53)
53 in a # True

a = tuple(i for i in range(10) if i % 2 == 0) # = [0, 2, 4, 6, 8]

a = (1.2, 2.5, 3.7)
a = tuple(map(int, a)) # (1, 2, 3)

# 리스트 표현식을 활용한 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
a = [[0] * 2 for i in range(3)]