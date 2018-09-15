# --vim: ts=2 sw=2 sts=2 expandtab:cindent:formatoptions+=cro
# --------- --------- --------- --------- --------- ---------
#
# require "sample"
#
# -- ## Example
#
# --
# --      n = nums{ 4,10,15,38,54,57,62,83,100,100,174,190,
# --                215,225,233,250,260,270,299,300,306,
# --                333,350,375,443,475,525,583,780,1000}
# --      print(n.mu, n.sd) ==> 270.3, 231.946
# --
#
# -- Inside a `num`:

from w13.sample import sample
from w13.TestEngine import O
import math, random

class num:

    def __init__(self,max):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = math.pow(10,32)
        self.hi = -math.pow(10,32)
        self._some = sample(max)
        self.w = 1

#     def  num(max):
#   return {n=0, mu=0, m2=0, sd=0,
#           lo=10^32, hi=-10^32, _some=sample(max),
#           w=1}
# end

# -- Bulk add to a `num`:

    def  nums(self,f):
        if f is None:
            f = lambda x: x
        n=num()
        for item in self._some:
            self._some.numInc(n, f(item))

        return n
# end

# -- Incremenally,? add `x` to a `num`.
# -- This is [Welford's algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm)

    def  numInc(self,x):
        if x == "?":
            return x

        self.n  = self.n + 1

        self.sampleInc(self._some, x)
        d    = x - self.mu
        self.mu = self.mu + d/self.n
        self.m2 = self.m2 + d*(x - self.mu)

        if x > self.hi:
            self.hi = x #end
        if x < self.lo:
            self.lo = x #end
        if (self.n>=2):
            self.sd = math.pow((self.m2/(self.n - 1 + math.pow(10,-32))),0.5) #end
        return x
# end
#
# -- Aside: this can be generalized to
# -- higher order moments; e.g. to calcuate
# -- [skew and kurtosis](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Higher-order_statistics).
# --
# -- ![](https://www.scratchapixel.com/images/upload/monte-carlo-methods/skew.png?)
# --
# -- Note that mean, variance, skew,
# -- kurtosis may not be enough to characterize
# -- real world data sedts. e.g
# -- see [these plots](https://raw.githubusercontent.com/txt/fss17/master/img/notnorm8.png) of CPU wait times for disk access time for numerous SQL queries from one program on one system. So whenever I can, I cluster the data and build
# -- different models for different small local regions.
# --
# -- Remove `x` from a `num`. Note: due to
# -- the approximation of this method, this
# -- gets inaccurate for small `x` numbers
# -- and very small sample sizes (small `n`,
# -- say, less than 5)

    def  numDec(self,x):
        if (x == "?"):
            return x
        if (self.n == 1):
            return x
        self.n  = self.n - 1
        d    = x - self.mu
        self.mu = self.mu - d/self.n
        self.m2 = self.m2 - d*(x- self.mu)

        if (self.n>=2):
            self.sd = (self.m2/(self.n - 1 + 10^-32))^0.5
        return x
# end

# -- Normalization

    def  numNorm(self,x):
        return x=="?" and 0.5 or (x-self.lo) / (self.hi-self.lo + math.pow(10, -32))
# end

# -- Misc

    def  numXpect(self,j):
        n = self.n + j.n + 0.0001
        return self.n/n * self.sd+ j.n/n * j.sd
# end

@O.k
def test():

    n = num([4, 10, 15, 38, 54, 57, 62, 83, 100, 100, 174, 190, 215, 225,
     233, 250, 260, 270, 299, 300, 306, 333, 350, 375, 443, 475,
     525, 583, 780, 1000])
    assert (abs(n.mu), abs(270.3))
    assert (abs(n.sd), abs(231.946))
    print(n.mu, n.sd)



