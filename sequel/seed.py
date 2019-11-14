import os
import sqlite3

DIR = os.path.dirname(__file__)
DBFILENAME = "taboola.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = """INSERT INTO taboolaCampaigns(campaign_id, start_date, end_date, zipcode_restriction_type)
                 VALUES 
                 ('1834034', '2019-02-05 12:41:31', '2019-03-16 03:59:59', 'INCLUDE'),
                 ('1835299', '2019-02-05 13:38:01', '9999-12-31 23:59:59', 'EXCLUDE'),
                 ('1836411', '2019-02-05 14:02:00', '9999-12-31 23:59:59', 'INCLUDE'),
                 ('1836366', '2019-02-05 14:03:00', '9999-12-31 23:59:59', 'EXCLUDE')
                 ;"""
        cur.execute(SQL)
  
        SQL = """INSERT INTO taboolaZipCodes(campaign_id, feature, value)
                 VALUES 
                 ('1836366', 'ZIPCODE', 'US_10302'),
                 ('1835299', 'ZIPCODE', 'IN_110019'),
                 ('1835299', 'ZIPCODE', 'IN_110014'),
                 ('1836411', 'ZIPCODE', 'US_07009'),
                 ('1834034', 'ZIPCODE', 'US_75006'),
                 ('1834034', 'ZIPCODE', 'US_75009'),
                 ('1834034', 'ZIPCODE', 'US_75007'),
                 ('1836366', 'ZIPCODE', 'US_10301'),
                 ('1835299', 'ZIPCODE', 'IN_110013'),
                 ('1836366', 'ZIPCODE', 'US_10305'),
                 ('1835299', 'ZIPCODE', 'IN_110003'),
                 ('1834034', 'ZIPCODE', 'US_75002'),
                 ('1836411', 'ZIPCODE', 'US_07006'),
                 ('1835299', 'ZIPCODE', 'IN_110017'),
                 ('1836366', 'ZIPCODE', 'US_10303'),
                 ('1836411', 'ZIPCODE', 'US_07002'),
                 ('1836366', 'ZIPCODE', 'US_10304'),
                 ('1834034', 'ZIPCODE', 'US_75001'),
                 ('1836411', 'ZIPCODE', 'US_07010'),
                 ('1836411', 'ZIPCODE', 'US_07008')
                 ;"""
        cur.execute(SQL)

seed()