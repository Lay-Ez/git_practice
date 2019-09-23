import csv

with open('books_long.csv') as titles:
    title_reader = csv.reader(titles)

    with open('titles_lower.csv', 'w') as new_csv:
        csv_writer = csv.writer(new_csv, delimiter='>')
        for line in title_reader:
            csv_writer.writerow(line)
