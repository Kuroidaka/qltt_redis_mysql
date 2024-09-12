import mysql.connector
import time

# Kết nối tới MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Idaka123",
    database="phamdoancanh"
)

# Tạo đối tượng cursor
cursor = conn.cursor()

# Đo thời gian truy vấn MySQL
start_time = time.time()


# Thực hiện 1 truy vấn MySQL
for i in range(1):
    cursor.execute("SELECT * FROM phamdoancanh.restaurant where id=38;")
    result = cursor.fetchall()

end_time = time.time()
execution_time_1 = end_time - start_time

print(f"Thời gian thực hiện truy vấn MySQL khi thực hiện 1 truy vấn: {execution_time_1} giây")

# Đo thời gian truy vấn MySQL
start_time = time.time()

# Thực hiện 1000 truy vấn MySQL
for i in range(1000):
    cursor.execute("SELECT * FROM phamdoancanh.restaurant where id=38;")
    result = cursor.fetchall()

end_time = time.time()
execution_time_2 = end_time - start_time

print(f"Thời gian thực hiện truy vấn MySQL khi thực hiện 1000 truy vấn: {execution_time_2} giây")

# Đóng kết nối
cursor.close()
conn.close()
