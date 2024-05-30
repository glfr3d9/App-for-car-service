import socket
import mysql.connector
from mysql.connector import Error
sock = socket.socket()
sock.bind(('192.168.1.53', 10500))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
conn.close()

data = data.decode()

for i in data:
    if i == "ask":
        type = "ask"
for i in data:
    if i == "check":
        type = "check"
if type == "check":
    for i in data:
        if i == "temp":check = "temp"
        if i == "bar":check = "bar"
        if i == "kol":check = "kol"
        if i == "disk":check= "disk"
        if i == "wh":check = "wh"
match check:
    case "temp": temp = temp+a,
    case "bar": bar = (6.28/(1/v))/v, if bar >= normal: data = "Select instruction from malfunction where i == bar"
    case "kol": (25*2.6)/(1.77*1000) if bar >= normal: data = "Select instruction from malfunction where i == bar"
    case "bar":bar = (6.28 / (1 / v)) / v if bar >= normal: data = "Select instruction from malfunction where i == bar"
    case "kol":(25 * 2.6) / (1.77 * 1000)if bar >= normal: data = "Select instruction from malfunction where i == bar"
if type == "ask":
    db= True
    script = "data {}".format()
try:
    connection = mysql.connector.connect(
        host="localhost",
        database="car_service",
        user="root",
        password="1234"
    )
    if connection.is_connected():

        cursor = connection.cursor(buffered=True)
        cursor.execute("data {}".format())
        record = cursor.fetchone()
        sock.send(record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


