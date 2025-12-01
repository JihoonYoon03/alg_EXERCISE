from heapdict import heapdict

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
start = 8

# MST

# graph 생성 (가중치 있음. 딕셔너리-딕셔너리. {출발지: {도착지 : 가중치}}
g = { u : dict() for u in range(num_vertex) } # 모든 출발점에 대해 빈 딕셔너리로 초기화
for u, v, w in edges:
    g[u][v] = w
    g[v][u] = w

# prim
D = heapdict() # key = vertex_to = v, value = (weight = w, vertex_from = u)
inland = set()
mst = []
D[start] = (0, start)

while D:
    v_to, (weight, v_from) = D.popitem()

    inland.add(v_to) # v_to 확정 (내륙으로 포함)
    if v_from != v_to: # 시작점-시작점은 간선 없음
        mst.append((v_from, v_to, weight))

    for adj, adj_w in g[v_to].items(): # 확정된 점 v_to 주위 점들 adj들에 대해
        if adj in inland: continue # 1. adj = 확정된 점일 경우 무시
        if adj in D and D[adj][0] < adj_w: continue # 2. 기존에 추가한 간선 비용이 더 적으면 무시
        D[adj] = adj_w, v_to # 3 + 4. 새로운 간선 추가 혹은 기존보다 비용이 싸서 추가


## TSP

# graph 생성 (가중치 없음. 키만 존재하므로 딕셔너리-셋)
mg = { u:set() for u in range(num_vertex) } # 모든 출발점에 대해 빈 세트로 초기화
for u, v, w in mst:
    mg[u].add(v)
    mg[v].add(u)

# sequence 생성
seq = [ start ]
current = start
while True:
    if not mg[current]: break # 갈 곳이 없으면 그만한다

    for k in mg[current]:
        if k not in seq: # 아직 방문 목록에 없는 점이면 선택한다
            visit = k
            break
    else:
        visit = list(mg[current])[0] # 방문 안한 점이 없으면 첫번째 점으로 간다

    seq.append(visit)           # 방문할 정점들에 추가
    mg[current].remove(visit)   # 선택한 점은 재방문을 막기 위한 삭제
    current = visit             # 선택할 점으로 진행한다.

print('--- before removing duplicates ---')
print(seq)

# 중복방문 삭제
index = 0
visited = set()
while index < len(seq):
    v = seq[index]
    if v in visited:    # 방문했던 점이라면
        seq.pop(index)
    else:               # 그렇지 않다면
        visited.add(v)
        index += 1

seq.append(start)

print('--- after removing duplicates ---')
print(seq)