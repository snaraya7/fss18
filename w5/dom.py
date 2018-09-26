#Porting... WIP

def dom(self,row1,row2):
  s1,s2,n = 0,0, 0
  for _ in enumerate(t.w):
      n=n+1
  for c,w in enumerate(t.w):
    a0  = row1[c]
    b0  = row2[c]
    a   = numNorm( t.nums[c], a0)
    b   = numNorm( t.nums[c], b0)
    s1 = s1 - 10^(w * (a-b)/n)
    s2 = s2 - 10^(w * (b-a)/n)
  return s1/n < s2/n

def doms(self):
  n= Lean.dom.samples
  c= len(self.name) + 1
  # port this > print(cat(t.name,",") .. ",>dom")
  for r1=1,len(self.rows):
    row1 = self.rows[r1]
    row1[c] = 0
    for s=1,n do
     row2 = another(r1,self.rows)
     s = dom(self,row1,row2) and 1/n or 0
     row1[c] = row1[c] + s
  dump(t.rows)
#
# def mainDom():
#     doms(rows())
#
# return {main = mainDom}
