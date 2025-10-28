#boba.py
import random
import time
import signature
st = time.time()
actswap = 0
def bubble_sort(arr, opt = True):
    try:
        global actswap
        SET = "   "
        actswap = 0
        actswapz = 0
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    SET = "swap"
                    actswap = actswap + 1
                else:
                    SET = "no swap"
                actswapz = actswapz + 1
            wando = abs(actswapz-n)
            print(arr, SET)
            if opt:
              time.sleep(0.05)
        print("actial swaps", actswap)
        print(f"O({n**2})")
        print("actual swap (BUT Z MODE!!!!!)", actswapz)
        print("(comparisons)")
        return arr
    except Exception as error:
      print(error)
def setup_boba(lenth, opt = True):
  arr = [0]
  for i in range(lenth):
    arr.append(i+1)
    print("added", i+1)
  random.shuffle(arr)
  return(bubble_sort(arr, opt))
if __name__ == "__main__":
  print("WELCOME TO BOBA \n TIME TO BUBBLESORT WE LOVE BUBBLESORT")
  setup_boba(int(input("length")), bool(input("opt")))