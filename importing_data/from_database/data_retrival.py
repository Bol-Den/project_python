from sqlalchemy import create_engine, text as sqltext
import pandas as pd

engine = create_engine('mysql+mysqlconnector://root:denis1987@localhost:3306/employees_database')
query = "select * from employees_tbl"

df = pd.read_sql_query(con = engine.connect(), sql = sqltext(query))

print(df)