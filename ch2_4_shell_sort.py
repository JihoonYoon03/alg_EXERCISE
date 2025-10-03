# from data_unsorted import numbers
from data_unsorted_a_lot import numbers
# from pyvisalgo import ShellSortVisualizer as Visualizer, array
# from pyvisalgo import Dummy as Visualizer

from random import randint, seed, shuffle
from time import time

# GAPS = [1750, 701, 301, 141, 63, 31, 15, 7, 3, 1, 0]
GAPS = [131071, 65535, 32767, 16383, 8191, 4095, 1750, 701, 301, 132, 57, 23, 10, 4, 1, 0]

def next_gap(gap):
    for g in GAPS:
        if gap > g: return g

def main_level_1():
    print('before:', array)
    count = len(array)
    gap = next_gap(count / 2.5)
    print(f'{count=} first_gap={gap}')
    while True:
        vis.set_gap(gap)
        for offset in range(gap):
            start = offset + gap
            while start < count:
                vis.mark_end(start, True)
                v = array[start]
                i = start
                while i >= gap:
                    vis.compare(i-gap, i)
                    if array[i - gap] > v:
                        vis.shift(i-gap, i)
                        array[i] = array[i - gap]
                        vis.draw()
                        i -= gap
                    else:
                        break
                vis.shift(start, i, True)
                array[i] = v
                vis.draw()
                start += gap
        gap = next_gap(gap)
        if gap < 1: break
    print('after:', array)

def main():
    # print('before:', array)
    count = len(array)
    gap = next_gap(count / 2.5)
    # print(f'{count=} first_gap={gap}')
    while True:
        # vis.set_gap(gap)
        for start in range(gap, count):
            # vis.mark_end(start, True)
            v = array[start]
            i = start
            while i >= gap:
                # vis.compare(i-gap, i)
                if array[i - gap] > v:
                    # vis.shift(i-gap, i)
                    array[i] = array[i - gap]
                    # vis.draw()
                    i -= gap
                else:
                    break
            # vis.shift(start, i, True)
            array[i] = v
            # vis.draw()
            start += gap
        gap = next_gap(gap)
        if gap < 1: break
    # print('after:', array)


'''
count=   100 elapsed=  0.000
count=  1000 elapsed=  0.001
count=  2000 elapsed=  0.002
count=  3000 elapsed=  0.003
count=  4000 elapsed=  0.004
count=  5000 elapsed=  0.005
count=  6000 elapsed=  0.006
count=  7000 elapsed=  0.007
count=  8000 elapsed=  0.008
count=  9000 elapsed=  0.009
count= 10000 elapsed=  0.011
count= 15000 elapsed=  0.017
count= 20000 elapsed=  0.023
count= 30000 elapsed=  0.038
count= 40000 elapsed=  0.053
count= 50000 elapsed=  0.074
count=100000 elapsed=  0.158
count=200000 elapsed=  0.350
count=300000 elapsed=  0.544
count=400000 elapsed=  0.760
count=500000 elapsed=  1.111
'''

if __name__ == '__main__':
    seed('Hello')

    counts = [
        100, 1000, 2000, 3000, 4000, 5000,
        6000, 7000, 8000, 9000, 10000, 15000,
        20000, 30000, 40000, 50000,
        100000, 200000, 300000, 400000, 500000,
    ]
    for count in counts:
        array = numbers[:count]
        shuffle(array)
        startedOn = time()
        main()
        elapsed = time() - startedOn
        print(f'{count=:6d} {elapsed=:7.3f}')
    exit()

    vis = Visualizer('Shell Sort')

    while True:
        count = randint(10, 30)
        array = numbers[:count]
        vis.setup(vis.get_main_module())
        main()
        # vis.set_gap(1)
        vis.mark_end(0)
        # vis.draw()

        again = vis.end()
        if not again:
            break