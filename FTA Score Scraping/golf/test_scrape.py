import csv

with open("scrape_2_table.csv", 'r') as input, open('event_output.csv', 'w', newline='') as output:
    reader = csv.reader(input, delimiter=',')
    writer = csv.writer(output, delimiter=',')

    all = []
    row = next(reader)
    row.insert(0, 'id')
    all.append(row)
    count = 0
    for row in reader:
        count += 1
        row.insert(0, count)
        all.append(row)
    writer.writerows(all)
