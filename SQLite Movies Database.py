import sqlite3

connection = sqlite3.connect('Movies_list.db')

cursor = connection.cursor()

# I'm creating new table named Movies in the Movies_list Database

query = """CREATE TABLE MOVIES
           (NAME VARCHAR(255), ACTOR VARCHAR(255), ACTRESS VARCHAR(255), DIRECTOR VARCHAR(255), RELEASE_YEAR INT)
        """

cursor.execute(query)

cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, ACTRESS, DIRECTOR, RELEASE_YEAR)
                VALUES ('MS DHONI', 'Sushant Singh', 'Kiara Advani', 'Neeraj Pandey', 2016)
            """)
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, ACTRESS, DIRECTOR, RELEASE_YEAR)
                VALUES ('SULTAN','Salman Khan', 'Anushka Sharma','Ali Abbas Zafar',2016)
            """)
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, ACTRESS, DIRECTOR, RELEASE_YEAR)
                VALUES ('KABIR SINGH','Sahid Kapur', 'Kiara Advani','Sandeep Reddy',2019)
            """)
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, ACTRESS, DIRECTOR, RELEASE_YEAR)
                VALUES ('KESARI','AKSHAY KUMAR', 'Pariniti Chopra','Anurag Singh',2019)
            """)
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, ACTRESS, DIRECTOR, RELEASE_YEAR)
                VALUES ('BHUJ','Ajay Devgan', 'Nora Fatehi','Abhishek Dudhaiya',2021)
            """)
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, ACTRESS, DIRECTOR, RELEASE_YEAR)
                VALUES ('SHERSHAAH','Sidharth Malhotra', 'Kiara Advani','Vishnuvardhan',2021)
            """)
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, ACTRESS, DIRECTOR, RELEASE_YEAR)
                VALUES ('LUDO', 'Pankaj Tripathi', 'Sanya Malhotra', 'Anuraj Basu', 2020)
            """)

connection.commit()

cursor.execute("""SELECT * FROM MOVIES""")
# It will print each row of the Table
result1 = cursor.fetchall()
for row in result1:
    print(row)


print("******************")


cursor.execute("""SELECT * FROM MOVIES
                WHERE ACTRESS='Kiara Advani'
            """)
# It will show all movies in which actress is "Kiara Advani"
result2 = cursor.fetchall()
for row in result2:
    print(row)


print("******************")


cursor.execute("""SELECT * FROM MOVIES
                WHERE RELEASE_YEAR>=2019
            """)
# It will show all movies that are released in 2019 and after 2019
result3 = cursor.fetchall()
for row in result3:
    print(row)

connection.close()