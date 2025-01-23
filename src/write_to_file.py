import string
import csv

def write_to_file(file_path:string, data:list):
    try:

        with open(file_path, 'w') as file:
            writer = csv.writer(file)


            for element in data:
                timestamp = element[0].strftime('%Y-%m-%dT%H:%M:%SZ')
                position = element[1]
                writer.writerow([timestamp,position])
        return True

    except:
        raise Exception("Error writing to file")

