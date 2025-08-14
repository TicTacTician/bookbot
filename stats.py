def get_word_count(file_contents):
    word_count = file_contents.split()
    return len(word_count)

def get_char_count(file_contents):
    lowercase_file_contents = list(file_contents.lower())
    char_count = {}
    for char in lowercase_file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_char_count(char_count):
    expanded_char_count = []
    for char in char_count:
        if char.isalpha():
            char_num_pair = {
            "char": char,
            "num": char_count[char]
        }
            expanded_char_count.append(char_num_pair)     
    expanded_char_count.sort(reverse=True, key=sort_on)
    return expanded_char_count
