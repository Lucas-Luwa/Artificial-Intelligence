import random

def select_and_append_lines(file_path, output_file_path, num_lines_to_select):
    # Read all lines from the input file
    with open(file_path, 'r') as file:
        all_lines = file.readlines()

    # Ensure the number of lines to select is not greater than the total number of lines
    num_lines_to_select = min(num_lines_to_select, len(all_lines))

    # Randomly select lines without replacement
    selected_lines = random.sample(all_lines, num_lines_to_select)

    # Append the selected lines to the output file
    with open(output_file_path, 'a') as output_file:
        for line in selected_lines:
            output_file.write(line)

# Example usage
input_file_path = 'evalDataDummy.txt'  # Replace with the path to your input file
output_file_path = 'output2.txt'  # Replace with the path to your output file
num_lines_to_select = 10
select_and_append_lines(input_file_path, output_file_path, num_lines_to_select)

