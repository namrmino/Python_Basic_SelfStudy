def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)

"""
\'
\"
\t
\n
\\
"""
# %
"""
%s	문자열 (String) / All pplyed  
%c	문자 1개(character)
%d	정수 (Integer)
%f	부동소수 (floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)
"""

# 출력
print("Hello there!\nHow are you?\nI\'m doing fine.")
print(r'That is Carol\'s cat.t')
print('''Dear Alice,
      
Eve's cat han been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

'Hello'.rjust(20, '*')
'Hello'.ljust(20, '-')
'Hello'.center(20)
'Hello'.center(20, '=')

"I eat %d apples." % 3
"I eat %s apples." % "five"

number = 3
"I eat %d apples." % number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

"Error is %d%%." % 98 # %는 %%로 표

"%10s" % "hi"
"%-10sjane." % 'hi'
"%0.4f" % 3.42134234
"%10.4f" % 3.42134234

# format
"I eat {0} apples".format(3)
"I eat {0} apples".format("five")

number = 3
"I eat {0} apples".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

"{0:<10}".format("hi")
"{0:>10}".format("hi")
"{0:^10}".format("hi")
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)
"{{ and }}".format()
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

age = 30
f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'

f'{"hi":<10}'
f'{"hi":>10}'  # 오른쪽 정렬
f'{"hi":^10}'  # 가운데 정렬
f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기

y = 3.42134234
f'{y:0.4f}'  # 소수점 4자리까지만 표현
f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
f'{{ and }}'

# 문자열 관련 함수들
a = "hobby"
a.count('b')

# 문자열 조작
s = 'Hello, world!'
s.replace('world', 'Python') # = 'Hello, Python!'

'apple pear grape'.split() # ['apple', 'pear', 'grape']
'apple,pear,grape'.split(',') # = ['apple', 'pear', 'grape']

",".join('abcd')
",".join(['a', 'b', 'c', 'd'])

s = 'python'
s.upper() # 'PYTHON'
s.lower() # 'python'

s = '   Python   '
s.lstrip() # 'Python   '
s.rstrip() # '   Python'
s.strip()  # 'Python'

s = ', python.'
s.lstrip(',.') # ' python'
s.rstrip(',.') # ', python'
s.strip(',.')  # ' python'

'35'.zfill(4) # '0035'
'3.5'.zfill(6) # '0003.5'
'hello'.zfill(10) # '0000hello'

s = 'apple pineapple'
s.find('pl') # = 2
s.find('xy') # = -1 / 값이 없을시 -1 반환
s.rfind('pl') # 12 / 오른쪽 부터

s.index('pl') # 2
s.rindex('pl') # 12
s.count('pl') # 2 / 문자열 'pl'이 몇 번 나오는지 반환

# 판별
'Hello' in 'Hello World'
'HELLO' in 'Hello World'
'cats' not in 'cats and dogs'

spam = 'Hello world!'
spam.islower()
spam.isupper()
'abc12345'.islower()
'12345'.islower()
'12345'.isupper()

'hello'.isalpha()
'hello123'.isalnum
'hello'.isalnum
'123'.isdecimal
'   '.isspace()
'This IS Title Case'.istitle()
'This Is Title Case 123'.istitle()
'This Is not Title Case'.istitle()
'This Is NOT TiTle Case Either'.istitle()

'Hello world!'.startswith('Hello')
'Hello world!'.endswith('world!')
'abc123'.startswith('abcdef')
'abc123'.endswith('12')
'Helloworld!'.startswith('Hello world!')
'Hello world!'.endswith('Hello world!')