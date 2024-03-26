from datetime import datetime
import time


# Part 1
def clock(n: int) -> None:
  """
  Updates a clock for each seconds for a specified number of seconds

  Parameters
  ------------
  n: int
    The number of seconds to update the clock by

  Returns
  -------------
  None
  """
  counter = 0

  while counter<n:      
    hour = datetime(1,1,1,12,59,59-counter).hour
    minute = datetime(1,1,1,12,59,59-counter).minute
    second = datetime(1,1,1,12,59,59-counter).second
    print(f"{hour}:{minute}:{second}", end='\r')
    time.sleep(1)
    counter += 1


# Part 2
def lcm(a: int, b: int) -> int:
  """
  Accepts 2 integer inputs and returns the lower common multiple of them

  Parameters
  ------------
  a: int
    1st integer
  b: int
    2nd integer

  Returns
  -------------
  int
    The lcm of both numbers
  """
  ori_a = a
  ori_b = b
  while a != b:
    if a<b:
      a += ori_a
    else:
      b += ori_b
  return a


# Part 3
def gcf(a: int, b: int) -> int:
  """
  Accepts 2 integer inputs and returns the greatest common factor of them

  Parameters
  ------------
  a: int
    1st integer
  b: int
    2nd integer

  Returns
  -------------
  int
    The gcf of both numbers
  """
  while b != 0:
    r = a%b
    a,b = b,r
  return a

#clock(3)