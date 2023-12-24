import unittest

from paik2json.line_manager import LineManager


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

raw_모든_깊이_0 = "line\nline\nline"
raw_모든_깊이_2 = "  line\n  line\n  line"


class LineManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.line_manager = LineManager(raw_data)
        self.line_manager_모든_깊이_0 = LineManager(raw_모든_깊이_0)
        self.line_manager_모든_깊이_2 = LineManager(raw_모든_깊이_2)
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

    def test_toString_으로_문자열을_하나의_문자열로_합칠_수_있다(self):
        self.assertEqual(
            "linelineline",
            self.line_manager_모든_깊이_0.toString(),
        )
        self.assertEqual(
            "linelineline",
            self.line_manager_모든_깊이_2.toString(),
        )
        raw = "  line\n   line\n   line"
        line_manager = LineManager(raw, True)
        self.assertEqual(
            "line line line",
            line_manager.toString(),
        )
        del line_manager

    def test_concatable_파라미터를_True_설정하면_들여쓰기가_홀수인_문자열이_있어도_하나의_문자열로_합칠_수_있다(self):
        raw = "line\n line\nline"
        line_manager = LineManager(raw, True)
        self.assertEqual(
            "line lineline",
            line_manager.toString(),
        )
        del line_manager

    def test_toString_실행시_모든_문자열의_깊이가_같지_않으면_에러를_반환한다(self):
        raw = "line\nline\nline\nline\n  line"
        with self.assertRaises(Exception):
            LineManager(raw).toString()

    def test_toList_로_문자열을_리스트로_바꿀_수_있다(self):
        self.assertEqual(
            "['line', 'line', 'line']",
            str(self.line_manager_모든_깊이_0.toList()),
        )
        self.assertEqual(
            "['line', 'line', 'line']",
            str(self.line_manager_모든_깊이_2.toList()),
        )

    def test_toList_실행시_모든_문자열의_깊이가_같지_않으면_에러를_반환한다(self):
        raw = "line\n  line\nline"
        with self.assertRaises(Exception):
            LineManager(raw).toList()

    def tearDown(self):
        del self.line_manager
        del self.line_manager_모든_깊이_0
        del self.line_manager_모든_깊이_2
