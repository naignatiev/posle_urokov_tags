from tagger import START_TAGS
import psycopg2
import psycopg2.extras
from database_cfg import USER, PASSWORD, HOST, PORT, DATABASE


def init_starts_db():
    connection = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
    cursor = connection.cursor()
    sql_q = 'insert into tag (tag_id, tag_name) values %s'
    data = [
        (i, t) for i, t in enumerate(START_TAGS)
    ]
    psycopg2.extras.execute_values(cursor, sql_q, data, template=None, page_size=100)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    init_starts_db()
