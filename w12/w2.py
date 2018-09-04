import re,traceback

def lines(s):
  rows = []

  for r in s.split('\n'):

     try:
        hashIndex = r.index('#')
     except ValueError:
         hashIndex = -1
     if hashIndex > 0 :
        rows.append(r[0:hashIndex].strip())
     else :
         rows.append(r.strip())

  return rows



def rows(src):
  """Kill bad characters. If line ends in ','
   then join to next. Skip blank lines."""

  rows = []
  newRow = ''
  next = False
  for r in src:

    if r.endswith(','):
        newRow += r
        next = True
    elif next:
        newRow += r
        next = False
    else:
        rows.append(r)

  rows = [newRow] + rows
  return rows


def cols(src):
  """ If a column name on row1 contains '?',
  then skip over that column."""

  cleanRows = []
  for r in src:
      if len(r.strip()) > 0:
          cleanRows.append(r)


  filteredCols = []
  colSkipIndex = -1
  for s in cleanRows:
      rowNames = s.split(",")
      for ss in rowNames:
          colSkipIndex = colSkipIndex + 1
          if '?' in ss:
              break
      break

  for r in cleanRows:

      fRow = ""
      currentIndex = 0
      for s in r.split (","):
          if colSkipIndex != currentIndex:
           fRow = fRow + s + ","

          currentIndex = currentIndex + 1

      filteredCols.append(fRow[:-1])

  return filteredCols


def prep(src):
  """ If a column name on row1 contains '$',
  coerce strings in that column to a float."""
  cleanRows = []
  for r in src:
      if len(r.strip()) > 0:
          cleanRows.append(r)

  filteredCols = []
  colSkipIndex = -1
  for s in cleanRows:
      rowNames = s.split(",")
      for ss in rowNames:
          colSkipIndex = colSkipIndex + 1
          if '$' in ss:
              break
      break

  header = True

  for r in cleanRows:

      fRow = ""
      currentIndex = 0
      for s in r.split(","):
          if colSkipIndex == currentIndex:
              if header:
                  fRow = fRow + s + ","
                  header = False
              else:
                  fRow = fRow + str(float(s)) + ","
          else:
              fRow = fRow + s + ","

          currentIndex = currentIndex + 1

      filteredCols.append(fRow[:-1])

  return filteredCols

DATA1 = """
  outlook,$temp,?humidity,windy,play
  sunny,85,85,FALSE,no
  sunny,80,90,TRUE,no
  overcast,83,86,FALSE,yes
  rainy,70,96,FALSE,yes
  rainy,68,80,FALSE,yes
  rainy,65,70,TRUE,no
  overcast,64,65,TRUE,yes
  sunny,72,95,FALSE,no
  sunny,69,70,FALSE,yes
  rainy,75,80,FALSE,yes
  sunny,75,70,TRUE,yes
  overcast,100,25,90,TRUE,yes
  overcast,81,75,FALSE,yes
  rainy,71,91,TRUE,no"""

DATA2 = """
      outlook,   # weather forecast. 
      $temp,     # degrees farenheit
      ?humidity, # relative humidity
      windy,     # wind is high
      play       # yes,no
      
      sunny,85,85,FALSE,no
      sunny,80,90,TRUE,no
      overcast,83,86,FALSE,yes
      rainy,70,96,FALSE,yes
      rainy,68,80,FALSE,yes
      rainy,65,70,TRUE,no
      overcast,64,65,TRUE,yes
      sunny,72,95,FALSE,no
      sunny,69,70,FALSE,yes
      rainy,75,80,FALSE,yes
      sunny,75,70,TRUE,yes
      overcast,100,25,90,TRUE,yes
      overcast,81,75,FALSE,yes # unique day
      rainy,71,91,TRUE,no """

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc())
    return f

def double(x):
    return x * 2

def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)