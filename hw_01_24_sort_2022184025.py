edges = [
    (0, 3, 288), (0, 16, 390), (0, 21, 346), (1, 4, 449), (1, 7, 346),
    (1, 13, 325), (2, 21, 335), (3, 6, 231), (3, 11, 437), (3, 17, 140),
    (3, 18, 325), (3, 19, 362), (3, 20, 323), (4, 7, 457), (4, 10, 234),
    (4, 15, 399), (5, 7, 101), (5, 10, 445), (5, 12, 261), (5, 13, 234),
    (5, 21, 364), (6, 19, 304), (6, 20, 461), (7, 12, 362), (7, 13, 288),
    (7, 21, 445), (8, 9, 230), (8, 22, 365), (9, 18, 154), (9, 22, 191),
    (10, 21, 433), (11, 15, 381), (11, 17, 400), (11, 20, 113), (12, 15, 402),
    (12, 21, 260), (14, 15, 320), (14, 19, 454), (14, 20, 326), (15, 17, 453),
    (15, 19, 243), (15, 20, 394), (16, 17, 308), (16, 18, 214), (17, 21, 430),
    (18, 22, 262), (19, 20, 318), (19, 21, 391)
]

num_vertex = 23

## Set Cover

# u, f
n_edges = len(edges)
U = set(list(range(n_edges))) # edge indexes
f = [set() for i in range(num_vertex)] # index : vertex, value : edges set
for i in range(n_edges):
    u,v,w = edges[i]
    f[u].add(i) # 정점 u 선택 시 i가 커버됨
    f[v].add(i) # 정점 v ''

# n x n x n
C = []
while U:
    max_i = f.index(max(f, key=lambda s: len(s & U)))
    S = f[max_i] # F 에서 U 와의 교집합이 가장 큰 부분집합
    C.append(max_i)
    U -= S       # U 에서 해당 부분집합의 원소를 제거한다
    # print(f'Selecting {S}, Now u = {U}')
    f[max_i] = set()

print('Selected vertices:', sorted(C))


## Max Matching

# graph build
adjs = [ set() for _ in range(num_vertex) ]
for u, v, w in edges:
    adjs[u].add(v)
    adjs[v].add(u)
print('Adj List:', adjs)

# search matching
vc = []
edge_count = 0

from random import randrange
vertices = list(range(num_vertex))

while edge_count < n_edges:
    rand_index = randrange(len(vertices))
    u = vertices.pop(rand_index)
    if not adjs[u]: continue
    v = adjs[u].pop()

    # print(f'{(u,v)=}')
    for n in (u, v):
        # print(f'----- {n=} ----- {adjs[n]=}')
        vc.append(n)

        for k in range(num_vertex):
            if k in adjs[n]:
                adjs[n].remove(k)
                if n in adjs[k]:
                    adjs[k].remove(n)
                edge_count += 1

        # while adjs[n]:
        #     k = adjs[n].pop()
        #     # print(f'{k=} {adjs[k]=}')
        #     if n in adjs[k]:
        #         adjs[k].remove(n)
        #     edge_count += 1

print('VC List:', sorted(vc))