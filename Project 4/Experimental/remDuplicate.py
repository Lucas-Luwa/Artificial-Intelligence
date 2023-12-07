def remove_duplicates(input_file, reference_file, output_file):
    with open(reference_file, 'r') as ref_file:
        reference_lines = ref_file.readlines()

    with open(input_file, 'r') as in_file:
        with open(output_file, 'w') as out_file:
            for line in in_file:
                if line in reference_lines:
                    reference_lines.remove(line)
                else:
                    out_file.write(line)

# Replace these file names with your actual file names
input_file = 'evalDataPrelim.txt'
reference_file = 'evalTest.txt'
output_file = 'evalTrain.txt'

remove_duplicates(input_file, reference_file, output_file)
