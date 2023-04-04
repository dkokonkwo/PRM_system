import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="David@2002",
    database="prm_system"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE IF NOT EXISTS prm_system")
# mycursor.execute("CREATE TABLE IF NOT EXISTS login (agent_id VARCHAR(50) NOT NULL, passwd VARCHAR(50) NOT NULL, plot VARCHAR(50) NOT NULL, id int NOT NULL PRIMARY KEY AUTO_INCREMENT)")

#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_1', '#p@sswd1', 'ALU park,Plot J'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_2', '#p@sswd2', 'Kigali park,Plot I'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_3', '#p@sswd3', 'ALU park,Plot D'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_4', '#p@sswd4', 'Kigali park,Plot F'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_5', '#p@sswd5', 'ALU park,Plot G'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_6', '#p@sswd6', 'Uganda park,Plot E'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_7', '#p@sswd7', 'Nigeria park,Plot C'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_8', '#p@sswd8', 'ALU park,Plot B'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_9', '#p@sswd9', 'Kampala park,Plot H'))
#mycursor.execute("INSERT INTO login (agent_id, passwd, plot) VALUES (%s, %s, %s)", ('agent_10', '#p@sswd10', 'ALU park,Plot A'))
#db.commit()

mycursor.execute("SELECT * FROM login")

