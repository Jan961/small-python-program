import csv
import os
import unittest

from src.process_data import process_data
from src.read_file import read_file
from src.write_to_file import write_to_file




# first path in a tuple points to example input and second to example output
# this could be refactored to dynamically construct paths
test_file_paths = [
    (r".\test_data\basic\input\diffs_middle.csv", r".\test_data\basic\output\diffs_middle_out.csv"),
    (r"./test_data/basic/input/even.csv", r"./test_data/basic/output/even_out.csv"),
    (r"./test_data/basic/input/input_example.csv", r"./test_data/basic/output/output_example.csv"),
    (r"./test_data/basic/input/odd.csv", r"./test_data/basic/output/odd_out.csv"),

    (r"./test_data/edge_cases/input/all_same_position.csv", r"./test_data/edge_cases/output/all_same_position_out.csv"),
]

# path to a temporary file used for created and deleted during each test
temp_test_file_path = r".\test_data\temp\temp_output.csv"




class TestDataProcessing(unittest.TestCase):

    def test_the_whole_process(self):

        for paths in test_file_paths:

            print(f"Testing {paths[0]}")

            data = read_file(paths[0])
            processed = process_data(data)
            write_to_file(data=processed,
                          file_path=temp_test_file_path)

            created_output = []
            with open(temp_test_file_path, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    if not all(cell.strip() == '' for cell in row):
                        created_output.append((row[0], int(row[1])))

            if os.path.exists(temp_test_file_path):
                os.remove(temp_test_file_path)

            expected_output = []
            with open(paths[1], newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    if not all(cell.strip() == '' for cell in row):
                        expected_output.append((row[0], int(row[1])))


            for i in range(len(created_output)):
                self.assertEqual(created_output[i], expected_output[i])

            print("Test passed")







if __name__ == '__main__':
    unittest.main()
