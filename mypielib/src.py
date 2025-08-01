#python3
from inspect import getframeinfo, stack

def src():
  '''Return file,line of caller

  :returns (str,int): file and line of caller

  Example:
  ```{doctest}

  >>> from mypielib.src import src
  >>> filename, lineno = src()
  >>> type(filename)
  <class 'str'>
  >>> lineno
  1

  ```
  '''
  caller = getframeinfo(stack()[1][0])
  return (caller.filename,caller.lineno)

if __name__ == '__main__':
  import doctest
  import os,sys
  sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
  failures, tests = doctest.testmod()
  print(f'Failures: {failures} of {tests} tests')
