import sys

def run(moves, move_descriptions):
    descriptions = [move_descriptions.get(move) for move in moves if move in move_descriptions]
    return descriptions


def display(args, show_index=True):
    for i, arg in enumerate(args):
        if show_index:
            print(f'args[{i}] = {arg}')
        else:
            print(arg)

move_descriptions = {
        "f": "Zwierzak idzie do przodu",
        "b": "Zwierzak idzie do tyłu",
        "l": "Zwierzak skręca w lewo",
        "r": "Zwierzak skręca w prawo",
    }

if __name__ == "__main__":

    moves = sys.argv[1:]
    print("Start")
    descriptions = run(moves, move_descriptions)
    display(descriptions, show_index=False)
    print("Stop")
