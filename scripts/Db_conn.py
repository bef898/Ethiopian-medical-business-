# db_connection.py

import psycopg2

# Function to connect to PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="data_hub",      # Change to your database name
            user="postgres",       # Change to your username
            password="1864",   # Change to your password
            host="localhost",           # Change if hosted elsewhere
            port="5432"                 # Default PostgreSQL port
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to create a table for storing YOLO detections
def create_detection_table(conn):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS yolo_detections (
        id SERIAL PRIMARY KEY,
        image_name TEXT,
        object_class TEXT,
        confidence FLOAT,
        xmin_value FLOAT,
        ymin FLOAT,
        xmax_value FLOAT,
        ymax FLOAT
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'yolo_detections' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
