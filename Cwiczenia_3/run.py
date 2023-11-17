import sys
from MoveDirection import MoveDirection
from OptionsParser import OptionsParser

def run(moves, move_descriptions):
    valid_moves = [move_descriptions[move] for move in moves if move in move_descriptions]
    return valid_moves

def display(args, show_index=True):
    for i, arg in enumerate(args):
        if show_index:
            print(f'args[{i}] = {arg}')
        else:
            print(arg)

move_descriptions = {
    MoveDirection.FORWARD: "Zwierzak idzie do przodu",
    MoveDirection.BACKWARD: "Zwierzak idzie do tyłu",
    MoveDirection.LEFT: "Zwierzak skręca w lewo",
    MoveDirection.RIGHT: "Zwierzak skręca w prawo",
}

if __name__ == "__main__":
    moves = OptionsParser.parse_options(sys.argv[1:])
    print("Start")
    descriptions = run(moves, move_descriptions)
    display(descriptions, show_index=False)
    print("Stop")
