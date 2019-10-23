#Fibonacci search


import math 
  
def isPerfectSquare(num): 
  
    n = int(math.sqrt(num)) 
    return (n * n == num) 
  
   
def checkFib(array, n): 
  
    count = 0
    for i in range(n): 
      
        if (isPerfectSquare(5 * array[i] * array[i] + 4) or 
            isPerfectSquare(5 * array[i] * array[i] - 4)): 
          
            print(array[i], " ", end =""); 
            count = count + 1
          
      
    if (count == 0): 
        print("None present"); 
  
  
array = [4, 2, 8, 5, 20, 1, 40, 13, 23] 
n = len(array) 
   
checkFib(array, n) 
