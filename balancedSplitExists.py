import math
import random

def _partition_and_sum_left(inp, start, end):
  p_idx = random.randint(start,end-1)
  inp[end-1], inp[p_idx] = inp[p_idx], inp[end-1]
  p_idx = end-1
  curr_idx = start
  lsum=0
  for i in range(start,end-1):
    if inp[i] <= inp[p_idx]:
      lsum+=inp[i]
      inp[i], inp[curr_idx] = inp[curr_idx], inp[i]
      curr_idx += 1

  inp[curr_idx], inp[p_idx] = inp[p_idx], inp[curr_idx]
  return curr_idx, lsum


def canSplit(arr, start, end, target_sum):
  
  if end==start:
    return False 
  
  p_idx, lsum = _partition_and_sum_left(arr, start, end)
  
  if lsum == target_sum:
    if arr[p_idx-1] < arr[p_idx]:
      return True
    else:
      return False
  elif lsum < target_sum:
    return canSplit(arr,p_idx, end, target_sum-lsum)
  else:
    return canSplit(arr,start, p_idx, target_sum)
    
  

def balancedSplitExists(arr):
  if len(arr)<2:
    return False
  
  arr_sum = sum(arr)
  if arr_sum%2 == 1:
    return False
  
  return canSplit(arr, 0, len(arr), arr_sum/2)

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)
  
