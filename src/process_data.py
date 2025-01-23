import datetime
import string
from multiprocessing.reduction import duplicate

import numpy
import numpy as np
from src.read_file import read_file





def process_data(input: list) -> list:

    positions = np.array([pos for date, pos in input])
    timestamps = [date for date, pos in input]

    output_positions = get_positions(all_positions=positions)
    output_timestamps = get_timestamps(positions=positions, timestamps=timestamps)


    final_stamp_objects = zip(output_timestamps, output_positions)
    # print(f"final stamps", list(final_stamp_objects))


    return list(final_stamp_objects)



# from the description we can assume that the input contains positions for evey hour
# whether the position changes or not
def get_positions(all_positions: np.ndarray):

    # collapse the same consecutive positions
    out = []

    i = 0
    prev = None
    while i < len(all_positions):

        curr = all_positions[i]

        if prev != curr:
            out.append(curr)

        prev = curr
        i+=1

    # duplicate all positions - with Numpy here, but this might be slower than plain Python in this case
    # the relative performance would need to be checked for larger datasets
    duplicate_positions = np.ravel(np.tile(out, (2, 1)).T)

    return duplicate_positions



def get_timestamps(positions: np.ndarray, timestamps: list[datetime.datetime]):

    out = []

    # get the differences between positions
    position_diffs =  np.abs(np.diff(positions))

    # get the non-zero differences
    nonzero_position_diffs = position_diffs[position_diffs != 0]

    # get the indices of the second timestamp in each pair of consecutive timestamps with different corresponding
    # positions
    diff_indices =  np.nonzero(position_diffs)[0] + 1

    # get the numbers of seconds needed for travel on each side of hour marks
    halves_seconds = np.ceil(60 * nonzero_position_diffs / 2)

    # get the timestamps for start end and of travel time -
    # using a library like datetime reduces the risk of errors in datetime calculations
    # and the need for debugging and testing
    for i in range(len(halves_seconds)):
        out.append(timestamps[diff_indices[i]] - datetime.timedelta(seconds=halves_seconds[i]))
        out.append(timestamps[diff_indices[i]] + datetime.timedelta(seconds=halves_seconds[i]))

    # add the first timestamp
    out.insert(0, timestamps[0])

    # add the last timestamp
    if out[-1] > timestamps[-1]:
        out.append(timestamps[-1] + datetime.timedelta(hours=1))
    else:
        out.append(timestamps[-1])

    return out




