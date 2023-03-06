import csv, datetime
with open('data/cnnarticles.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([ 'date', #str(datetime.datetime.now()),
                     'title',
                     'text'])
