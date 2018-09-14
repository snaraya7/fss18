# -- vim: ts=2 sw=2 sts=2 expandtab:cindent:formatoptions+=cro
# --------- --------- --------- --------- --------- ---------


# -- ## Inside a `sample`
# --
# -- Samples keep up to `max` items in a list
# -- called `some`.
# --

import random,math
from w13.TestEngine import O

class sample:

    def __init__(self, max = 1000, txt = ""):
            self.max = max
            self.rank = 1
            self.txt = txt
            self.n = 0
            self.sorted = False
            self.some = []

    def sampleInc(self,x):
        now = len(self.some)
        self.n = self.n + 1
        if now < self.max :
            self.sorted = False
            # self.some[ len(self.some) + 1 ] = x
            self.some.append(x)
        elif random.random() < now/self.n:
            self.sorted = False
            self.some[ math.floor(0.5+ random.random()* now) ] = x
        return x

# -- Never resort if we are already sorted.

    def sampleSorted(self):
        if  self.sorted == False:
            self.sorted=True
            self.some.sort()

        return self.some

# -- But once they are sorted, we can access the `nth`
# -- percentile item.

    def nths(self, ns):

        ns = ns or {0.1,0.3,0.5,0.7,0.9}
        out = []
        for value in ns:
            out[ len(out) + 1 ] = self.nth(value)

        return out


    def nth(self,n):

        data = self.sampleSorted()

        x = min(len(data), max(1, math.floor(0.5 + len(data)*n)))
        y = len(data)
        return data[ min(len(data), max(1, math.floor(0.5 + len(data)*n))) ]

    def sampleLt(s1,s2):
            return (s1.nth(0.5) < s2.nth(0.5))


@O.k
def test():
    random.seed(1)
    samp = sample()
    s = {}

    for i in range (5,10):
        s[i] = math.pow(2,i)

    for i in range (1,10):
        y = random.random()
        for key, value in s.items():
            samp.sampleInc(y)

    for key, value in s.items():
        print ( samp.nth(0.5) - 0.5 )
        assert abs(samp.nth(0.5) - 0.5) < 0.2

