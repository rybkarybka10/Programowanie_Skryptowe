import sys

def display(args, show_index=False):
    for i, arg in enumerate(args):
        if show_index:
            print(f'args[{i}] = {arg}')
        else:
            print(arg)

if __name__ == "__main__":
    args = sys.argv
    print("System wystartował.")
    display(args)
    print("System zakończył działanie.")