#!/usr/bin/env python3
import json
import datetime
import argparse


def avg_abv(abv_list):
    avg_abv = sum(abv_list) / len(abv_list)
    return round(avg_abv, 2)


def uniques(data):
    uniques = list({x['bid']: x for x in data}.values())
    duplicates = len(data) - len(uniques)
    noabv = [x for x in uniques if x['beer_abv'] == '0']
    print(type(uniques))
    print(f'\n{len(data)} total check-ins with {len(uniques)} unique beer id\'s, '
          f'{duplicates} duplicates check-ins, and ')
    print(f'{len(noabv)} had no abv data.\n')
    return uniques


def per_year(data):
    date = datetime.date.today()
    for y in range(2010, int(date.year) + 1):
        checkin = 0
        abv_list = []
        for d in data:
            if str(y) in d['created_at'] and float(d['beer_abv']) > 0:
                abv_list.append(float(d['beer_abv']))
                checkin = checkin + 1
        print(f'{y}      : {max(abv_list)}% max | {avg_abv(abv_list)}% avg | {min(abv_list)}% min | {checkin} check-ins')


def all_years(data):
    checkin = 0
    abv_list = []
    for d in data:
        if float(d['beer_abv']) > 0:
            abv_list.append(float(d['beer_abv']))
            checkin = checkin + 1
    print(
        f'All Years : {max(abv_list)}% max | {avg_abv(abv_list)}% avg | {min(abv_list)}% min | {checkin} check-ins')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='name of the untappd json export file')
    args = parser.parse_args()

    with open(args.file) as f:
        data = json.load(f)
        f.close

    print(f'Working on {args.file}')

    per_year(data)
    all_years(data)
    uniques(data)
