edges=[
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

# 엣지 리스트를 변환. i = 출발점, g[i] = { 도착점 : 비용 }
g = { i : dict() for i in range(num_vertex) }
for u, v, w in edges:
    g[u][v] = w # u에서 v로 가는 비용
    g[v][u] = w # v에서 u로 가는 비용

roots = []

mst = []
def append(s, e, w):
    if s <= e:
        mst.append((s,e,w))
    else:
        mst.append((e,s,w))
    mst.sort(key=lambda e:e[0]*1000+e[1])

from heapdict import heapdict

def prim(start):
    # D = 다음 확정할 노드들 목록 (최소 힙)
    D = heapdict()
    # key = 도착점, value = (비용, 출발점)
    D[start] = (0, start)
    # 내륙을 모아두는 셋
    completed = set()

    # main loop, 알려진 거리가 있는 동안 반복
    while D:
        # 제일 비용이 적은 아이템 pop = 노드 확정
        index_to, (weight, index_from) = D.popitem()
        completed.add(index_to)

        # 첫 번째 실행에는 다른 점과 연결되지 않으므로 제외
        if index_from != index_to:
            append(index_from, index_to, weight)

        # items로 key와 value 튜플을 얻어서 이용. adj_index: 도착점, adj_weight: 비용
        for adj_index, adj_weight in g[index_to].items():
            # 이미 확정된 노드 제외
            if adj_index in completed:
                continue
            # 추가되지 않은 노드 or 기존보다 비용이 적은 경로인 경우 갱신
            if not adj_index in D or D[adj_index][0] > adj_weight:
                D[adj_index] = adj_weight, index_to

prim(8)

print('[')
for result in mst:
    print(f'({result[0]}, {result[1]}, {result[2]}),')
print(']')