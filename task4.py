# Task 4: Extract Two Boundary Points of Any Given KM Value

from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine('mysql+mysqlconnector://root:@localhost/new_indel')

km_value = 10  # Replace with the desired KM value

query = text("""
    SELECT * FROM path_details
    WHERE km <= :km_value
    ORDER BY km DESC
    LIMIT 2
""")

with engine.connect() as conn:
    results = pd.read_sql(query, conn, params={'km_value': km_value})

print(results)
