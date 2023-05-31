import sqlite3


connection = sqlite3.connect('database.db')
connection.execute(
    """
    CREATE TABLE IF NOT EXISTS STORE (
    name TEXT,
    id INT
    )
    """)


connection.execute(
    """
    CREATE TABLE IF NOT EXISTS PRODUCT (
    name TEXT,
    id INT
    )
    """)



connection.commit()
connection.close()


