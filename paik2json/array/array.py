from paik2json.line import Line


class Array(list):
    def __init__(self, lines: list[Line]):
        super().__init__()
        [self.append(str(line).strip()) for line in lines]
