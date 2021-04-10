import sqlite3

class Database:
    def __init__(self, db):
        self.conn= sqlite3.connect(db)
        self.cur= self.conn.cursor()#쿼리 접속
        self.cur.execute("CREATE TABLE IF NOT EXISTS part (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        # create table : db 만들기
        # part : db 이름
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM part") 
        rows= self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO part VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM part WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE part SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part,customer,retailer,price,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__=="__main__":   
    db=Database('store.db')
    db.insert("4GB DDR4 Ram", "Kim Doe", "DD", "180")
