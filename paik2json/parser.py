import copy
from paik2json.line_manager import LineManager


class Parser:
    def __init__(self, line_manager: LineManager):
        self.line_manager = line_manager
        self.table = self.__to_table()

    def __to_table(self):
        table = [[None] * (self.line_manager.deepest_depth + 1)]
        for index, line in enumerate(self.line_manager.lines):
            right_empties_count = self.line_manager.deepest_depth - line.depth
            table[index][line.depth] = line.strip_depth()
            table[index] = table[index][: line.depth + 1] + (
                [None] * right_empties_count
            )
            if index < len(self.line_manager.lines) - 1:
                table.append(copy.deepcopy(table[index]))
        return table

    def parse(self):
        json = {}
        for i in range(self.line_manager.deepest_depth + 1):
            for r in self.table:
                if r[i] is None:
                    continue

                if i == 0:
                    upper = json
                elif i == 1:
                    upper = json[r[0]]
                elif i == 2:
                    upper = json[r[0]][r[1]]
                elif i == 3:
                    upper = json[r[0]][r[1]][r[2]]
                elif i == 4:
                    upper = json[r[0]][r[1]][r[2]][r[3]]
                elif i == 5:
                    upper = json[r[0]][r[1]][r[2]][r[3]][r[4]]
                elif i > 5:
                    raise NotImplementedError()

                upper[r[i]] = {}

        return json
