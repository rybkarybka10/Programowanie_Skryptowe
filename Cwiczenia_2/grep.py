import re

def grep(input_text, pattern, ignore_case=False, whole_word=False):
    flags = 0
    if ignore_case:
        flags |= re.IGNORECASE
    lines = input_text.split('\n')
    result = []

    for line in lines:
        if whole_word:
            pattern = r'\b' + re.escape(pattern) + r'\b'
        if re.search(pattern, line, flags):
            result.append(line)

    return '\n'.join(result)
