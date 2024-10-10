class CustomList(list):
    def __add__(self, other):
        if isinstance(other, CustomList):
            max_len = max(len(self), len(other))
            extended_self = list(self) + [0] * (max_len - len(self))
            extended_other = list(other) + [0] * (max_len - len(other))
            return CustomList(a + b for a, b in
                              zip(extended_self, extended_other))
        if isinstance(other, list):
            return CustomList(list(self) + list(other))
        if isinstance(other, int):
            return CustomList(x + other for x in self)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, CustomList):
            max_len = max(len(self), len(other))
            extended_self = self + [0] * (max_len - len(self))
            extended_other = other + [0] * (max_len - len(other))
            return CustomList(a - b for a, b in
                              zip(extended_self, extended_other))
        if isinstance(other, list):
            max_len = max(len(self), len(other))
            extended_self = self + [0] * (max_len - len(self))
            extended_other = other + [0] * (max_len - len(other))
            return CustomList(a - b for a, b in
                              zip(extended_self, extended_other))
        if isinstance(other, int):
            return CustomList(x - other for x in self)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return CustomList(other - x for x in self)
        if isinstance(other, list):
            return CustomList(other) - self
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, CustomList):
            return sum(self) == sum(other)
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) < sum(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, CustomList):
            return sum(self) <= sum(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) > sum(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, CustomList):
            return sum(self) >= sum(other)
        return NotImplemented

    def __str__(self):
        return f"{list(self)} (sum: {sum(self)})"
