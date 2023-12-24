from .line import Line


class LineManager:
    def __init__(self, raw_data: str):
        self.lines = [Line(line) for line in raw_data.strip().splitlines()]
