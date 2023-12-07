import random

def split_data(input_file, train_file, test_file, test_percentage=0.2):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    test_size = int(total_lines * test_percentage)

    # Randomly select lines for testing
    test_lines = random.sample(lines, test_size)

    # Remaining lines are for training
    train_lines = [line for line in lines if line not in test_lines]

    # Write training data to the train_file
    with open(train_file, 'w') as train_file:
        train_file.writelines(train_lines)

    # Write testing data to the test_file
    with open(test_file, 'w') as test_file:
        test_file.writelines(test_lines)

# Example usage
split_data('letterRecog.txt', 'letterRecogTrain2.txt', 'letterRecogTest2.txt')
