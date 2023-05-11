from mysql.connector import connect

def mysqlconnection (host, user, password, database):
    connection = connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    return connection