import sqlite3

with sqlite3.connect("trains.db") as connection:
    c = connection.cursor()
    #c.execute("DROP TABLE trains")
    c.execute("CREATE TABLE trains(train_id TEXT, fromCity TEXT, toCity TEXT, size INTEGER)")
    c.execute("INSERT INTO trains VALUES('S1', 'aylmer', 'ottawa', 700)")
    c.execute("INSERT INTO trains VALUES('B2', 'ottawa', 'montreal', 300)")




