
import sqlite3, requests, smtplib, re, json
from difflib import SequenceMatcher as SM

config = None
conn = None
from_addr = "stock_alerts@gmail.com"
sms_gateway = {
    "at&t": "txt.att.net",
    "cricket": "mms.cricketwireless.net",
    "republic": "text.republicwireless.com",
    "tmobile": "tmomail.net",
    "sprint": "pm.sprint.com",
    "verizon": "vtext.com",
    "uscellular": "email.uscc.net",
    "virgin": "vmobl.com",
    "boost": "myboostmobile.com",
    "alltel": "message.alltel.com",
    "nextel": "messaging.nextel.com"
}

def notify_phone(number, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login( config['gmail_address'], config['gmail_password'])

        number = re.sub("[^0-9]", "", str(number))
        server = match_carrier( config['phone_carrier'] )
        server.sendmail(from_addr, number + "@" + server, message)
    except Exception as e:
        print "Text alert failed:\n" + str(e)

def notify_email(to_addr, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(config['gmail_address'], config['gmail_password'])
        server.sendmail(from_addr, to_addr, message)
    except Exception as e:
        print "Email alert failed:\n" + str(e)


def match_carrier(given):
    carriers = sms_gateway.keys()
    matches = []
    given = given.lower()

    for i in range(len(carriers)):
        m = SM(None, given, carriers[i]).ratio()
        matches.append(m)

    k = matches.index(max(matches))
    return sms_gateway[ carriers[k] ]


if __name__ == "__main__":
    try:
        with open("profile.conf") as f:
            config = json.load(f)
    except Exception as e: 
        print "Profile failed to load:\n" + str(e)
        return

    conn = sqlite3.connect(config["yahoo_code"] + ".db")

    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + config["yahoo_code"] + "&f=nghl1s"
    r = requests.get(url)
    data = r.text.split(",")
    close_price = data[3]
    # "Vanguard 500 Index Fd Admiral S",N/A,N/A,185.64,"VFIAX"

    # TODO: get date, load into database


