#Time Complexity Verifications of Different Search Methods.
# This program Efficient to check the Different Methods Verifying the Smallest Element within the List .

import time
import numpy
import random


def sort1_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length-1])
    print("Smallest element is:", list1[0])
    print("Second Largest element is:", list1[length-2])
    print("Second Smallest element is:", list1[1])
    print("Third Largest element is:", list1[length-3])
    print("Third Smallest element is:", list1[2])
 

def another_method(list1,list2):
   for i in range (0,3):
      shortest = min(list1)
      second_shortest = min(list2)
      max1 = max(list1)
      max2 = max(list2)
      if ( shortest < second_shortest):
         print ( " shortest Element List ", shortest)
         list1.remove(shortest)
      else: 
         print (" Shortest Element List ", second_shortest)
         list2.remove(second_shortest)
      if ( max1 > max2):
         print ( " Largest Element List ", max1)
         list1.remove(max1)
      else: 
         print (" Largest Element List ", max2)
         list2.remove(max2)


def another_method1(list1):
   #list refer method 
   for i in range (0,3):
      shortest = min(list1)
      second_shortest = min(list2)
      max1 = max(list1)
      #print ( shortest)
      #print (second_shortest)
      print ( " shortest Element List ", shortest)
      print ( " Largest Element List ", max1)
      list1.remove(shortest)
      list1.remove(max1)


def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')


def merge_sort(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    merge_sort(left_data)
    merge_sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]

 
if __name__ =='__main__':

   print (" Analyser of the Best Method1 of the Data Finding on the shortest between two List.")   
   #list1  =   [12, 45, 2, 41, 31, 10, 8, 6, 4]
   #list2  =   [22, 85, 62, 40, 55, 12, 39, 2, 43]
   list1 = random.sample(range(1000, 700000), 300000)
   list2 = random.sample(range(7000, 700000), 300000)
   start_time = time.time()
   Largest = sort1_len(list1+list2)
   print("--- %s seconds ---" % (time.time() - start_time))
   print (" Analyser of the Best Method2 of the Data Finding on the shortest between two List.") 
   start_time = time.time()
   another_method(list1.copy(),list2.copy())
   print("--- %s seconds ---" % (time.time() - start_time))
   print (" Analyser of the Best Method3 of the Data Finding on the shortest between two List.")  
   start_time = time.time()
   another_method1(list1.copy()+list2.copy())
   print("--- %s seconds ---" % (time.time() - start_time))
  

   
