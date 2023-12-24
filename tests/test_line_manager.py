import unittest

from paik2json.line import Line
from paik2json.line import LineManager


raw_data = """line
  line
  line: >
    line
    line
line
  line:
    line
    line
"""


class LineManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.line_manager = LineManager(raw_data)
        self.splited_lines = raw_data.strip().splitlines()
        self.invalid_raw_data = "\n".join([f" {line}" for line in self.splited_lines])

    def test_문자열을_Line_리스트로_저장할_수_있다(self):
        self.assertEqual(
            self.splited_lines,
            [str(line) for line in self.line_manager.lines],
        )

    def test_들여쓰기_규칙이_맞지_않는_라인이_있으면_에러를_반환한다(self):
        with self.assertRaises(Exception):
            LineManager(self.invalid_raw_data)
