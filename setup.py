from tagger import START_TAGS
import psycopg2
import psycopg2.extras

from database_cfg import USER, PASSWORD, HOST, PORT, DATABASE


def with_con_cur(method):
    def wrapper():
        con = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
        cur = con.cursor()
        method(cur)
        con.commit()
        cur.close()
        con.close()
    return wrapper


@with_con_cur
def init_starts_db(cur):
    sql_q = 'insert into tag (tag_id, tag_name) values %s'
    data = [
        (i, t) for i, t in enumerate(START_TAGS)
    ]
    psycopg2.extras.execute_values(cur, sql_q, data, template=None, page_size=100)


@with_con_cur
def get_dummy_data(cur=None):
    from dummy_data import orgs, locs
    from tagger import NaiveTagger, get_id_by_tag

    for i, (name, desc) in enumerate(orgs):
        cur.execute("INSERT INTO address(latitude, longitude) values (%s, %s) returning address_id", locs[i])
        address_id = cur.fetchone()[0]
        org_id = i + 1333
        cur.execute("INSERT INTO organization (vk_group_id, name, description, address_id) values(%s, %s, %s, %s)",
                    (org_id, name, desc, address_id))
        for tag in NaiveTagger(name + ' ' + desc).get_tag():
            cur.execute("INSERT INTO org2tag (org_id, tag_id) values(%s, %s)",  (org_id, get_id_by_tag(tag)))


if __name__ == '__main__':
    get_dummy_data()
