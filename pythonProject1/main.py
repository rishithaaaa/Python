import mysql.connector
import json
import xlrd

conn = mysql.connector.connect(host="localhost", user="root", passwd="crimson", database="invtry")
cur = conn.cursor()
loc = "C:/Users/mamid/Downloads/product_finale.xlsx"
x = xlrd.open_workbook(loc)
a = x.sheet_by_index(0)
a.cell_value(0, 0)
l = []
for i in range(1, 3780):
    l.append(tuple(a.row_values(i)))

q = f"insert into product_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(q, l)
conn.commit()
conn.close()