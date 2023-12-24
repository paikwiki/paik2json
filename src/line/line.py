class Line:
    def __init__(self, str: str) -> None:
        self.str = str
        self.depth = self.__calc_depth(str)
        self.sub_content_type = self.__type(str)


    def __type(self, str: str) -> str:
        if str.endswith(":"):
            return "list"
        else:
            return "string"

    def __calc_depth(self, str: str) -> int:
        left_padding = len(str) - len(str.lstrip())
        if left_padding % 2 != 0:
            raise Exception(f"Uneven number of spaces on left side of line: {left_padding}")

        return left_padding / 2

    def __str__(self) -> str:
        return self.str
