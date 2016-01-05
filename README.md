# stock-tracker
Track the performance of a stock, bond, or index using the Yahoo finance API

[Rough documentation](https://code.google.com/p/yahoo-finance-managed/wiki/csvQuotesDownload)

### Historical data
In order to backfill historical data, download the last X years of daily price figures (going back to 2000) from the main yahoo finanical website. Go to your particular stock or bond and select "Historical Prices" and "Download to Spreadsheet". Use `backfill.py` to populate the database.

### Alerts
Take `update.py` and cron it to run on a daily basis. It appends the day's price to the database and sends out any alerts based off of preset thresholds. 

### Analtyics
Use `chart.py` to graph the last week, 30 days, year, or all values. 

### Requirements
sqlite, pandas, matplotlib
