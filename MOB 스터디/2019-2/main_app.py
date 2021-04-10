#To activate this project's virtualenv, run pipenv shell.
#Alternatively, run a command inside the virtualenv with pipenv run.

#pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main_app.py

#mac은 버그있음
#왜 from만 가능한지는 모른다
from tkinter import *
from db_connect import Database
db=Database('store.db')


def populate_list():  #저장 목록 가져오기
    part_list.delete(0,END)#시작시 리스트 비우고 불러오기
    for row in db.fetch():
        part_list.insert(END, row)#끝에 계속 붙이기
        
def add_item():
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(),
              price_text.get())
    part_list.delete(0, END)
    part_list.insert(END, (part_text.get(), customer_text.get(),
                           retailer_text.get(), price_text.get()))
    populate_list()
    clear_item()
    
def select_item(event):
    try:
        global selected_item #배열형태
        index= part_list.curselection()[0] #고른것만 선택
        selected_item= part_list.get(index) #고른거 인덱스

        part_entry.delete(0, END)  #입력칸 비운 뒤,  선택한걸 거기로 입력
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass
    
def remove_item():
    db.remove(selected_item[0])
    populate_list()
    clear_item()
    
def update_item():
    db.update(select_item[0],part_text.get(), customer_text.get(), retailer_text.get(),
              price_text.get())
    populate_list()
    clear_item()
              
def clear_item():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

#create window obj
app= Tk()  #보일 화면을 정의

# part1
part_text= StringVar()
# 텍스트 박스 만들기
part_label= Label(app, text='Part Name', font=('bold',14), pady=20)
#   라벨 텍스트, 폰트와 크기, 패딩
# pady => 세로간격
# padx => 가로간격

# part_label에 대한 디자인 설정하기
part_label.grid(row=0, column=0, sticky=W)
#   해당 ele 배치. 스티키는 어느 4방면에 붙어있는지
# sticky=W는 글자가 나오는 시작위치를 설정한다.(W=west)

# 입력받는 창 만들기
part_entry=Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# part2
customer_text= StringVar()
customer_label= Label(app, text='Customer', font=('bold',14))#, pady=20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry=Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# part3
retailer_text= StringVar()
retailer_label= Label(app, text='Retailer', font=('bold',14))#, pady=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry=Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# part4
price_text= StringVar()
price_label= Label(app, text='Price', font=('bold',14))#, pady=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry=Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# part list
part_list= Listbox(app, height=8, width=50, border=0)#보더는 태두리
part_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# columnspan => 열크기
# rowspan => 행크기

# 스크롤바
scrollbar= Scrollbar()
scrollbar.grid(row=3, column=3)
# 리스트박스랑 스크롤 연결
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)

# bind select
part_list.bind('<<ListboxSelect>>', select_item)

# 버튼 추가1
add_btn= Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

# 버튼 추가2
remove_btn= Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(row=2, column=1, pady=20)

# 버튼 추가3
update_btn= Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(row=2, column=2, pady=20)

# 버튼 추가4
clear_btn= Button(app, text="Clear Part", width=12, command=clear_item)
clear_btn.grid(row=2, column=3, pady=20)


app.title('Part Manager')
app.geometry('700x350')

populate_list()

#start program
app.mainloop()

