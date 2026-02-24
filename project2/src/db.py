import mysql.connector
from mysql.connector import Error

def get_conn():
    return mysql.connector.connect(
        user="root",
        password="TempPass_123!",
        database="csce548_watchlist",
        unix_socket="/tmp/mysql.sock"
    )

def ping():
    try:
        conn = get_conn()
        conn.ping(reconnect=True, attempts=3, delay=2)
        conn.close()
        return True
    except Error as e:
        print("MySQL connection error:", e)
        return False
