#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re
import csv
from io import StringIO
from datetime import datetime
from icalendar import Calendar, Event


def parse_agenda(filename):
    f = open(filename, 'r').read()
    print(f)
    talks, workshops = re.findall('(?:Talk Agenda\n[=]*(.*)Workshop Agenda\n[=]*(.*))', f, re.S)[0]
    tday1, tday2, tday3 = re.findall('Tuesday 20 October 2015 \(Talks\)\n[-]*(.*)Wednesday 21 October 2015 \(Talks\)\n[-]*(.*)Thursday 22 October 2015 \(Talks\)\n[-]*(.*)', talks, re.S)[0]
    days = []
    for d in [tday1, tday2, tday3]:
        # remove lines starting with {
        d = re.sub(r'(?m)^\{.*\n?', '', d)
        c = csv.reader(StringIO(d), delimiter='|')
        tmp = []
        for row in c:
            if len(row) != 4:
                continue
            x, time, data, z = row
            if time in [' Time ', ':----:']:
                continue
            tmp.append((time.strip(), data.strip()))
        days.append(tmp)
    return days


def convert(cal, days):
    for day, d in days:
        for time, data in d:
            if len(data) == 0:
                continue
            event = Event()
            h, m = time.split(':')
            if data.startswith('['):
                try:
                    # Title + speaker
                    t, s = data.split(') (')
                    title = re.findall('\[(.*)\].*', t)
                    event.add('summary', title)
                    speakers = s.split('), ')
                    for s in speakers:
                        speaker = re.findall('\[(.*)\].*', s)
                        event.add('organizer', speaker)
                except:
                    try:
                        title = re.findall('\[(.*)\].*', data)[0]
                        event.add('summary', title)
                    except:
                        print("blah ", data)
            else:
                event.add('summary', data)
            event.add('location', 'Room Europe')
            event.add('dtstart', day.replace(hour=int(h), minute=int(m)))
            cal.add_component(event)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert agenda to ical.')
    parser.add_argument('-m', '--markdown', required=True, help='MD file to convert')
    args = parser.parse_args()

    days = parse_agenda(args.markdown)
    to_convert = zip([datetime(2015, 10, 20, 0, 0), datetime(2015, 10, 21, 0, 0), datetime(2015, 10, 22, 0, 0)], days)
    cal = Calendar()
    convert(cal, to_convert)
    ical = cal.to_ical()
    with open('talks.ical', 'wb') as f:
        f.write(ical)
