from __future__ import annotations

import math


class CFloat:

    def __init__(self, value: float):
        self.val = value

    def __lt__(self, other: CFloat):
        if other == None: return False
        return self.val < other.val and not math.isclose(self.val, other.val)

    def __gt__(self, other: CFloat):
        if other == None: return False
        return self.val > other.val and not math.isclose(self.val, other.val)

    def __le__(self, other: CFloat):
        if other == None: return False
        return self.val <= other.val or math.isclose(self.val, other.val)

    def __ge__(self, other: CFloat):
        if other == None: return False
        return self.val >= other.val or math.isclose(self.val, other.val)

    def __eq__(self, other: CFloat):
        if other == None: return False
        return math.isclose(self.val, other.val)

    def __sub__(self,other: CFloat):
        return CFloat(self.val - other.val)

    def __rsub__(self,other: CFloat):
        return CFloat(other.val - self.val)