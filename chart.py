# usage: python chart.py range
# range options = day,week,month,year,all

import sqlite3, json, sys, pandas

config = None
ranges = {
    "day": 1,
    "week": 7,
    "month": 30,
    "year": 365,
    "all": -1
}

def load(conn, days):
    if (days < 0):
        # days = today
    
    sql = "SELECT * from prices where mdy > %(days)s"
    # today - days 
    params = {'days': days}

    data = pandas.read_sql(sql, con, index_col="id", params=params, parse_dates={'mdy':'D'}
    return data 


def chart(data):
    pass


if __name__ == "__main__":
    try:
        with open("profile.conf") as f:
            config = json.load(f)
    except Exception as e: 
        print "Profile failed to load:\n" + str(e)
        return

    conn = sqlite3.connect(config["yahoo_code"] + ".db")

    if (len(sys.argv) < 2 or sys.argv[1].lower() not in ranges):
        print "Missing or invalid arguments"
        return
    days = ranges[sys.argv[1].lower()]

    data = load(conn, days)
    chart(data)


