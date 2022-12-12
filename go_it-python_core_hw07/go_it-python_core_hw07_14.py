def to_indexed(source_file, output_file):
    data = []
    with open(source_file, 'r') as file_r:
        for i, line in enumerate(file_r.readlines()):
            data.append(f'{i}: {line}')
    with open(output_file, 'w') as file_w:
        for line in data:
            file_w.write(line)

# to_indexed('14_test.txt', '14_test_2.txt')