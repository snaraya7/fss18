from w13.num import num
from w13.sym import sym
from w13.sample import sample
from texttable import Texttable
import re,csv

class table:


    def __init__(self):
        """
        A table object to represent rows that holds and works with
        both num and sym instance
        """
        self.use = {}
        self.w={}
        self.syms = {}
        self.nums = {}
        self.clazz = None
        self.rows = {}
        self.name = {}
        self. indeps = {}


    def row(self,cells):
          """
         Adds a row to this table instance
          :param cells:
          :return:
          """
          r= len(self.rows) + 1
          self.rows[r] = {}
          for c,c0 in self.use.items():
            x = cells[c0]
            if x != '?':
              if c0 in self.nums.keys():
                x = float(x)
                self.nums[c].numInc(x)
              else:
                self.syms[c].symInc(x)
            self.rows[r][c] = x

    def dep(self, c):
        """
        Check if this column is a dependent column
        :param c:
        :return: True/False
        """
        return not self.indep(c)

    def indep(self,c):
        """
        Check if this column is an independent column
        :param c:
        :return: True/False
        """
        return not self.w[c] and self.clazz != c

    def printReport(self, fileName):
        """
        Pretty print the table instance for a given csv input
        :param fileName:
        :return:
        """

        t = Texttable()
        t.add_rows([[' ', ' ', 'n' , 'mode' ,'frequency']])
        print("-------------- ",str(fileName)," ---------------------------\n")
        for key, symVal in self.syms.items():
            t.add_row([str(key), self.name[key], symVal.n, symVal.mode, symVal.most])

        print (t.draw())


        t = Texttable()
        t.add_rows([[' ', ' ', 'n', 'mu', 'sd']])

        for key, numVal in self.nums.items():
            t.add_row([str(key), self.name[key], numVal.n, numVal.mu, numVal.sd])

        print(t.draw())


def header(cells):
  """
   To read and process special symbols for input rows
  :param cells:
  :return:
  """

  t = table()
  for c0,x in enumerate(cells):
    if "?" not in x:
      c = len(t.use)
      t.use[c] = c0
      t.name[c] = x
      if re.search("[<>$]", x):
        t.nums[c] = num(1000)
      else :
          t.syms[c] = sym()
      if     "<" in x :
         t.w[c]  = -1
      elif ">" in x:
        t.w[c]  =  1
      elif "!" in x:
        t.clazz =  c
      else:
          t.indeps[ len(t.indeps) + 1 ] = c

  return t


def createTable(fileName):
    """
    Reads csv from disk using fileName
    :param fileName: csv relative file path
    :return: a table object with only header or all data rows.
    """

    newTable = table()
    lineNumber = 1
    with open(fileName) as csv_file:
        csvRows = ''
        readerElements = csv.reader(csv_file, delimiter=',')
        for row in readerElements:
            cells = row #row.split(",")
            if lineNumber > 1:
                 newTable.row(cells)
            else :
                lineNumber += 1
                newTable = header(cells)


    return newTable




if __name__ == "__main__":

    """
    Prints the statistics for each csv
    """
    autoTable = createTable("data/auto.csv")
    autoTable.printReport("auto.csv")

    weatherTable = createTable("data/weather.csv")
    weatherTable.printReport("weather.csv")

    weatherLongTable = createTable("data/weatherLong.csv")
    weatherLongTable.printReport("weatherLong.csv")
