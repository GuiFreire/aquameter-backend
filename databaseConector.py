from mysql.connector import connect

def mysqlconnection ():
    connection = connect(
        host = "xxxx",
        user = "xxxxx",
        password = "xxxxx",
        database = "xxxxx"
    )

    return connection