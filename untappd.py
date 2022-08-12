#!/usr/bin/env python3
import json
import sys
import datetime

if len(sys.argv) < 2 or len(sys.argv) >= 3:
    print(f"{sys.argv[0]} jsonexport")
    sys.exit()

file = sys.argv[1]

print(f"Working on {file}")

with open(file) as f:
  data = json.load(f)
  f.close

date = datetime.date.today()

def avg_abv(abv_list):
    avg_abv = sum(abv_list) / len(abv_list)
    return round(avg_abv,2)

for y in range(2010, int(date.year) + 1):
    checkin = 0
    abv_list = []
    for d in data:
        if d['created_at'].find(str(y)) >= 0:
            if float(d['beer_abv']) > 0:
                abv_list.append(float(d['beer_abv'])) 
            checkin = checkin + 1
    print(f"{y} : {max(abv_list)}% max | {avg_abv(abv_list)}% avg | {min(abv_list)}% min | {checkin} unique check-ins")

checkin = 0
abv_list = []
for d in data:
    if float(d['beer_abv']) > 0:
        abv_list.append(float(d['beer_abv'])) 
    checkin = checkin + 1
print(f"All Years : {max(abv_list)}% max | {avg_abv(abv_list)}% avg | {min(abv_list)}% min | {checkin} unique check-ins")
