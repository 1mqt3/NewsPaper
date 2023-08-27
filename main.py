import sqlite3

db = sqlite3.connect('news_paper')

# Create Cursor
c = db.cursor()

db.commit()

db.close()