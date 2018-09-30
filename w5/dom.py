#Porting... WIP
import math
import operator
import random as rand

from texttable import Texttable
from w4 import table
from w5 import Configuration





def dom(table,row1,row2):

  s1, s2 ,n = 0,0, len(table.w)

  for c,w in table.w.items():
    a0  = row1[c]
    b0  = row2[c]
    a   = table.nums[c].numNorm(a0)
    b   = table.nums[c].numNorm(b0)
    s1 = s1 - math.pow(10,(w * (a-b)/n) )
    s2 = s2 - math.pow( 10, (w * (b-a)/n) )
  return s1/n < s2/n


def anotherRow(table, row1):

    row2 = row1
    while row1 == row2 :
        row2 = table.rows[rand.randrange(1, len(table.rows))]

    return row2


def dump(table):

    t = Texttable()

    colNames = []
    for key, colName in table.name.items():
            colNames.append(colName)

    t.add_row(colNames)



    for a, b in table.rows.items():
        row = []
        for c, d in b.items():
            row.append(d)

        while len( row ) != len(colNames):
            row.append(None)

        t.add_row(row)

    print(t.draw())



def doms(table):
  n = Configuration.samples
  c = len(table.name)
  table.name[c] = "dom"
  # port this > print(cat(t.name,",") .. ",>dom")
  for key,value in table.rows.items():

    # print(key," >> ",value)
    row1 = value
    value[c] = 0

    for s in range (n):
     row2 = anotherRow(table, row1)
     s = dom(table,row1,row2) and 1/n or 0
     row1[c] = row1[c] + s

  # dump(table)


def dumpList(table, rows, max):
    t = Texttable()

    colNames = []
    for key, colName in table.name.items():
        colNames.append(colName)

    t.add_row(colNames)

    for r in rows:

        max = max - 1
        if max <= 0:
            break

        row = []
        for k,v in r.items():
            row.append(v)

        t.add_row(row)

    print(t.draw())


if __name__ == '__main__':

    print("Test 1 auto.csv ")
    t1 = table.createTable("data/auto.csv")
    doms(t1)
    sorted_d = sorted(list(t1.rows.values()), key=operator.itemgetter(8), reverse=True)
    dumpList(t1, sorted_d, 10)
    print()

    print()
    print("Test 1 weatherLong.csv ")
    t2 = table.createTable("data/weatherLong.csv")
    doms(t2)
    sorted_d = sorted(list(t2.rows.values()), key=operator.itemgetter(5), reverse=True)
    dumpList(t2, sorted_d, 10)
    print()

    print()
    print("Test 2 auto.csv")
    print()

    print("First 10")
    t3 = table.createTable("data/auto.csv")
    doms(t3)
    sorted_d = sorted(list(t3.rows.values()), key=operator.itemgetter(8), reverse=True)
    dumpList(t3, sorted_d, 10)

    print("Last 10")
    t4 = table.createTable("data/auto.csv")
    doms(t4)
    sorted_d = sorted(list(t4.rows.values()), key=operator.itemgetter(8), reverse=False)
    dumpList(t4, sorted_d, 10)



