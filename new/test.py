import psycopg2
def dtable(): # conect db
    conn = psycopg2.connect(dbname="company",user="gaurav",password="7750",host="localhost",port="5432")


    cursor = conn.cursor()
    print("connection succesfully")
    conn.commit() 
    conn.close()
dtable()


    # def table(): # create table
    #     conn = psycopg2.connect(dbname="company",user="gaurav",password="7750",host="localhost",port="5432")


    #     cursor = conn.cursor()

    #     cursor.execute('''create table employees(Name Text,ID int, Age int);''')
    #     print("Table created succesfully")

    #     conn.commit()
    #     conn.close()
    # table()

def data(): # insert data
    conn = psycopg2.connect(dbname="company",user="gaurav",password="7750",host="localhost",port="5432")


    cursor = conn.cursor()

    cursor.execute('''insert into employees(Name,ID, Age) values('gaurav',01,21);''')
    print("data added succesfully")

    conn.commit()
    conn.close()
data()



def extract():
    conn = psycopg2.connect(dbname="company",user="gaurav",password="7750",host="localhost",port="5432")


    cursor = conn.cursor()

    # cursor.execute('''select * from employees;''')
    # print(cursor.fetchone())

    cursor.execute('''select * from employees;''')
    show=cursor.fetchone()
    print(show[0])
    conn.commit()
    conn.close()

extract()

def update():
    conn = psycopg2.connect(dbname="company", user="gaurav",password="7750", host="localhost", port="5432" )

    cursor = conn.cursor()

    cursor.execute(
        '''update employees set Age = 30 where Name = 'gaurav';''' )

    print("Data updated successfully")

    conn.commit()
    conn.close()

update()


def delete():
    conn = psycopg2.connect(dbname="company",user="gaurav", password="7750",host="localhost",port="5432")

    cursor = conn.cursor()

    cursor.execute(
        '''delete from employees where Name = 'gaurav';'''
    )

    print("Data deleted successfully")

    conn.commit()
    conn.close()

delete()



# def datainput(): # input user through data
#     conn = psycopg2.connect(dbname="company",user="gaurav",password="7750",host="localhost",port="5432")

#     cursor = conn.cursor()
    
#     name=input('Enter yor name: ')
#     id=input('enter id: ')
#     age= input('enter age: ')


#     query='''insert into employees(Name,ID, Age) values(%s,%s,%s);'''
#     cursor.execute(query,(name,id,age))
#     print("data added succesfully")

#     conn.commit()
#     conn.close()
# datainput()
