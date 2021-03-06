import math
import operator

from texttable import Texttable

from w4 import table
from w5 import Configuration
from w13.num import num
from w5.dom import doms


def super(data,goal,enough):

  """
        Discretizing columns based on another column
        :param data:
        :param goal:
        :param enough:
        :return:
 """

  rows   = []
  intermediateMap = {}

  for key, value in data.rows.items():
      rows.append(value)

  # print(rows)
  goal   = len(rows[0])-1
  # print("goal", goal)
  enough = (len (rows))**Configuration.super_enough
  # most = 0

  def band(c,lo,hi):
        if lo==0 :
            return ".."+ str( rows[hi][c])
        elif hi == most:
            return str(rows[lo][c])+".."
        else:
            return str(rows[lo][c])+".."+str(rows[hi][c])

  def argmin(c,lo,hi):
    """
            Check the cut
            :param c:
            :param lo:
            :param hi:
            :return:
    """

    cut = None
    xl,xr = num(), num()
    yl,yr = num(), num()
    for i in range (lo,hi+1) :
      xr.numInc( rows[i][c])
      yr.numInc( rows[i][goal])


    bestx = xr.sd
    besty = yr.sd
    n = yr.n
    mu    = yr.mu


    if (hi - lo > 2*enough) :
      for i in range (lo,hi+1):
        x = rows[i][c]
        y = rows[i][goal]
        xl.numInc(x)
        xr.numDec(x)
        yl.numInc(y)
        yr.numDec(y)
        if xl.n >= enough and xr.n >= enough :
          tmpx = xl.numXpect(xr) * Configuration.super_margin
          tmpy = yl.numXpect(yr) * Configuration.super_margin
          if tmpx < bestx :
            if tmpy < besty :
              cut,bestx,besty = i, tmpx, tmpy

    intermediateMap[c] = yr.sd**2/n
    return cut,mu

  def cuts(c, lo, hi, pre):

        """
            Do the cut recursively
            :param c:
            :param lo:
            :param hi:
            :param pre:
            :return:
        """
        # s = None
        txt = str(pre)+".."+str(rows[lo][c])+".."+str(rows[hi][c])
        cut, mu = argmin(c, lo, hi)

        if cut:
            print(txt)
            cuts(c, lo, cut, pre+str("..|.. "))
            cuts(c, cut + 1, hi, pre+str("..|.. "))

        else:
            s = band(c, lo, hi)
            print(txt+str(".. ==> ..")+str(math.floor(100 * mu)))
            for r in range (lo, hi+1) :
                rows[r][c] = s

  def stop(c,t):

    """
            Stopping criterion
            :param c:
            :param t:
            :return:
    """
    # print("len t",len(t))
    # print("c",c)

    for i in range (len(t) -1,-1 -1) :
        print("print ",t[i][c])
        if t[i][c] != '?':
            return i
    return 0


  for c  in data.indeps:
        if c in data.nums :
            # rows.sort(key=operator.itemgetter(0), reverse=True)
            # print("calling stop")
            most = stop(c,rows)
            print("\n-- .. "+str(data.name[c])+" : " +str(most)+" ..  ----------")
            # print("most",most)
            cuts(c,0,most,"|.. ")

  dump(rows)

  """
   Finding the Splitter
  """
  minVar = math.inf
  for k,v in intermediateMap.items():
      minVar = min(v, minVar)

  print("split at : ",rows[int(minVar)][0])



def dump(rows):
    """
    Pretty print the resulting table with dom column
    :param table
    :return nothing
    """

    t = Texttable()

    # colNames = []
    # for   colName in [ '%outlook', '$temp' ,     '<humid'   ,    ' wind'    ,   '!play '  ,     '>dom']:
    #         colNames.append(colName)

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
  print("Test 1 weatherLong.csv ")
  t = table.createTable("data/weatherLong.csv")
  s = super(doms(t), None, None)

  print("Test 2 auto.csv ")
  t = table.createTable("data/auto.csv")
  s = super(doms(t), None, None)