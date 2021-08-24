import sqlite3

connection = sqlite3.connect('Movies.db')

cursor = connection.cursor()

# Inserting a new table in a existing database "Movie.db"
# inserting a new table in a Movies DataBase

newtable = """CREATE TABLE SPORTS_MOVIE
            ( NAME VARCHAR(255), ACTOR VARCHAR(255), RATING FLOAT(2,1))        
           """
cursor.execute(newtable)

cursor.execute("""INSERT INTO SPORTS_MOVIE (NAME, ACTOR, RATING) 
                VALUES ('MS DHONI', 'SUSHANT', 9.1)""")
cursor.execute("""INSERT INTO SPORTS_MOVIE (NAME, ACTOR, RATING) 
                VALUES ('CHICHORE', 'SUSHANT', 9.4)""")
cursor.execute("""INSERT INTO SPORTS_MOVIE (NAME, ACTOR, RATING)
                VALUES ('SULTAN', 'SALMAN', 6.5)""")
cursor.execute("""INSERT INTO SPORTS_MOVIE (NAME, ACTOR, RATING)
                VALUES ('GOLD', 'AKSHAY', 8.5)""")
cursor.execute("""INSERT INTO SPORTS_MOVIE (NAME, ACTOR, RATING)
                VALUES ('DANGAL', 'AMIR', 8.3)""")

connection.commit()


connection.close()