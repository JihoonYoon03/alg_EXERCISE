#from data_nearly_sorted_a_lot import nearly as numbers
from data_unsorted import numbers
#from data_unsorted_a_lot import numbers
#number = numbers[:1000]

from random import randint, seed, shuffle
from time import time

from pyvisalgo import BubbleSortVisualizer as Visualizer
#from pyvisalgo import Dummy as Visualizer

def main():
    print('before:', array)
    count = len(array)
    end = count - 1
    while end > 0:
        last = 1
        for i in range(end):
            vis.compare(i, i + 1)
            if array[i] > array[i+1]:
                vis.swap(i, i + 1)
                array[i], array[i+1] = array[i+1], array[i]
                last = i + 1
        end = last - 1
        vis.bubble_end(last)
    vis.bubble_end(0)
    print('after:', array)

''' 
* Dummy Visualizer 를 썼을 때
count=100   elapsed=0.001
count=1000  elapsed=0.093
count=2000  elapsed=0.370
count=3000  elapsed=0.830
count=4000  elapsed=1.445

* Visualizer 코드를 완전히 제거했을 때
count=100   elapsed=0.000
count=1000  elapsed=0.023
count=2000  elapsed=0.096
count=3000  elapsed=0.221
count=4000  elapsed=0.379
count=5000  elapsed=0.609
count=6000  elapsed=0.872
count=7000  elapsed=1.183
count=8000  elapsed=1.548
count=9000  elapsed=1.940
count=10000 elapsed=2.401
count=15000 elapsed=5.439
count=20000 elapsed=9.739

거의 정렬된 데이터를 대상으로 할 때
count=100   elapsed=0.000
count=1000  elapsed=0.010
count=2000  elapsed=0.027
count=3000  elapsed=0.050
count=4000  elapsed=0.071
count=5000  elapsed=0.095
count=6000  elapsed=0.109
count=7000  elapsed=0.137
count=8000  elapsed=0.165
count=9000  elapsed=0.185
count=10000 elapsed=0.195
count=15000 elapsed=0.314
count=20000 elapsed=0.426
count=30000 elapsed=0.887
count=40000 elapsed=1.192
count=50000 elapsed=1.538
'''

if __name__ == '__main__':
    seed('Hello')
    vis = Visualizer('Bubble Sort')

    while True:
        count = randint(10, 30)
        array = numbers[:count]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()

        again = vis.end()
        if not again: break