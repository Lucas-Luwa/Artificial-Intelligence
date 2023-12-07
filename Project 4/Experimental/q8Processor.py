def count_last_element_instances(file_path):
    element_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            elements = line.strip().split(',')

            last_element = elements[-1]

            element_counts[last_element] = element_counts.get(last_element, 0) + 1

    for element, count in element_counts.items():
        print(f'{element}: {count} occurrences', f'{element}: {round(count*0.2)} occurrences')

file_path = 'evalData.txt'
count_last_element_instances(file_path)
