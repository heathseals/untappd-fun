#!/usr/bin/env python3
import json, datetime, argparse

def avg_abv(abv_list):
    avg_abv = sum(abv_list) / len(abv_list)
    return round(avg_abv,2)

def per_year(data):
    date = datetime.date.today()
    for y in range(2010, int(date.year) + 1):
        checkin = 0
        abv_list = []
        for d in data:
            if d['created_at'].find(str(y)) >= 0:
                if float(d['beer_abv']) > 0:
                    abv_list.append(float(d['beer_abv']))
                checkin = checkin + 1
        print(f"{y}      : {max(abv_list)}% max | {avg_abv(abv_list)}% avg | {min(abv_list)}% min | {checkin} unique check-ins")

def all_years(data):
    checkin = 0
    abv_list = []
    for d in data:
        if float(d['beer_abv']) > 0:
            abv_list.append(float(d['beer_abv']))
        checkin = checkin + 1
    print(f"All Years : {max(abv_list)}% max | {avg_abv(abv_list)}% avg | {min(abv_list)}% min | {checkin} unique check-ins")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='name of the json file to extract uniques from')
    args = parser.parse_args()

    with open(args.file) as f:
        data = json.load(f)
        f.close

    print(f"Working on {args.file}")

    per_year(data)
    all_years(data)
