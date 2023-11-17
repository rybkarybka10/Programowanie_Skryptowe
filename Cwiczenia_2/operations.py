
def first_character(string):
    return string[0] if string else ""

def first_two_characters(string):
    return string[:2] if len(string) >= 2 else ""

def all_characters_except_first_two(string):
    return string[2:]

def penultimate_character(string):
    return string[-2] if len(string) >= 2 else ""

def last_three_characters(string):
    return string[-3:] if len(string) >= 2 else ""

def all_characters_in_even_positions(string):
    return string[::2]

def merge_characters_and_duplicate(string):
    first = first_character(string)
    penultimate = penultimate_character(string)
    result = (first + penultimate) * len(string)
    return result
