#from data_nearly_sorted_a_lot import nearly as numbers
from data_unsorted import numbers
#from data_unsorted_a_lot import numbers
from random import randint, seed, shuffle
from pyvisalgo import SelectionSortVisualizer as Visualizer, array
#from pyvisalgo import Dummy as Visualizer
from time import time

def main():
    print('before:', array)
    count = len(array)

    for a in range(count):
        min_value = array[a]
        min_at = a
        vis.selection(a)
        for b in range(a + 1, count):
            vis.compare(min_at, b)
            if min_value > array[b]:
                min_value = array[b]
                min_at = b
                vis.selection(b)
        vis.swap(a, min_at)
        array[a], array[min_at] = array[min_at], array[a]
        vis.mark_done(a)
        print(f'min_at={min_at}, swap {a} <=> {min_at}')

    print('after :', array)

'''
성능측정:
count=100   elapsed=0.000
count=1000  elapsed=0.008
count=2000  elapsed=0.031
count=3000  elapsed=0.070
count=4000  elapsed=0.124
count=5000  elapsed=0.194
count=6000  elapsed=0.282
count=7000  elapsed=0.383
count=8000  elapsed=0.521
count=9000  elapsed=0.635
count=10000 elapsed=0.773
count=15000 elapsed=1.739
count=20000 elapsed=3.161
count=30000 elapsed=7.476
count=40000 elapsed=14.590
count=50000 elapsed=24.205

거의 정렬된 데이터를 대상으로 할 때
count=  100 elapsed=  0.000
count= 1000 elapsed=  0.008
count= 2000 elapsed=  0.032
count= 3000 elapsed=  0.070
count= 4000 elapsed=  0.125
count= 5000 elapsed=  0.196
count= 6000 elapsed=  0.279
count= 7000 elapsed=  0.378
count= 8000 elapsed=  0.498
count= 9000 elapsed=  0.630
count=10000 elapsed=  0.798
count=15000 elapsed=  1.884
count=20000 elapsed=  3.615
count=30000 elapsed=  8.732
count=40000 elapsed= 18.692
count=50000 elapsed= 38.067
'''

if __name__ == '__main__':
    seed('Hello')
    vis = Visualizer('Selection Sort')

    while True:
        count = randint(10, 30)
        array = numbers[:count]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()

        again = vis.end()
        if not again: break