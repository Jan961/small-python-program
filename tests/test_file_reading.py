import os
import unittest

from src.read_file import read_file

dirname = os.path.dirname(__file__)

# not written yet
class TestFileReading(unittest.TestCase):



    def test_normal_file_read(self):
        file = read_file(os.path.join(dirname, './test_data/input_example.csv'))

        self.assertEqual(True, False)  # add assertion here

    def test_normal_file_read(self):
        file = read_file(os.path.join(dirname, './test_data/input_example.csv'))



        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
