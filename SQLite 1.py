import sqlite3

connection  = sqlite3.connect('Movies.db')

cursor = connection.cursor()

table = """CREATE TABLE MOVIES 
        ( NAME VARCHAR(255), ACTOR VARCHAR(255), RATING FLOAT(2,1))        
        """

cursor.execute(table)

cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, RATING) 
                VALUES ('MS DHONI', 'SUSHANT', 9.1)""")
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, RATING) 
                VALUES ('CHICHORE', 'SUSHANT', 9.4)""")
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, RATING)
                VALUES ('DIL BECHARA', 'SUSHANT', 8.5)""")
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, RATING)
                VALUES ('BHUJ', 'AJAY', 9.2)""")
cursor.execute("""INSERT INTO MOVIES (NAME, ACTOR, RATING)
                VALUES ('DANGAL', 'AMIR', 8.3)""")

print("Data Inserted in the table: ")

cursor.execute("SELECT * FROM MOVIES")

results = cursor.fetchall()
print(results)

connection.commit()

connection.close()

