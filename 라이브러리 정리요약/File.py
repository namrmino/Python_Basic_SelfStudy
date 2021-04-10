file_data = open('file.txt')
print(file_data.readline(), end="")
file_data.close()

with open('file.txt') as file_data:
    # 기본적으로 사용하는 함수를  with문 안에 사용하면 되며
    # with문을 나올 때 close를 자동으로 불러줍니다.
    print(file_data.readline(), end="")