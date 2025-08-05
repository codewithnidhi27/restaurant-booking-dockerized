import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="psswd",
    database="restaurant_management"
)

cursor = conn.cursor()

# Fetch data from restaurants table
cursor.execute("SELECT * FROM restaurants")
restaurants = cursor.fetchall()

print("\n--- Restaurants Table ---")
for row in restaurants:
    print(row)

# Fetch data from reservations table
cursor.execute("SELECT * FROM reservations")
reservations = cursor.fetchall()

print("\n--- Reservations Table ---")
for row in reservations:
    print(row)

# Close connection
cursor.close()
conn.close()
