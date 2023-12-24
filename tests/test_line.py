import unittest

from paik2json.line import Line


class LineTestCase(unittest.TestCase):
    def setUp(self):
        self.line = Line("Hello, World!")
        self.list_starting_line = Line("Hello, World:")
        self.strings_starting_line = Line("Hello, World: >")
        self.depthed_strs = [" " * (i * 2) + "Hello, World!" for i in range(0, 10)]

    def test_문자열을_저장할_수_있다(self):
        self.assertEqual("Hello, World!", str(self.line))

    def test_들여쓰기로_깊이를_확인할_수_있다(self):
        for index, str in enumerate(self.depthed_strs):
            line = Line(str)
            self.assertEqual(index, line.depth)

    def test_홀수인_들여쓰기가_있으면_에러를_반환한다(self):
        with self.assertRaises(Exception):
            Line(" " + "Hello, World!")

    def test_일반_문자열의_다음_깊이의_아이템은_문자열_타입이_된다(self):
        self.assertEqual("string", self.line.sub_content_type)

    def test_문자열이_콜론으로_끝나면_다음_깊이의_문자열들은_list_가_된다(self):
        self.assertEqual("list", self.list_starting_line.sub_content_type)

    def test_문자열이_콜론_공백_Greater_Than_으로_끝나면_다음_깊이의_문자열들은_하나의_문자열이_된다(self):
        self.assertEqual("concatables", self.strings_starting_line.sub_content_type)

    def tearDown(self):
        del self.line


if __name__ == "__main__":
    unittest.main()
