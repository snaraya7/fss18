from w13 import num
from w13 import sym
from w13 import sample
import re

class table:
    def __init__(self, max = 1000):
        w={}
        syms = sym()
        nums = num(max),
        clazz = None,
        rows = {}
        name = {}
        _use = {}
        indeps = {}


def indep(self,c):
    return not self.w[c] and self.clazz != c

def dep(self,c):
    return not indep(c)

def header(self, cells):
  t = self or table()
  t.indeps = {}
  for c0,x in enumerate(cells):
    if "?" not in x: #match("%?"):
      c = len(t._use)+1
      t._use[c] = c0
      t.name[c] = x
      if re.search("[<>$]", x): #x:match("[<>%$]")
	    t.nums[c] = num(1)
      else :
          t.syms[c] = sym()
      if     "<" in x : #x:match("<") then
         t.w[c]  = -1
      elif ">" in x: #:match(">") then
        t.w[c]  =  1
      elif "!" in x: #:match("!") then
        t.clazz =  c
      else:
          t.indeps[ len(t.indeps) + 1 ] = c
          # end end end
  return t


def row(self,cells):
  r=  len(self.rows)+1
  self.rows[r] = {}
  for c,c0 in enumerate(self._use):
    x = cells[c0]
    if x != "?": #then
      if self.nums[c]: #then
	x = float(x)#tonumber(x)
        self.nums.numInc(self.nums[c], x)
      else:
	self.sym.symInc(self.syms[c], x)
    self.rows[r][c] = x
    # end
  return self
# end


# def rows1(stream, t,f0,f,   first,line,cells):
#   first,line = true,io.read()
#   while line do
#     line= line:gsub("[\t\r ]*","")
#               :gsub("#.*","")
#     cells = split(line)
#     line = io.read()
#     if #cells > 0 then
#       if first then f0(cells,t) else f(t,cells) end end
#       first = false
#   end
#   io.close(stream)
#   return t
# end
#
# function rows(file,t,f0,f,      stream,txt,cells,r,line)
#   return rows1( file and io.input(file) or io.input(),
#                 t  or data(), f0 or header, f or row) end





