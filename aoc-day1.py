#!/usr/bin/env python3


# Day 1
def file_read(fname, value):
    with open(fname) as f:
        for line in f:
            value.append(line.strip())

depths = []
file_read('inputs/depths', depths)

# Part 1
increased_measurements = 0

for index, measurement in enumerate(depths):
    if index in range(1, len(depths)):
        if int(depths[index]) > int(depths[index-1]):
            increased_measurements = increased_measurements + 1

print("Increased Measurements: " + str(increased_measurements))

# Part 2
increased_measurements = 0
depth_groups = []

for index, measurement in enumerate(depths):
    if index not in range(len(depths)-3, len(depths)):
        number = int(depths[index]) + int(depths[index + 1]) + int(depths[index + 2])
        depth_groups.append(number)
    elif index in range(len(depths)-3, len(depths)):
        number = int(depths[index]) + int(depths[index + 1]) + int(depths[index + 2])
        depth_groups.append(number)
        break

for index, measurement in enumerate(depth_groups):
    if index != 0 and index <= len(depth_groups):
        if int(depth_groups[index]) > int(depth_groups[index-1]):
            increased_measurements = increased_measurements + 1

print("Increased Sliding Measurements: " + str(increased_measurements))