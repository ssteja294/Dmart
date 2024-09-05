# MySQL using Python

import mysql.connector

DbConnection = mysql.connector.connect(host='138.68.140.83', user='saiteja', password='Saiteja@123', database='dbSaiteja')
DbCursor = DbConnection.cursor()


def loadItemFields():
  DbCursor.execute("SHOW COLUMNS FROM Item")
  global itemFields
  itemFields = [FieldName[0] for FieldName in DbCursor.fetchall()]

def printItems():
  DbCursor.execute("SELECT * FROM Item")
  Items = DbCursor.fetchall()
  for Item in Items:
    for itemFieldCounter, itemField in enumerate(itemFields):
      print(f"{itemField}: {Item[itemFieldCounter]}")
    print("\n")

loadItemFields()
printItems()
