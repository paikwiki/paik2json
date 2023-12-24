from .line import Line


class LineManager:
    def __init__(self, raw_data: str):
        self.lines = [Line(line) for line in raw_data.splitlines()]
        self.deepest_depth = max([line.depth for line in self.lines])

    def concatLines(self) -> str:
        for line in self.lines:
            if line.depth != self.deepest_depth:
                raise Exception(
                    f"lines have different depths. current depth: {line.depth} / deepest depth: {self.deepest_depth}"
                )
        return "".join([str(line)[line.depth * 2:] for line in self.lines])
