import os
from datetime import datetime
import csv
messages = {"head": ['Date accepted','Date delivered','Mail From','Recipient To','Status','Tries','Sender','Tracking ID']}

with open ('./log', 'r') as f:
    list1 = f.readlines()
    for i in list1[::-1]:
        values = i.split("@")
        if values[7] == "D":
            time = values[0].split(":")
            tracking = values[3].split("/")
            messages[values[4]] = []
            messages[values[4]].append("-")
            messages[values[4]].append(datetime.fromtimestamp(int(time[1])).strftime('%m/%d/%Y %H:%M'))
            messages[values[4]].append(values[10] + "@" + values[11])
            messages[values[4]].append(values[8] + "@" + values[9])
            messages[values[4]].append(values[7])
            messages[values[4]].append(values[15])
            messages[values[4]].append(values[1])
            messages[values[4]].append(tracking[0])
        elif values[7] == "R" and values[4] not in messages:
            time = values[0].split(":")
            tracking = values[3].split("/")
            messages[values[4]] = []
            messages[values[4]].append(datetime.fromtimestamp(int(time[1])).strftime('%m/%d/%Y %H:%M'))
            messages[values[4]].append("-")
            messages[values[4]].append(values[10] + "@" + values[11])
            messages[values[4]].append(values[8] + "@" + values[9])
            messages[values[4]].append(values[7])
            messages[values[4]].append("-")
            messages[values[4]].append(values[1])
            messages[values[4]].append(tracking[0])
        elif values[7] == "R" and values[4] in messages:
            time = values[0].split(":")
            messages[values[4]][0] = datetime.fromtimestamp(int(time[1])).strftime('%m/%d/%Y %H:%M')

with open('report.csv','w') as csvfile:
    for list_item in messages.values():
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(list_item)
