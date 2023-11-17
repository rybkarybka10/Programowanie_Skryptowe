import sys
import operations

if len(sys.argv) < 2:
    print("Usage: skrypt1.py <text>")
    sys.exit(1)

text = sys.argv[1]

print(operations.first_character(text))
print(operations.first_two_characters(text))
print(operations.all_characters_except_first_two(text))
print(operations.penultimate_character(text))
print(operations.last_three_characters(text))
print(operations.all_characters_in_even_positions(text))
print(operations.merge_characters_and_duplicate(text))
