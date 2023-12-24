import unittest

from src.line.line import Line


class LineTestCase(unittest.TestCase):
    def setUp(self):
        self.line = Line("Hello, World!")

    def test_문자열을_저장할_수_있다(self):
        self.assertEqual("Hello, World!", str(self.line))

    def test_들여쓰기로_깊이를_확인할_수_있다(self):
        for i in range(0, 10):
            left_padding = " " * (i * 2)
            line = Line(left_padding + "Hello, World!")
            self.assertEqual(i, line.depth)

    def test_홀수인_들여쓰기가_있으면_에러를_반환한다(self):
        with self.assertRaises(Exception):
            Line(" " + "Hello, World!")

    def tearDown(self):
        del self.line


if __name__ == "__main__":
    unittest.main()
