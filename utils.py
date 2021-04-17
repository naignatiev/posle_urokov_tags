import psycopg2
import psycopg2.extras

from database_cfg import USER, PASSWORD, HOST, PORT, DATABASE


def with_con_cur(method):
    def wrapper(*args):
        con = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
        cur = con.cursor()
        method(cur, *args)
        con.commit()
        cur.close()
        con.close()
    return wrapper
