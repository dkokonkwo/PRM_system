import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="David@2002",
    database="testdatabase"
)

mycursor = db.cursor()
# mycursor.execute("CREATE TABLE test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO test (first_name, created, gender) VALUES (%s, %s, %s)", ("Caco", datetime.now(), "F"))

# mycursor.execute("ALTER TABLE test ADD COLUMN class VARCHAR(50) NOT NULL")
# mycursor.execute("ALTER TABLE test CHANGE name first_name VARCHAR(50)")

mycursor.execute("ALTER TABLE test DROP ROW WHERE first_name = 'TOP G'")
db.commit()

mycursor.execute("SELECT * FROM test")

for x in mycursor:
    print(x)
