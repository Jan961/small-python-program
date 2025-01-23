import csv
import string
from datetime import datetime


def read_file(path:string) -> list:

    out = []

    try:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            prev_date = None

            for row in reader:
                if not all(cell.strip() == '' for cell in row):

                    curr_date = datetime.strptime(row[0],'%Y-%m-%dT%H:%M:%SZ')

                    # if date-times are not ascending print a waring
                    if prev_date and (curr_date < prev_date):
                        raise Exception("Datestamps not in ascending order")

                    # append tuples of Dates and positions
                    out.append((curr_date, int(row[1])))
                    prev_date = curr_date

        return out

    except:
        raise Exception("Error reading file")


