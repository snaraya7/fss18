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
from w13 import O

class sym:
  def __init__(self):
    self.counts = []
    self.mode = None
    self.most = 0
    self.n = 0
    self._ent = None

# -- Buld add to a `sym`:

def syms(t,f,s):

  # if f == None:
  #   f = function(x)
  #
  # f=f or function(x) return x end

  s=sym()
  for _,x in enumerate(t):
    symInc(s, f(x))
  return s

# -- Add `x` to a `sym`:

def symInc(t,x,   new,old):
  if x=="?":
    return x

  t._ent= None
  t.n = t.n + 1
  old = t.counts[x]
  new = old and old + 1 or 1
  t.counts[x] = new
  if new > t.most:
    t.most = new
    t.mode = x
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

def symEnt(t,  p):
  if t._ent == False:
    t._ent=0
    for x,n in enumerate(t.counts): #do
      p      = n/t.n
      t._ent = t._ent - p * math.log(p,2) #end end
  return t._ent

@O.k
def test():
  assert symEnt(sym().syms(["t","f"])) == 0.5
