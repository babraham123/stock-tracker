# usage: python backfill.py filename.csv

import sqlite3, json, sys, pandas
config = None

def load(conn, data):
    data = data[['Date', 'Adj Close']]
    data.columns = ['mdy', 'close_price']
    data.to_sql("prices", conn, flavor='sqlite', if_exists='replace', index=True, index_label="id")


if __name__ == "__main__":
    try:
        with open("profile.conf") as f:
            config = json.load(f)
    except Exception as e: 
        print "Profile failed to load:\n" + str(e)
        return

    conn = sqlite3.connect(config["yahoo_code"] + ".db")

    if (len(sys.argv) < 2):
        print "Missing arguments"
        return
    csv_file = sys.argv[1]

    try:
        with open(csv_file) as f:
            data = pandas.read_csv(f)
    except Exception as e: 
        print "Data failed to load:\n" + str(e)
        return

    load(conn, data)