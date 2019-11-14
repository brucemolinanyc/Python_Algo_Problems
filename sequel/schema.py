import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "taboola.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename="taboolaCampaigns"))

        SQL = """CREATE TABLE taboolaCampaigns(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id VARCHAR(128),
                start_date VARCHAR(128),
                end_date VARCHAR(128),
                zipcode_restriction_type VARCHAR(128)
            );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="taboolaZipCodes"))

        SQL = """CREATE TABLE taboolaZipCodes(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id VARCHAR(128),
            feature VARCHAR(128),
            value VARCHAR(128)
            );"""

        cur.execute(SQL)

schema()