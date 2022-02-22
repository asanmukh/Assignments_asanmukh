from itertools import combinations
from collections import Counter


class StringClass:

    def __init__(self, string):
        self.string = string

    def length(self):
        return len(self.string)

    def split(self):
        stringtocharacters = list(self.string)

        return stringtocharacters


class PairsPossible(StringClass):

    def pairs(self):
        res = list(combinations(self.string, 2))
        return res

    def printpairs(self):
        res = list(combinations(self.string, 2))
        print(*res)


class SearchCommonElemts:
    def __init__(self, StringClass, PairsPossible):
        self.str1 = StringClass.string
        self.str2 = PairsPossible.string

    @property
    def common(self):
        dict1 = Counter(self.str1)
        dict2 = Counter(self.str2)

        commonDict = dict1 & dict2

        if len(commonDict) == 0:
            print(-1)
            return
        commonchars = list(commonDict.elemets())
        return commonchars

p = PairsPossible("12314532")
print(p.length())
print(p.split())
p.printpairs()
p.pairs()
a = StringClass("987654912")
h = SearchCommonElemts(p, a)
print(h.common)
