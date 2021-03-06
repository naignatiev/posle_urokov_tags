from tagger import START_TAGS, NaiveTagger, get_id_by_tag
from utils import with_con_cur
import psycopg2.extras


@with_con_cur
def init_starts_db(cur):
    sql_q = 'insert into tag (tag_id, tag_name) values %s'
    data = [
        (i, t) for i, t in enumerate(START_TAGS)
    ]
    psycopg2.extras.execute_values(cur, sql_q, data, template=None, page_size=100)


@with_con_cur
def get_dummy_data_org(cur=None):
    from dummy_data import orgs, locs

    for i, (name, desc) in enumerate(orgs):
        cur.execute("INSERT INTO address(latitude, longitude) values (%s, %s) returning address_id", locs[i])
        address_id = cur.fetchone()[0]
        org_id = i + 1333
        cur.execute("INSERT INTO organization (vk_group_id, name, description, address_id) values(%s, %s, %s, %s)",
                    (org_id, name, desc, address_id))
        for tag in NaiveTagger(name + ' ' + desc).get_tag():
            cur.execute("INSERT INTO org2tag (org_id, tag_id) values(%s, %s)",  (org_id, get_id_by_tag(tag)))


@with_con_cur
def get_dummy_data_child(cur):
    def add_child(name, y, m, d, l0, l1, tags):
        from datetime import date
        date = date(y, m, d)
        cur.execute("INSERT INTO address(latitude, longitude) values (%s, %s) returning address_id",
                    (l0, l1))
        address_id = cur.fetchone()[0]
        cur.execute("INSERT INTO child(name, address_id, birth_date) values (%s, %s, %s) returning child_id",
                    (name, address_id, date))
        child_id = cur.fetchone()[0]
        for tag in tags:
            cur.execute("INSERT INTO child2tag(child_id, tag_id) values (%s, %s) returning child_id",
                        (child_id, get_id_by_tag(tag)))
    add_child('Петя', 2009, 8, 5, 53.991, 38.992, tags=['Шахматы'])
    add_child('Толя', 2011, 11, 5, 53.2123, 51.2241, tags=['История', 'Химия'])


@with_con_cur
def get_dummy_score(cur):
    sql_q = 'insert into tag (tag_id, tag_name) values %s'
    data = [
        (2, 1335, 5),
        (2, 1336, 4),
        (3, 1334, 4),
    ]
    psycopg2.extras.execute_values(cur, sql_q, data, template=None, page_size=100)


if __name__ == '__main__':
    get_dummy_data_child()
