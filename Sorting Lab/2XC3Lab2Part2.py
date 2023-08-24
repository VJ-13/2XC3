"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""

import random
import timeit
import math
import matplotlib.pyplot as plot

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# Quick Sort with two pivots
def quicksort2(list):
    if len(list) <= 1:
        return list
    elif len(list) == 2:
        return sorted(list)
    pivot1, pivot2 = sorted([list.pop(0), list.pop(0)])
    left, middle, right = [],[],[]
    for element in list:
        if element < pivot1:
            left.append(element)
        elif pivot1 <= element < pivot2:
            middle.append(element)
        else:
            right.append(element)
    return quicksort2(left) + [pivot1] + quicksort2(middle) + [pivot2] + quicksort2(right)

# Quick Sort with three pivots
def quicksort3(list):
    if len(list) <= 1:
        return list
    elif len(list) == 2:
        return sorted(list)
    pivot1, pivot2, pivot3 = sorted([list.pop(0), list.pop(0), list.pop(0)])
    left, middle1, middle2, right = [],[],[],[]
    for element in list:
        if element < pivot1:
            left.append(element)
        elif pivot1 <= element < pivot2:
            middle1.append(element)
        elif pivot2 <= element < pivot3:
            middle2.append(element)
        else:
            right.append(element)
   
    return quicksort3(left) + [pivot1] + quicksort3(middle1) + [pivot2] + quicksort3(middle2) + [pivot3] + quicksort3(right)

# Quick Sort with four pivots
def quicksort4(list):
    if len(list) <= 1:
        return list
    elif len(list) == 2 or len(list) == 3:
        return sorted(list)
    pivot1, pivot2, pivot3, pivot4 = sorted([list.pop(0), list.pop(0), list.pop(0),list.pop(0)])
    left, middle1, middle2, middle3, right = [],[],[],[],[]
    for element in list:
        if element < pivot1:
            left.append(element)
        elif pivot1 <= element < pivot2:
            middle1.append(element)
        elif pivot2 <= element < pivot3:
            middle2.append(element)
        elif pivot3 <= element < pivot4:
            middle3.append(element)
        else:
            right.append(element)
   
    return quicksort4(left) + [pivot1] + quicksort4(middle1) + [pivot2] + quicksort4(middle2) + [pivot3] + quicksort4(middle3) + [pivot4] + quicksort4(right)


# *************************************
         



# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def bottom_up_mergesort(L):
    step = 1
    while step < len(L):
        for i in range(0, len(L), step * 2):
            start = i
            mid = i + step
            end = min(i + step * 2, len(L))
            left = L[start:mid]
            right = L[mid:end]
            L[start:end] = merge(left, right)
        step *= 2
    return L

def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


# step is space between
# n is highest length list
# m is number of lists
size_plot = []

#Experiment 4
def experiement4(n, m, step):
    times1 = []
    times2 = []
    times3 = []
    times4 = []
    timesAll = []
    for i in range(0, n, step):
        timeQuick = 0
        timeMer = 0
        timeHeap = 0
        L = create_random_list(i, i)
        size_plot.append(i)
        for _ in range(m):
            print("Experiement 1 Running")
            copy1 = L.copy()
            copy2 = L.copy()
            copy3 = L.copy()

            # Quick Sort
            start1 = timeit.default_timer()
            quicksort(copy1)
            end1 = timeit.default_timer()
            timeQuick += end1 - start1


            # Merge Sort
            start2 = timeit.default_timer()
            mergesort(copy2)
            end2 = timeit.default_timer()
            timeMer += end2 - start2
            

            # Heap Sort
            start3 = timeit.default_timer()
            heapsort(copy3)
            end3 = timeit.default_timer()
            timeHeap += end3 - start3


            # print(time)
        times1.append(timeQuick/m)
        times2.append(timeMer/m)
        times3.append(timeHeap/m)
        timesAll.append(times1)
        timesAll.append(times2)
        timesAll.append(times3)

    
        
    
    return timesAll


size_plot = []

#experiment 5
def experiement5(size, num_of_lists, max_num_swaps):
    times1 = []
    timesAll = []
    swaps = 0
    for i in range(0, max_num_swaps):
        
        timeBub = 0
        timeOptBub = 0
        L = create_near_sorted_list(size,size, swaps)
        size_plot.append(swaps)
        for _ in range(num_of_lists):
            copy1 = L.copy()

            # QuickSort
            start1 = timeit.default_timer()
            quicksort(copy1)
            end1 = timeit.default_timer()
            timeBub += end1 - start1


            # print(time)
        swaps += 1
        times1.append(timeBub/num_of_lists)
        timesAll.append(times1)





    return timesAll
