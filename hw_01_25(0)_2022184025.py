import random
random.seed(2025120101)
BIN_SIZE = 100

objs = [random.randint(5, 70) for _ in range(100)]
print(objs)

bins = []
print(bins)

def fits(bin, obj):
    return sum(bin) + obj <= BIN_SIZE

def free_size_of(bin):
    return BIN_SIZE - sum(bin)


## First Fit
for obj in objs:
    for bin in bins:
        if fits(bin, obj):
            break
    else:
        bin = []
        bins.append(bin)
    bin.append(obj)
print('First Fit: ', bins)


## Best Fit
bins = []
for obj in objs:
    bin, smallest = None, BIN_SIZE + 1
    for b in bins:
        free_size = free_size_of(b)
        if free_size < obj:
            continue
        if free_size < smallest:
            bin, smallest = b, free_size
    if not bin:
        bin = []
        bins.append(bin)
    bin.append(obj)
print('Best Fit: ', bins)


## Worst Fit
bins = []
for obj in objs:
    bin = max(bins, key=free_size_of) if len(bins) > 0 else None
    if not bin or not fits(bin, obj):
        bin = []
        bins.append(bin)
    bin.append(obj)

    # bin, largest = None, -1
    # for b in bins:
    #     free_size = free_size_of(b)
    #     if free_size < obj:
    #         continue
    #     if free_size > largest:
    #         bin, largest = b, free_size
    # if not bin:
    #     bin = []
    #     bins.append(bin)
    # bin.append(obj)
print('Worst Fit: ', bins)


## Next Fit
bins = []
last_bin = None
for obj in objs:
    if not last_bin or not fits(last_bin, obj):
        last_bin = []
        bins.append(last_bin)
    last_bin.append(obj)

print('Next Fit: ', bins)