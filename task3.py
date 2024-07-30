# Task 3: Query Points with Terrain "Road" without "Civil Station"

from sqlalchemy import create_engine, text
import pandas as pd

# Create engine
engine = create_engine('mysql+mysqlconnector://root:@localhost/new_indel')

# Fetch column names
with engine.connect() as conn:
    column_query = text("SHOW COLUMNS FROM path_details")
    columns = conn.execute(column_query).fetchall()
    column_names = [col[0] for col in columns]
    print("Column names in path_details:", column_names)

# Adjust query based on actual column names
query = text("""
    SELECT * FROM path_details
    WHERE terrain = 'Road' AND terrain NOT LIKE '%Civil Station%'
""")

with engine.connect() as conn:
    results = pd.read_sql(query, conn)

print(results)
