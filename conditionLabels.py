import csv
from os import listdir
from os.path import *
import datetime

MYDIR = 'U:/Downloads/'

onlyfiles = [f for f in listdir(MYDIR) if isfile(join(MYDIR, f))]
for x in onlyfiles:
    if x.startswith('Active'):
        dates = x[23:-4]
        g = dates.replace('-', '')
        print(datetime.datetime.strptime(g, "%m%d%Y"))

data = {}

conditions = {11: 'New',
              4: 'UsedAcceptable',
              3: 'UsedGood',
              2: 'UsedVeryGood',
              1: 'UsedLikeNew'}

with open("U:/Downloads/listings.tsv", mode='r', encoding='utf8') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    for row in csv_reader:
        for item in conditions:
            if row[12] == item:
                data[row[2]] = item
            else:
                pass
#for x in data.values():
#    print(x)

