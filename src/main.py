from src.process_data import process_data
from src.read_file import read_file
from src.write_to_file import write_to_file


# assumptions used here though not explicitly stated in the task description:
# - the number of timestamps is greater than 2
# - the distance travelled by the chandelier between two positions always less than 60 m
#  the gallery is not monstrously tall

data = read_file(r"./../tests/test_data/basic/input/input_example.csv")

processed = process_data(data)
print(f" processed {processed}")

# write_to_file(data=processed, file_path=r".\output.csv")