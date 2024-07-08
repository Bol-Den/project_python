from data_retriev_from_mysql import connection, data_retrieval
import pandas as pd

# sql_employees = "select * from employees_tbl"
# sql_city = "select * from city"
# sql_trades = "select * from trades"

# conn_employees = data_retriev_from_mysql.connection( "localhost", "root", "denis1987", "employees_database")
# conn_city = data_retriev_from_mysql.connection( "localhost", "root", "denis1987", "world")

##### employees table
# employees = data_retriev_from_mysql.data_retrieval(conn_employees, sql_employees)
# df_employees = pd.DataFrame(employees, columns = ["id", "name", "departmetn", "salary"])
# print(df_employees)

# print("/////////////////////////")
##### city table
# city = data_retriev_from_mysql.data_retrieval(conn_city, sql_city)
# df_city = pd.DataFrame(city)
# print(df_city.shape)

trades_query = "select * from trades"
conn_trades = connection("investments_portfolio")
trades = data_retrieval(conn_trades, trades_query)
trades_column_names = [ "id",
                        "trade_date",
                        "symbol",
                        "description",
                        "currency_primary",
                        "fx_rate_to_base",
                        "quantity",
                        "trade_price",
                        "proceeds",
                        "ib_commission",
                        "net_cash",
                        "cost_basis",
                        "fifo_pnl_realized",
                        "buy_sell"]

df_trades = pd.DataFrame(trades, columns=trades_column_names)
df_trades["total_price"] = float(df_trades["quantity"]) * df_trades["trade_price"]

print(df_trades)
# print(df_trades.dtypes)