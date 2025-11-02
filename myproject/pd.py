import pandas as pd

  # 1. Read Excel files (you can replace these with the actual file paths)
df1 = pd.read_excel("G:/AI_Backend/Django_class/myproject/customers_file_1.xlsx", engine="openpyxl")

# print(df1.head())   
def insert_data():
    for _, row in df1.iterrows():
        customer_id=row['customer_id']
        print(customer_id)

insert_data()

