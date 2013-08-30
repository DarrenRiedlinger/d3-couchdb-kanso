#!/usr/bin/env python
import csv
import requests
import json
import time

reader = csv.DictReader(open('sp500.csv', 'rb'))

database = "http://127.0.0.1:5984/kanso-d3-example"

to_upload = {"docs": []}

for row in reader:
    # Convert the date into something more suitable for CouchDB
    row['date'] = 1000 * time.mktime(time.strptime(row['date'], "%b %Y"))
    to_upload['docs'].append(row)

print requests.post("%s/_bulk_docs" % database,
                    headers={'content-type': 'application/json'},
                    data=json.dumps(to_upload))
