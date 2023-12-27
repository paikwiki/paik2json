import unittest

from paik2json.line_manager import LineManager
from paik2json.parser import Parser


raw_메모_예시 = """day-2023-12-27-D0
  일일보고-D1
    한일-D2
      문서 쓰기
      코드 짜기
    할일-D2
      문서 읽기
      코드 실행하기
  토픽1-D1
    할일1-D2
      뭔가 해야함
      할 게 많음
    할일2-D2
    할일3-D2
  토픽2-D1
    할 게 별로 없음-D2
    할일4-D2
"""


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = Parser(LineManager(raw_메모_예시))

    def test_parse_로_테이블을_JSON_으로_변경할_수_있다(self):
        self.assertDictEqual(
            {
                "day-2023-12-27-D0": {
                    "일일보고-D1": {
                        "한일-D2": {"문서 쓰기": {}, "코드 짜기": {}},
                        "할일-D2": {"문서 읽기": {}, "코드 실행하기": {}},
                    },
                    "토픽1-D1": {
                        "할일1-D2": {"뭔가 해야함": {}, "할 게 많음": {}},
                        "할일2-D2": {},
                        "할일3-D2": {},
                    },
                    "토픽2-D1": {"할 게 별로 없음-D2": {}, "할일4-D2": {}},
                }
            },
            self.parser.parse(),
        )
