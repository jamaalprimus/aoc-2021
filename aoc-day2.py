#!/usr/bin/env python3
def file_read(fname, value):
    with open(fname) as f:
        for line in f:
            value.append(line.strip())

commands = []

file_read('inputs/commands', commands)

hor_pos = submarine_depth = aim = 0

for command in commands:
    operation = command.split(" ")

    if operation[0] == "forward":
        hor_pos += int(operation[1])
        submarine_depth += aim*int(operation[1])

    if operation[0] == "down":
        aim += int(operation[1])

    if operation[0] == "up":
        aim -= int(operation[1])

print("Horizontal Pos:", hor_pos)
print("Depth:", submarine_depth)
print("Horizontal * Depth: ", int(hor_pos)*int(submarine_depth))
