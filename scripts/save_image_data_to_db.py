# Function to insert detection data into the PostgreSQL database
def insert_detection_data(conn, detection_data):
    insert_query = """
    INSERT INTO yolo_detections (image_name, object_class, confidence, xmin_value, ymin, xmax_value, ymax)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    cursor = conn.cursor()
    try:
        # Loop through each row of detection data
        for index, row in detection_data.iterrows():
            cursor.execute(insert_query, (
                row['image_name'], row['name'], row['confidence'], row['xmin'], row['ymin'], row['xmax'], row['ymax']
            ))
        conn.commit()
        print("Detections inserted into the database.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

