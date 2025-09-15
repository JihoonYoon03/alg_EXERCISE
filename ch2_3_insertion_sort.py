#from data_nearly_sorted_a_lot import nearly as numbers
from data_unsorted import numbers
#from data_unsorted_a_lot import numbers
from random import randint, seed, shuffle
from pyvisalgo import InsertionSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time

def main_level_1():
    print('before:', array)
    count = len(array)

    for i in range(1, count):
        vis.mark_end(i)
        for j in range(i, 0, -1):
            vis.compare(j-1, j)
            if array[j-1] > array[j]:
                vis.swap(j-1, j)
                array[j-1], array[j] = array[j], array[j-1]

    print('after:', array)

def main_level_2():
    print('before:', array)
    count = len(array)

    for i in range(1, count):
        vis.mark_end(i)
        for j in range(i, 0, -1):
            vis.compare(j-1, j)
            if array[j-1] > array[j]:
                vis.swap(j-1, j)
                array[j-1], array[j] = array[j], array[j-1]
            else: break

    print('after :', array)

def main():
    print('before:', array)
    count = len(array)

    for i in range(1, count):
        #vis.mark_end(i, True)
        v = array[i]
        j = i
        while j > 0:
            vis.compare(j-1, j)
            if array[j-1] > v:
                vis.shift(j-1, j)
                array[j] = array[j-1]
                vis.draw()
                j -= 1
            else: break
        #vis.shift(i, j, True)
        array[j] = v
        vis.draw()

    vis.draw()

    print('after:', array)

'''
count=100   elapsed=0.000
count=1000  elapsed=0.011
count=2000  elapsed=0.046
count=3000  elapsed=0.104
count=4000  elapsed=0.186
count=5000  elapsed=0.284
count=6000  elapsed=0.412
count=7000  elapsed=0.560
count=8000  elapsed=0.755
count=9000  elapsed=0.941
count=10000 elapsed=1.165
count=15000 elapsed=2.605
count=20000 elapsed=4.692
count=30000 elapsed=10.815
count=40000 elapsed=19.556
count=50000 elapsed=30.054

거의 정렬된 데이터를 대상으로 할 때
count=  100 elapsed=  0.000
count= 1000 elapsed=  0.002
count= 2000 elapsed=  0.004
count= 3000 elapsed=  0.007
count= 4000 elapsed=  0.010
count= 5000 elapsed=  0.014
count= 6000 elapsed=  0.018
count= 7000 elapsed=  0.017
count= 8000 elapsed=  0.019
count= 9000 elapsed=  0.021
count=10000 elapsed=  0.023
count=15000 elapsed=  0.036
count=20000 elapsed=  0.047
count=30000 elapsed=  0.073
count=40000 elapsed=  0.096
count=50000 elapsed=  0.121
'''

if __name__ == '__main__':
    seed('Hello')
    vis = Visualizer('Insertion Sort')

    while True:
        count = randint(10, 30)
        array = numbers[:count]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()

        again = vis.end()
        if not again: break
