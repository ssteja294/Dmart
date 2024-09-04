# MySQL using Python

import mysql.connector

DbConnection = mysql.connector.connect(host='138.68.140.83', user='saiteja', password='Saiteja@123', database='dbSaiteja')
DbCursor = DbConnection.cursor()
ItemTable = "Item"

def LoadFields():
  DbCursor.execute(f"SHOW COLUMNS FROM {ItemTable}")
  global Fields
  Fields = [FieldName[0] for FieldName in DbCursor.fetchall()]

def PrintItems():
  DbCursor.execute(f"SELECT * FROM {ItemTable}")
  Items = DbCursor.fetchall()
  for Item in Items:
    for FieldCounter, Field in enumerate(Fields):
      print(f"{Field}: {Item[FieldCounter]}")
    print("\n")

LoadFields()
PrintItems()