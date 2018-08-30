import re,traceback
import random as wheeloffortune
import math
from collections import Counter


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

@O.k
def testTuples():
    my_tuple = (1, 2)
    try:
        my_tuple[1] = 3
        modifyable = True
    except TypeError:
        modifyable = False

    assert modifyable == False

@O.k
def testDict():

    grades = {"Shri": 90, "kanth": 97}
    assert grades["Shri"] == 90

@O.k
def testSet():
   s = set()
   s.add('apple')
   s.add('Apple')
   s.add('apple')
   s.add('orange')

   assert len(s) == 3

@O.k
def testCount():
    c = Counter([1,1,1,3,4])
    assert c[1] == 3

@O.k
def testFunctions():
    assert double(2) == 4

@O.k
def testControlFlow():
    assert True if 10 % 2 == 0 else False


@O.k
def testTruthiness():

    space = None

    assert None == space

@O.k
def testRandom():
    assert wheeloffortune.randrange(3, 6) >= 3 and wheeloffortune.randrange(3, 6) < 6

def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
     yield i
     i += 1

def customGen():
    return (i for i in lazy_range(20) if i % 2 == 0)

@O.k
def testGenerator():
    evenList = list(customGen())
    for e in evenList:
        if e % 2 != 0:
            assert False

    assert True

@O.k
def testIte():

    sample = [1,2]
    i = 0
    for s in sample:
        sample[i] = sample[i] + 1
        i = i + 1

    assert sample[0] == 2 and sample[1] == 3

@O.k
def testRegex():
    name = "shri2018"
    passed = re.match(name, "shri2018kanth")
    name = re.sub("[0-9]", "-", name)

    assert passed and name == "shri----"

@O.k
def testListCompr():

    squares = [x * x for x in range(5)]
    test = False

    for s in squares:
        if  s !=0 and s / math.sqrt(s) != math.sqrt(s):
            assert False

    assert True



@O.k
def testSorting():
    x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
    assert x[0] <= x[len(x) - 1]

@O.k
def testModules():
    assert wheeloffortune.random() != wheeloffortune.random()

@O.k
def testStrings():
    assert "shrikanth" == 'shrikanth'

@O.k
def testLists():

    myList = [1]
    myList.extend([1])

    assert len(myList) == 2 # list contains duplicates

@O.k
def testException():

    exceptionOccurred = False

    try:
        print(0 / 0)
    except ZeroDivisionError:
        exceptionOccurred =   True

    assert exceptionOccurred

@O.k
def testArithmetic():
    assert 5 / 2 == 2.5

@O.k
def testWhitespace():

    a = 10
    b = 20

    for b in [5]:

     a = b

    assert a == 5

@O.k
def testingFailure():
  """this one must fail.. just to
  test if the  unit test system is working"""
  assert 1==2

@O.k
def testingSuccess():
  """if this one fails, we have a problem!"""
  assert 1==1

if __name__== "__main__":
  O.report()

