import sqlite3 as sql


# create database in SQLite3
def createDb():
    conn = sql.connect('file_transfer.db')
    c = conn.cursor()
    initSchema(c) # pass cursor to initSchema()

# init SQLite3 db objects
def initSchema(c):
    # utilizing DROP / CREATE for unit testing
    c.execute("DROP TABLE IF EXISTS program")
    c.execute("CREATE TABLE program (programId INT not null,"
              "programName TEXT not null,"
              "transDate TEXT not null,"
              "tranId INT not null,"
              "FOREIGN KEY (tranId) REFERENCES file_transfer(tranId))")

    c.execute("DROP TABLE IF EXISTS file_transfer")
    c.execute("CREATE TABLE file_transfer (tranId INTEGER PRIMARY KEY AUTOINCREMENT,"
              "recentMods TEXT not null,"
              "transDate TEXT not null,"
              "comments TEXT null)")

    c.execute("DROP TABLE IF EXISTS file_info")
    c.execute("CREATE TABLE file_info (fileId INTEGER PRIMARY KEY AUTOINCREMENT, "
              "root VARCHAR(80) not null,"
              "dest VARCHAR(80) not null,"
              "fileType VARCHAR(20) not null,"
              "tranId INT not null,"
              "FOREIGN KEY (tranId) REFERENCES file_transfer(tranId))")
