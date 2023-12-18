import psycopg2


def create():
    conn =  psycopg2.connect(dbname="postgres", user="postgres", password="harshal123", host="localhost", port="5433")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student(ID SERIAL, NAME TEXT,AGE TEXT);''')
    print("table created")
    conn.commit()
    conn.close()



def insert_data():
    conn =  psycopg2.connect(dbname="postgres", user="postgres", password="harshal123", host="localhost", port="5433")
    cur = conn.cursor()
    name = input("enter name")
    age = input("enter age")

    query='''INSERT INTO student (NAME,AGE) VALUES (%s,%s);'''
    cur.execute(query,(name,age))
    print("table created")
    conn.commit()
    conn.close()



insert_data()