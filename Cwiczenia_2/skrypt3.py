import argparse
import operations
import cut
import grep
import skrypt1

def main():
    parser = argparse.ArgumentParser(prog='skrypt3', description='Combine GREP and CUT in Python')
    parser.add_argument('action', help='Choose cut or grep "word" option', type=str)
    parser.add_argument('-d', '--delimiter', required=False, help='Specify delimiter instead of TAB, used with cut')
    parser.add_argument('-f', '--fields', required=False, help='Select only these fields, used with cut', nargs='+')
    parser.add_argument('-i', '--ignore', required=False, help='Ignore case distinctions in patterns and input data, used with grep', action='store_true')
    parser.add_argument('-w', '--word', required=False, help='Select only those lines containing matches that form whole words, used with grep', action='store_true')
    args = parser.parse_args()

    if args.action == 'cut':
        if args.ignore or args.word or len(args.fields) == 0:
            print("Bad optional argument, see help")
            exit()

        text = input("Enter text: ")
        result = cut.cut(text, args.delimiter, args.fields)
        print(result)

    elif args.action == 'grep':
        if args.delimiter or args.fields:
            print("Bad optional argument, see help")
            exit()

        text = input("Enter text: ")
        result = grep.grep(text, args.ignore, args.word)
        print(result)
        
    elif args.action == 'skrypt1.py':
        skrypt1.printAll(args.function[1])
    else:
        print("Syntax: ./skrypt3.py {grep, cut} [optional arguments, see help]")
