from sqlalchemy import create_engine

def send_cleaned_data_to_db(cleaned_data, table_name, username='postgres', password='1864', host='localhost', port='5432', database='data_hub'):
      # Step 1: Create a database connection string
    connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
    
    # Step 2: Create an SQLAlchemy engine
    engine = create_engine(connection_string)
    
    # Step 3: Send the DataFrame to the database
    cleaned_data.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Data successfully sent to the '{table_name}' table in the '{database}' database!")


