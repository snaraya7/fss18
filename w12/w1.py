import re,traceback
import random as wheeloffortune


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
def testFunctions():
    assert double(2) == 4

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

