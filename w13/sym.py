# --vim: ts=2 sw=2 sts=2 expandtab:cindent:formatoptions+=cro
# --------- --------- --------- --------- --------- ---------
#
# -- ## Example
#
# --
#s = syms{ 'y','y','y','y','y','y','y','y','y',
# --              'n','n','n','n','n'}
# --      print(symEnt(s)) ==> 0.9402
# --

# -- Inside a `sym`:

import math
from w13.TestEngine import O

class sym:

    def __init__(self):
        self.counts = {}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None

# -- Build add to a `sym`:


    def syms(self,items, f):

        if f is None:
            f = lambda x : x

        s=sym()

        for item in items:
            self.symInc(f(item))
        return s



# -- Add `x` to a `sym`:

    def symInc(self,x):
        if x == "?":
            return x

        self._ent= None
        self.n = self.n + 1

        old = self.counts.get(x, 0)
        new = old and old + 1 or 1

        self.counts[x] = new

        if new > self.most:
            self.most = new
            self.mode = x

        return x

# -- Remove `x` from a `sym`.

    def symDec(t,x):
        t._ent= None
        if t.n > 0:
            t.n = t.n - 1
            t.counts[x] = t.counts[x] - 1
        return x

# -- Computing the entropy: don't recompute if you've
# -- already done it before.

    def symEnt(self):
        if self._ent == None:
            self._ent=0

        for key, value in self.counts.items():
            p      = value/self.n
            self._ent = self._ent - p * math.log(p,2)
        return self._ent

@O.k
def test():
    s = sym()

    syms = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y',
            'n', 'n', 'n', 'n', 'n']
    s.syms(syms, None)
    result = s.symEnt()
    print("input ", syms)
    print("entropy ", result)
    assert result == 0.9402859586706309