#Experiment 6
def experiment6(n, m, step):
    times1 = []
    times2 = []
    times3 = []
    times4 = []
    timesAll = []
    for i in range(0, n, step):
        timePiv1 = 0
        timePiv2 = 0
        timePiv3 = 0
        timePiv4 = 0
        L = create_random_list(i, i)
        size_plot.append(i)
        for _ in range(m):
            print("Experiement 3 Running")
            copy1 = L.copy()
            copy2 = L.copy()
            copy3 = L.copy()
            copy4 = L.copy()

            # Quick Sort 1 pivot
            start1 = timeit.default_timer()
            quicksort(copy1)
            end1 = timeit.default_timer()
            timePiv1 += end1 - start1


            # Quick Sort 2 pivot
            start2 = timeit.default_timer()
            quicksort2(copy2)
            end2 = timeit.default_timer()
            timePiv2 += end2 - start2
            

            # Quick Sort 3 pivot
            start3 = timeit.default_timer()
            quicksort3(copy3)
            end3 = timeit.default_timer()
            timePiv3 += end3 - start3


            # Quick Sort 4 pivot
            start4 = timeit.default_timer()
            quicksort4(copy4)
            end4 = timeit.default_timer()
            timePiv4 += end4 - start4
        


            # print(time)
        times1.append(timePiv1/m)
        times2.append(timePiv2/m)
        times3.append(timePiv3/m)
        times4.append(timePiv4/m)  
        timesAll.append(times1)
        timesAll.append(times2)
        timesAll.append(times3)
        timesAll.append(times4)
    
        
    
    return timesAll


#Experiment 7
def experiment7(n, m, step):
    times1 = []
    times2 = []
    timesAll = []
    for i in range(0, n, step):
        timeMerge = 0
        timeBottomMerge = 0
        L = create_random_list(i, i)
        size_plot.append(i)
        for _ in range(m):
            print("Experiment 4 Running")
            copy1 = L.copy()
            copy2 = L.copy()

            # Merge Sort
            start1 = timeit.default_timer()
            mergesort(copy1)
            end1 = timeit.default_timer()
            timeMerge += end1 - start1


            # Optimized Merge Sort
            start2 = timeit.default_timer()
            bottom_up_mergesort(copy2)
            end2 = timeit.default_timer()
            timeBottomMerge += end2 - start2
            
            # print(time)
        times1.append(timeMerge/m)
        times2.append(timeBottomMerge/m)
        timesAll.append(times1)
        timesAll.append(times2)
    return timesAll
def experiement8(max_size, num_of_lists, step):
    times1 = []
    times2 = []
    times3 = []
    timesAll = []
    for i in range(0, max_size, step):
        timeIns = 0
        timeQuick = 0
        timeMerge = 0
        L = create_random_list(i, i)
        size_plot.append(i)
        for _ in range(num_of_lists):
            copy1 = L.copy()
            copy2 = L.copy()
            copy3 = L.copy()

            # Insertion Sort
            start1 = timeit.default_timer()
            insertion_sort(copy1)
            end1 = timeit.default_timer()
            timeIns += end1 - start1


            # Selection Sort
            start2 = timeit.default_timer()
            quicksort(copy2)
            end2 = timeit.default_timer()
            timeQuick += end2 - start2


            # Bubble Sort
            start3 = timeit.default_timer()
            mergesort(copy3)
            end3 = timeit.default_timer()
            timeMerge += end3 - start3

           
        times1.append(timeIns/num_of_lists)
        times2.append(timeQuick/num_of_lists)
        times3.append(timeMerge/num_of_lists)

        timesAll.append(times1)
        timesAll.append(times2)
        timesAll.append(times3)
    
    return timesAll

step = 250
# nbSwap = 1000
size = 1000
number_of_lists = 1000

times = experiment4(size, number_of_lists, step)

plot.plot(size_plot, times[0], label = "Traditional Merge Sort")
plot.plot(size_plot, times[1], label = "Bottom-up Merge Sort")



plot.ylabel("Time")
plot.xlabel("List Size")
plot.title("Merge Sort vs Bottom-Up Merge Sort")
plot.legend()
plot.show()
