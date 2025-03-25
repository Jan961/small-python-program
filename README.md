Short Programming Task - specification

Suppose you are writing software for an art installation which involves a chandelier which can be moved up and down by a motor. The input to your program will be a CSV file called schedule.csv with hourly timestamps (in 'YYYY-MM-DDTHH:MM:SSZ' format) and an integer value representing the desired height of the chandelier for a period of one hour starting at that timestamp. For example:

2025-01-01T01:00:00Z, 10

2025-01-01T02:00:00Z, 15

2025-01-01T03:00:00Z, 15

2025-01-01T04:00:00Z, 13

...

2025-01-04T05:00:00Z, 5

2025-01-04T06:00:00Z, 3



The motor can either be stationary or it can move at a constant speed of 1 metre per minute. It will change between the hourly steps symmetrically about the hour boundary, i.e. half of its movement will be before the hour boundary and half will be afterward.



Your software needs to write a file called output.csv which contains the minimal sequence of points that, when linearly interpolated, describe the actual height of the chandelier over time after accounting for the movement of the motor.



For the example above, the output.csv should be:

2025-01-01T01:00:00Z, 10

2025-01-01T01:57:30Z, 10

2025-01-01T02:02:30Z, 15

2025-01-01T03:59:00Z, 15

2025-01-01T04:01:00Z, 13

...

2025-01-04T05:59:00Z, 5

2025-01-04T06:01:00Z, 3

2025-01-04T07:00:00Z, 3



Please provide your solution, with unit tests, using one of the following languages.



- Python + Pytest + requirements.txt or pyproject.toml
