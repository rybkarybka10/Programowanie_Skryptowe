import unittest

def display(args, show_index=False):
    output = []
    for i, arg in enumerate(args):
        if show_index:
            output.append(f'args[{i}] = {arg}')
        else:
            output.append(arg)
    return output

class TestDisplay(unittest.TestCase):

    def test_display_with_index(self):
        args = ["A", "B", "C"]
        expected_output = [
            "args[0] = A",
            "args[1] = B",
            "args[2] = C"
        ]
        with self.subTest():
            self.assertEqual(display(args, show_index=True), expected_output)

    def test_display_without_index(self):
        args = ["A", "B", "C"]
        expected_output = ["A", "B", "C"]
        with self.subTest():
            self.assertEqual(display(args, show_index=False), expected_output)

if __name__ == '__main__':
    unittest.main()
