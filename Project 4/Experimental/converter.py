def convert_line(line):
    items = line.strip().split(',')
    first_item = items.pop(0)
    items.append(first_item)
    items[-1] = str(ord(items[-1]) - ord('A'))
    return ','.join(items)

def convert_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            converted_line = convert_line(line)
            outfile.write(converted_line + '\n')

input_file = 'lrd.txt' 
output_file = 'output3.txt' 
convert_file(input_file, output_file)
