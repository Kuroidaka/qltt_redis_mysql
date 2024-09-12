
import pandas as pd
import redis
import json

# Read the CSV file into a pandas DataFrame
file_path = './FastFoodRestaurants.csv'
df = pd.read_csv(file_path)

# Replace NaN values with None
df = df.where(pd.notnull(df), None)

# Establish a connection to Redis
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

# Insert data into Redis
def insert_data_to_redis(redis_conn, df):
    for i, row in df.iterrows():
        # Create a unique key for each row (e.g., restaurant:<id>)
        key = f"restaurant:{i+1}"

        # Create a dictionary of the row data
        data = {
            'address': row['address'],
            'city': row['city'],
            'country': row['country'],
            'keys': row['keys'],
            'latitude': row['latitude'],
            'longitude': row['longitude'],
            'name': row['name'],
            'postalCode': row['postalCode'],
            'province': row['province'],
            'websites': row['websites']
        }

        # Convert the data to JSON format and store in Redis
        redis_conn.set(key, json.dumps(data))

# Provide Redis connection details
redis_conn = create_redis_connection("localhost", 6379, 0)

# Insert data into Redis
if redis_conn:
    print("Inserting data into Redis...")
    insert_data_to_redis(redis_conn, df)
    print("Data inserted into Redis successfully")
