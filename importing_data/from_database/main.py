import data_retriev_from_mysql
import pandas as pd

sql_employees = "select * from employees_tbl"
sql_city = "select * from city"

conn_employees = data_retriev_from_mysql.connection( "localhost", "root", "denis1987", "employees_database")
conn_city = data_retriev_from_mysql.connection( "localhost", "root", "denis1987", "world")

##### employees table
employees = data_retriev_from_mysql.data_retrieval(conn_employees, sql_employees)
df_employees = pd.DataFrame(employees, columns = ["id", "name", "departmetn", "salary"])
print(df_employees)

print("/////////////////////////")
##### city table
city = data_retriev_from_mysql.data_retrieval(conn_city, sql_city)
df_city = pd.DataFrame(city)
print(df_city.shape)