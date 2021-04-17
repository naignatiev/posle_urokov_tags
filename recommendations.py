from utils import with_con_cur


class Recommendation:
    def __init__(self, default_score=4):
        self.default_score = default_score

    def get_organizations(self, ch_id):
        # пока так
        return get_relevant_orgs(ch_id)

    def get_events_for_child(self, ch_id):
        raise NotImplementedError

    def get_events_for_section(self, s_id):
        raise NotImplementedError


@with_con_cur
def get_relevant_orgs(cur, ch_id):
    sql_q = "select distinct org_id from org2tag where tag_id in (select tag_id from child2tag where child_id = %s);"
    cur.execute(sql_q, (ch_id,))
    return cur.fetchall()
