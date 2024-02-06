# Kelden Phuntsho Dorji
# Section A
# 02230285

# REFERENCES
# Links that you referred while solving the problem
# https://www.geeksforgeeks.org/
# https://bobbyhadz.com/blog/find-range-overlap-in-python-or-check-if-ranges-overlap

# SOLUTION
# Your Solution Score:
# There were 20000 people assigned and there are 6425 of overlapping space assignments
# There were 2556 assignments that overlap completely.

# Import required libraries
import os

# Function to read the contents of the input file
def read_input(file_name="input_2_cap2.txt"):
    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

# Function to parse a line from the input file into a list of ranges
def parse_line(line):
    return [[int(num) for num in range_.split('-')] for range_ in line.split(', ')]

# Function to count the total number of overlaps between all space assignments
def count_overlaps(spaces):
    total_overlaps = 0
    for i in range(len(spaces)):
        for j in range(i + 1, len(spaces)):
            if max(spaces[i][0], spaces[j][0]) <= min(spaces[i][1], spaces[j][1]):
                total_overlaps += 1
    return total_overlaps

# Function to count the number of complete overlaps where one assignment fully contains another
def count_complete_overlaps(spaces):
    complete_overlaps = 0
    for i in range(len(spaces)):
        for j in range(i + 1, len(spaces)):
            if spaces[i][0] <= spaces[j][0] and spaces[i][1] >= spaces[j][1]:
                complete_overlaps += 1
    return complete_overlaps

# Main function to execute the program
def main():
    # Read the input file and store the lines
    lines = read_input()
    
    # Calculate the total number of people assigned
    total_people = len(lines) * 2
    
    # Count the total number of overlaps across all lines
    total_overlaps = sum(count_overlaps(parse_line(line)) for line in lines)
    
    # Count the number of complete overlaps across all lines
    complete_overlaps = sum(count_complete_overlaps(parse_line(line)) for line in lines)
    
    # Print the results
    print(f"There were {total_people} people assigned and there are {total_overlaps} of overlapping space assignments")
    print(f"There were {complete_overlaps} assignments that overlap completely")

# Execute the main function when the script runs
if __name__ == "__main__":
    main()
