import pandas as pd
from models.order import *
from models.sale import *

def create_excel(orders, sales):
    df_orders = pd.DataFrame(orders)
    df_sales = pd.DataFrame(sales)
    
    order_columns = [column.key for column in Order.__table__.columns]
    sale_columns = [column.key for column in Sale.__table__.columns]

    df_orders = df_orders[order_columns]
    df_sales = df_sales[sale_columns]

    with pd.ExcelWriter('report.xlsx') as writer:
        df_orders.to_excel(writer, sheet_name='Orders', index=False)
        df_sales.to_excel(writer, sheet_name='Sales', index=False)
