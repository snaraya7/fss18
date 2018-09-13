
n = [4,10,15,38,54,57,62,83,100,100,174,190,
                215,225,233,250,260,270,299,300,306,
                333,350,375,443,475,525,583,780,1000]

def num(max):
  return
  # {n=0, mu=0, m2=0, sd=0,
  #         lo=10^32, hi=-10^32, _some=sample(max),
  #         w=1}


# -- Bulk add to a `num`:

def nums(t,f,      n):
#   f=f or function(x) return x end
#   n=num()
#   for _,x in pairs(t) do numInc(n, f(x)) end
#   return n
# end
    return

# -- Incremenally, add `x` to a `num`.
# -- This is [Welford's algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm)

def numInc(t,x,    d):
#   if x == "?" then return x end
#   t.n  = t.n + 1
#   sampleInc(t._some, x)
#   d    = x - t.mu
#   t.mu = t.mu + d/t.n
#   t.m2 = t.m2 + d*(x - t.mu)
#   if x > t.hi then t.hi = x end
#   if x < t.lo then t.lo = x end
#   if (t.n>=2) then
#     t.sd = (t.m2/(t.n - 1 + 10^-32))^0.5 end
#   return x
# end
    return

# -- Aside: this can be generalized to
# -- higher order moments; e.g. to calcuate
# -- [skew and kurtosis](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Higher-order_statistics).
# --
# -- ![](https://www.scratchapixel.com/images/upload/monte-carlo-methods/skew.png?)
# --
# -- Note that mean, variance, skew,
# -- kurtosis may not be enough to characterize
# -- real world data sets. e.g
# -- see [these plots](https://raw.githubusercontent.com/txt/fss17/master/img/notnorm8.png) of CPU wait times for disk access time for numerous SQL queries from one program on one system. So whenever I can, I cluster the data and build
# -- different models for different small local regions.
# --
# -- Remove `x` from a `num`. Note: due to
# -- the approximation of this method, this
# -- gets inaccurate for small `x` numbers
# -- and very small sample sizes (small `n`,
# -- say, less than 5)

def numDec(t,x,    d):
  if (x == "?"):
      return x
  if (t.n == 1):
      return x
  t.n  = t.n - 1
  d    = x - t.mu
  t.mu = t.mu - d/t.n
  t.m2 = t.m2 - d*(x- t.mu)
  if (t.n>=2):
      t.sd = (t.m2/(t.n - 1 + 10^-32))^0.5
  return x

# -- Normalization

def numNorm(t,x,     y):
  return x=="?" and 0.5 or (x-t.lo) / (t.hi-t.lo + 10^-32)

# -- Misc

def numXpect(i,j,   n):
  n = i.n + j.n +0.0001
  return i.n/n * i.sd+ j.n/n * j.sd