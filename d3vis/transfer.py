import json
import csv
def main():
  myFile = open('tickerdata.json', 'r')
  print "hello"
  x = json.load(myFile)
  print x
  f = csv.writer(open("test.csv", "wb+"))

  # Write CSV Header, If you dont need that, remove this line
  f.writerow(["DATE", "IBM US Equity"."LAST_PRICE", "MSFT US Equity"."LAST_PRICE", "AAPL US Equity"."LAST_PRICE", "AMGN US Equity"."LAST_PRICE", "SPY US Equity"."LAST_PRICE"])

for x in x:
    f.writerow([x["IBM US Equity"."DATE"], x["IBM US Equity"."LAST_PRICE"], x["MSFT US Equity"."LAST_PRICE"], x["AAPL US Equity"."LAST_PRICE"], x[ "AMGN US Equity"."LAST_PRICE"], x["SPY US Equity"."LAST_PRICE"])