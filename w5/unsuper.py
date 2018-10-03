import operator

from texttable import Texttable

from w13.num import num
import math


from w4 import table
from w5 import Configuration
from w5.dom import dump


def unsuper(data):
  """
    Discretizing columns
    :param data:
    :return:
    """

  rows = []

  for key, value in data.rows.items():
      rows.append(value)

  enough = math.pow(len(rows) , Configuration.unsuper_enough)

  def band(c,lo,hi):
    if lo == 0 :
      return ".." + str(rows[hi][c])
    elif hi == most:
      return str(rows[lo][c]) + ".."
    else:
      return str(rows[lo][c]) + ".." + str(rows[hi][c])


  def argmin(c,lo,hi):
    """
      Check the cut
      :param c:
      :param lo:
      :param hi:
      :return:
      """

    cut = None
    if (hi - lo > 2*enough):
      l,r = num(), num()
      for i in range (lo,hi):
          r.numInc(rows[i][c])
      best = r.sd
      for i in range (lo,hi):
        x = rows[i][c]
        l.numInc(x)
        r.numDec(x)
        if l.n >= enough and r.n >= enough:
          tmp = num.numXpect(l,r) * Configuration.unsuper_margin
          if tmp < best :
            cut,best = i, tmp
    return cut

  def cuts(c,lo,hi,pre):
    """
      Do the cut recursively
      :param c:
      :param lo:
      :param hi:
      :param pre:
      :return:
      """
    txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
    cut = argmin(c,lo,hi)
    if cut:
      print(txt)
      cuts(c,lo,   cut, pre + "|.. ")
      cuts(c,cut+1, hi, pre + "|.. ")
    else :
      b= band(c,lo,hi)
      print(txt + " (" + b + ")")
      for r in range (lo,hi + 1) :
        rows[r][c] = b

  def stop(c,t):
    """
      Stopping criterion
      :param c:
      :param t:
      :return:
      """
    for i in range (len(t)-1, 0 ,-1):
        if t[i][c] != "?" : return i
    return 0

  for c  in data.indeps:
    if c in data.nums:
      rows.sort(key=operator.itemgetter(c))
      most = stop(c,rows)
      print("\n-- "+ str(data.name[c]) + " ::: " + str(most + 1 )+"----------")
      cuts(c,0,most,"|.. ")

  dump(rows)

def dump(rows):
    """
    Pretty print the resulting table with dom column
    :param table
    :return nothing
    """

    t = Texttable()

    # colNames = []
    # for key, colName in table.name.items():
    #         colNames.append(colName)
    #
    # t.add_row(colNames)

    for r in rows:
        row = []
        for k, v in r.items():
            row.append(v)

        #
        # while len( row ) != len(colNames):
        #     row.append(None)

        t.add_row(row)

    print(t.draw())

if __name__ == '__main__':
  """
  Required report
  """
  print("Part 2 weatherLong.csv ")
  t = table.createTable("data/weatherLong.csv")
  unsuper(t)

