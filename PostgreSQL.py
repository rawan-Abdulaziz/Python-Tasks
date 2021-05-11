import pandas as pd
import pickle
import numpy as np
import sqlalchemy as db
import psycopg2
con = db.create_engine('postgresql://iti:iti@localhost/data_management')
con.table_names()
model = pickle.load(open('/home/rawan/Desktop/Python/model.pkl', 'rb'))
sepal_length = input("Enter sepal_length: ")
sepal_width = input("Enter sepal_width: ")
petal_length = input("Enter petal_length: ")
petal_width = input("Enter petal_width: ")
data=[[sepal_length,sepal_width,petal_length,petal_width]]
df = pd.DataFrame(data, columns = ['sepal_length','sepal_width','petal_length','petal_width'])
df['variety'] = model.predict(df)
df.to_sql(name ='iris',con=con,schema = 'public',if_exists='append',index=False)   
print("Your Row Inserted Successfully Go To PostgreSQL And Check Variety")
