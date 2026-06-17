import mysql.connector
import random

con = mysql.connector.connect(host="localhost", user="root", password="tiger", database="johan")
cursor = con.cursor()

names = ["Johan", "Sven", "Erik", "Lars", "Anna", "Maria", "Karin", "Olof", "Gustav", "Sara","Anders", "Per", "Nils", "Eva", "Lena", "Björn", "Mikael", "Fredrik", "Johanna", "Emil"]
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Camera", "Printer", "Monitor", "Keyboard", "Mouse", "Speaker","Router", "External Hard Drive", "Smartwatch", "Fitness Tracker", "Drone", "VR Headset", "Gaming Console", "Projector", "Microphone", "Webcam"]

cursor.execute("SELECT COALESCE(MAX(id), 0) FROM store")
prev = cursor.fetchone()[0] + 1
print(prev-1)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
rows = []

for i in range(1_00):
    name = ''.join(random.choice(chars) for _ in range(10))
    product = random.choice(products)
    qty = random.randint(1, 10**5)
    price = random.uniform(10.0, 1000.0) * qty

    rows.append(
        (i + prev, name, product, qty, round(price, 2))
    )

cursor.executemany(
    "INSERT INTO store VALUES (%s,%s,%s,%s,%s)",
    rows
)
con.commit()
con.close()