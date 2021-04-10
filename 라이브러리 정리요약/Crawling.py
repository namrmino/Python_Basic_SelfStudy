""" CSS 선택자 서식
* 모든 요소를 선택
<요소 이름> 요소이름을 기반으로 선택
.<클래스 이름> 클래스 이름을 기반으로 선택
#<id 이름> id 속성을 기반으로 선택

<>, <> 쉼표로 구분된 여러 개의 선택자를 모두 선택
<> <> 앞선택자의 후손 중 뒤 선택자에 해당하는 것을 모두 선택
<> > <> 앞 선택자의 자손 중 뒤 선택자에 해당하는 것을 모두 선택
<> + <> 같은 계층에서 바로 뒤에 있는 요소를 선택
<> ~ <> 선택자1부터 선택자2까지의 요소를 모두 선택

<요소>[<속성>] 해당 속성을 가진 요소를 선택
<요소>[<속성>=<값>] 해당 속성의 값이 지정한 값과 같은 요소를 선택
<요소>[<속성>~=<값>] 해당 속성의 값이 지정한 값을 단어로 포함하고 있다면 선택
<요소>[<속성>|=<값>] 해당 속성의 값으로 시작하면 선택
<요소>[<속성>^=<값>] 해당 속성의 값이 지정한 값으로 시작하면 선택
<요소>[<속성>$=<값>] 해당 속성의 값이 지정한 값으로 끝나면 선택
<요소>[<속성>*=<값>] 해당 속성의 값이 지정한 값을 포함하고 있다면 선택
"""



import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import json
import os

# 웹에 있는 소스 가져오기
web_url = "naver.com"
with urllib.request.urlopen(web_url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
all_divs = soup.find_all("div") # find_all
all_ps = soup.find_all("p") # 모든 <p> 태그들을 가져오기
ex_id_divs = soup.find('div', {'id' : 'ex_id'}) # find_all('태그명', {'속성명' : '값' ...})


# HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
    )
data = {}
# my_titles는 list 객체
for title in my_titles:
    data[title.text] = title.get('href')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)



