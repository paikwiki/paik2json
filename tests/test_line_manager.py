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

    def test_가장_깊은_들여쓰기를_반환할_수_있다(self):
        self.assertEqual(2, self.line_manager.deepest_depth)

    def test_문자열을_하나의_문자열로_합칠_수_있다(self):
        raw = """line
line
line"""
        line_manager = LineManager(raw)
        self.assertEqual(
            "linelineline",
            line_manager.toString(),
        )

    def test_concatable_파라미터를_True_설정하면_들여쓰기가_홀수인_문자열이_있어도_하나의_문자열로_합칠_수_있다(self):
        raw = """line
 line
line"""
        line_manager = LineManager(raw, True)
        self.assertEqual(
            "line lineline",
            line_manager.toString(),
        )

    def test_모든_문자열의_깊이가_같지않으면_에러를_반환한다(self):
        raw = """line
line
line
line
  line
"""
        line_manager = LineManager(raw)
        with self.assertRaises(Exception):
            line_manager.toString()

    def test_문자열을_합칠_때_시작_공백을_깊이만큼_제거한다(self):
        raw1 = """  line
  line
  line"""
        raw2 = """  line
   line
   line"""
        line_manager = LineManager(raw1, True)
        self.assertEqual(
            "linelineline",
            line_manager.toString(),
        )
        line_manager = LineManager(raw2, True)
        self.assertEqual(
            "line line line",
            line_manager.toString(),
        )

    def tearDown(self):
        del self.line_manager
