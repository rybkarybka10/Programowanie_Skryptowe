import pytest

def display(args, show_index=True):
    for i, arg in enumerate(args):
        if show_index:
            print(f'args[{i}] = {arg}')
        else:
            print(arg)

def run(moves, move_descriptions):
    descriptions = [move_descriptions.get(move) for move in moves if move in move_descriptions]
    return descriptions

def test_run(): #test powinien byc zdany
    moves = ["f", "b", "r", "l"]
    move_descriptions = {
        "f": "Zwierzak idzie do przodu",
        "b": "Zwierzak idzie do tyłu",
        "l": "Zwierzak skręca w lewo",
        "r": "Zwierzak skręca w prawo",
    }
    expected_output = [
        "Zwierzak idzie do przodu",
        "Zwierzak idzie do tyłu",
        "Zwierzak skręca w prawo",
        "Zwierzak skręca w lewo",
    ]
    assert run(moves, move_descriptions) == expected_output

def test_step(): #test powinien byc bledny
    moves = ["f"]
    move_descriptions = {"f": "Zwierzak idzie do przodu"}
    expected_output = ["Zwierzak idzie do tyłu"]
    assert run(moves, move_descriptions) == expected_output

    