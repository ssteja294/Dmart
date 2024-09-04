# MySQL using Python

import mysql.connector

DbConnection = mysql.connector.connect(host='138.68.140.83', user='saiteja', password='Saiteja@123', database='dbSaiteja')
DbCursor = DbConnection.cursor()


def LoadFields():
  DbCursor.execute("SHOW COLUMNS FROM Item")
  global Fields
  Fields = [FieldName[0] for FieldName in DbCursor.fetchall()]

def PrintItems():
  DbCursor.execute("SELECT * FROM Item")
  Items = DbCursor.fetchall()
  for Item in Items:
    for FieldCounter, Field in enumerate(Fields):
      print(f"{Field}: {Item[FieldCounter]}")
    print("\n")

LoadFields()
PrintItems()
