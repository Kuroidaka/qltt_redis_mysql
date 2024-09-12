import redis
import time
import json

# Kết nối tới Redis
def create_redis_connection(host_name, port, db):
    try:
        r = redis.StrictRedis(
            host=host_name,
            port=port,
            db=db,
            decode_responses=True  # Ensures the data is returned as a string
        )
        print("Connection to Redis successful")
        return r
    except Exception as e:
        print(f"Error connecting to Redis: {e}")
        return None

# Kết nối tới Redis
redis_conn = create_redis_connection("localhost", 6379, 0)

# Đo thời gian truy vấn Redis cho 1 truy vấn
start_time = time.time()

# Thực hiện 1 truy vấn Redis
for i in range(1):
    data = redis_conn.get("restaurant:38")  # Get restaurant with id 38
    if data:
        result = json.loads(data)
        print(f"Restaurant with ID 38: {result}")

end_time = time.time()
execution_time_1 = end_time - start_time

print(f"Thời gian thực hiện truy vấn Redis khi thực hiện 1 truy vấn: {execution_time_1} giây")


# Đo thời gian truy vấn Redis cho 1000 truy vấn
start_time = time.time()

# Thực hiện 1000 truy vấn Redis
for i in range(1000):
    data = redis_conn.get("restaurant:38")  # Get the same restaurant entry with id 38 for 1000 times
    if data:
        result = json.loads(data)

end_time = time.time()
execution_time_2 = end_time - start_time

print(f"Thời gian thực hiện truy vấn Redis khi thực hiện 1000 truy vấn: {execution_time_2} giây")

# Không cần đóng kết nối Redis vì Redis không yêu cầu như MySQL
