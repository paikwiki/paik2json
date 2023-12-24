import unittest
from paik2json.array import Array
from paik2json.line import Line


class ArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.array = Array(
            [
                Line("line"),
                Line("line"),
                Line("line"),
            ]
        )
        self.padding_contained_array = Array(
            [
                Line("  line"),
                Line("  line"),
                Line("    line  "),
            ]
        )

    def test_각_Line_을_문자열로_출력할_수_있다(self):
        self.assertEqual("['line', 'line', 'line']", str(self.array))

    def test_각_Line_앞뒤의_공백을_제거한_문자열의_리스트를_반환한다(self):
        self.assertEqual(
            "['line', 'line', 'line']",
            str(self.padding_contained_array),
        )
