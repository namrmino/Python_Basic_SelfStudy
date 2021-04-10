import openpyxl
import re
import os


# 경로
os.getcwd()
os.path.abspath('.')
os.path.abspath('.\\Scripts')

os.path.join('User', 'Happy', 'Desktop')
os.chdir('C:\\Users\\happy\\Desktop')

os.makedirs('.\\Test')

# Read
with open('file.txt') as file_data:
    # 기본적으로 사용하는 함수를  with문 안에 사용하면 되며
    # with문을 나올 때 close를 자동으로 불러줍니다.
    print(file_data.readline(), end="")

helloFile = open('.\\Test\\2.txt')
helloFile.readlines()
helloContent = helloFile.read()

file_data = open('file.txt')
print(file_data.readline(), end="")
file_data.close()

# Write
baconFile = open('bacon.txt', 'w')
baconFile = open('bacon.txt', 'a')
baconFile.write('Hello world!\n')
baconFile.close()