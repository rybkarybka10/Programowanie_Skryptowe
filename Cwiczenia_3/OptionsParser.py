from MoveDirection import MoveDirection

class OptionsParser:
    @staticmethod
    def parse_options(options):
        parsed_options = []
        for option in options:
            try:
                move_direction = MoveDirection(option)
                parsed_options.append(move_direction)
            except ValueError:
                pass
        return parsed_options
