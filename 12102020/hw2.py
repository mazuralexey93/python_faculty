with open('hw2.txt', 'r', encoding='utf-8') as my_file_hw2:
    line_counter = 0
    word_counter = 0
    for line in my_file_hw2.readlines():
        line_counter += 1
        words = line.split()
        word_counter += len(words)
        print(f'Line №{line_counter} contains {len(words)} words')

    print(f'file contains {line_counter} lines, {word_counter} words')
